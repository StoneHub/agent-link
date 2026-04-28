#!/usr/bin/env python3
"""Agent Link v0 helper.

Stores named SSH/OpenClaw profiles and sends chat-only messages to a remote
OpenClaw agent. It intentionally does not store passwords or expose tools.
"""

from __future__ import annotations

import argparse
import json
import os
import shlex
import subprocess
import sys
from pathlib import Path
from typing import Any


CONFIG_DIR = Path(os.environ.get("AGENT_LINK_HOME", Path.home() / ".agent-link"))
PROFILES_PATH = CONFIG_DIR / "profiles.json"


def load_profiles() -> dict[str, Any]:
    if not PROFILES_PATH.exists():
        return {"profiles": {}}
    with PROFILES_PATH.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if "profiles" not in data or not isinstance(data["profiles"], dict):
        raise SystemExit(f"Invalid profile store: {PROFILES_PATH}")
    return data


def save_profiles(data: dict[str, Any]) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with PROFILES_PATH.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, sort_keys=True)
        handle.write("\n")


def get_profile(name: str) -> dict[str, Any]:
    data = load_profiles()
    profile = data["profiles"].get(name)
    if not profile:
        known = ", ".join(sorted(data["profiles"])) or "none"
        raise SystemExit(f"Unknown profile {name!r}. Known profiles: {known}")
    return profile


def ssh_target(profile: dict[str, Any]) -> str:
    user = profile.get("user")
    host = profile.get("host")
    if not user or not host:
        raise SystemExit("Profile requires user and host")
    return f"{user}@{host}"


def run_ssh(profile: dict[str, Any], remote_command: str, timeout: int = 60) -> subprocess.CompletedProcess[str]:
    command = [
        "ssh",
        "-o",
        "BatchMode=yes",
        "-o",
        "ConnectTimeout=10",
        ssh_target(profile),
        remote_command,
    ]
    return subprocess.run(
        command,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
        check=False,
    )


def openclaw_command(profile: dict[str, Any], *args: str) -> str:
    binary = profile.get("openclawBin", "openclaw")
    return " ".join([shlex.quote(binary), *[shlex.quote(arg) for arg in args]])


def parse_agent_text(stdout: str) -> str:
    try:
        data = json.loads(stdout)
    except json.JSONDecodeError:
        return stdout.strip()
    payloads = data.get("result", {}).get("payloads", [])
    texts = [item.get("text", "") for item in payloads if item.get("text")]
    if texts:
        return "\n\n".join(texts).strip()
    return json.dumps(data, indent=2)


def cmd_profile_add(args: argparse.Namespace) -> None:
    data = load_profiles()
    data["profiles"][args.name] = {
        "id": args.name,
        "transport": "ssh-openclaw-cli",
        "host": args.host,
        "user": args.user,
        "openclawBin": args.openclaw_bin,
        "agent": args.agent,
        "capabilities": ["chat", "brief", "handoff"],
        "toolGrants": [],
    }
    save_profiles(data)
    print(f"Saved profile {args.name!r} to {PROFILES_PATH}")


def cmd_profile_list(_: argparse.Namespace) -> None:
    data = load_profiles()
    print(json.dumps(data["profiles"], indent=2, sort_keys=True))


def cmd_probe(args: argparse.Namespace) -> None:
    profile = get_profile(args.name)
    checks = {
        "hostname": "hostname",
        "whoami": "whoami",
        "openclawVersion": openclaw_command(profile, "--version"),
        "gatewayStatus": openclaw_command(profile, "gateway", "status", "--json"),
    }
    result: dict[str, Any] = {"profile": args.name, "ok": True, "checks": {}}
    for key, remote in checks.items():
        proc = run_ssh(profile, remote, timeout=args.timeout)
        ok = proc.returncode == 0
        result["checks"][key] = {
            "ok": ok,
            "stdout": proc.stdout.strip(),
            "stderr": proc.stderr.strip(),
        }
        result["ok"] = result["ok"] and ok
    print(json.dumps(result, indent=2))
    if not result["ok"]:
        raise SystemExit(1)


def send_agent_message(profile: dict[str, Any], message: str, timeout: int) -> str:
    agent = profile.get("agent", "main")
    remote = openclaw_command(
        profile,
        "agent",
        "--agent",
        agent,
        "--json",
        "--timeout",
        str(timeout),
        "--message",
        message,
    )
    proc = run_ssh(profile, remote, timeout=timeout + 30)
    if proc.returncode != 0:
        raise SystemExit((proc.stderr or proc.stdout).strip())
    return parse_agent_text(proc.stdout)


def cmd_ask(args: argparse.Namespace) -> None:
    profile = get_profile(args.name)
    print(send_agent_message(profile, args.message, args.timeout))


def cmd_brief(args: argparse.Namespace) -> None:
    profile = get_profile(args.name)
    prompt = (
        "Brief this transient coding agent before it starts work. "
        "Summarize the user's working preferences, relevant environment facts, "
        "active project context, and any cautions. Keep it concise. Avoid secrets."
    )
    print(send_agent_message(profile, prompt, args.timeout))


def cmd_handoff(args: argparse.Namespace) -> None:
    profile = get_profile(args.name)
    prompt = (
        "Record this handoff from a transient agent. Keep durable memory only if useful. "
        "Summary:\n"
        f"{args.summary}"
    )
    print(send_agent_message(profile, prompt, args.timeout))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Agent Link chat-only profile helper")
    sub = parser.add_subparsers(dest="command", required=True)

    profile = sub.add_parser("profile", help="Manage profiles")
    profile_sub = profile.add_subparsers(dest="profile_command", required=True)
    add = profile_sub.add_parser("add", help="Add or replace a profile")
    add.add_argument("name")
    add.add_argument("--host", required=True)
    add.add_argument("--user", required=True)
    add.add_argument("--openclaw-bin", default="openclaw")
    add.add_argument("--agent", default="main")
    add.set_defaults(func=cmd_profile_add)
    listing = profile_sub.add_parser("list", help="List profiles")
    listing.set_defaults(func=cmd_profile_list)

    probe = sub.add_parser("probe", help="Probe a profile")
    probe.add_argument("name")
    probe.add_argument("--timeout", type=int, default=30)
    probe.set_defaults(func=cmd_probe)

    ask = sub.add_parser("ask", help="Send a chat-only message")
    ask.add_argument("name")
    ask.add_argument("message")
    ask.add_argument("--timeout", type=int, default=600)
    ask.set_defaults(func=cmd_ask)

    brief = sub.add_parser("brief", help="Ask for a working-context briefing")
    brief.add_argument("name")
    brief.add_argument("--timeout", type=int, default=600)
    brief.set_defaults(func=cmd_brief)

    handoff = sub.add_parser("handoff", help="Send a session handoff summary")
    handoff.add_argument("name")
    handoff.add_argument("--summary", required=True)
    handoff.add_argument("--timeout", type=int, default=600)
    handoff.set_defaults(func=cmd_handoff)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
