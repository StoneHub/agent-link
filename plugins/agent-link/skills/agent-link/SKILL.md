---
name: agent-link
description: Connect to a known persistent agent such as OpenClaw over a local, LAN, or Tailnet profile for chat-only briefings and context handoff. Use when Codex needs to ask another agent what it knows about the user, environment, project history, preferences, or needs to send a session summary back. Do not use for remote tool execution; v0.1 is chat and context only.
---

# Agent Link

Use Agent Link to reduce Time To Being Useful when a transient agent needs context from a persistent agent.

## Rules

- Keep v0.1 chat-only.
- Do not request remote tool execution through Agent Link.
- Do not store or echo passwords.
- Treat Tailnet reachability as network access, not authorization.
- Ask the user before sending sensitive project content to a linked agent.
- Prefer a stored profile over rediscovering host paths and agent IDs.

## Helper

From the repo root, use:

```powershell
python .\plugins\agent-link\scripts\agent_link.py --help
```

Common commands:

```powershell
python .\plugins\agent-link\scripts\agent_link.py profile list
python .\plugins\agent-link\scripts\agent_link.py probe openclaw-home
python .\plugins\agent-link\scripts\agent_link.py brief openclaw-home
python .\plugins\agent-link\scripts\agent_link.py ask openclaw-home "What should this agent know before working on this project?"
python .\plugins\agent-link\scripts\agent_link.py handoff openclaw-home --summary "Changed X, tested Y, next step Z."
```

## Workflow

1. Run `profile list`.
2. If no profile exists, create one with `profile add`.
3. Run `probe <profile>`.
4. Run `brief <profile>` before doing project work.
5. Work normally.
6. Run `handoff <profile> --summary "<summary>"` before ending a session when useful.

## Profile Guidance

The OpenClaw home-agent profile should include:

- `host`: Tailnet hostname or IP
- `user`: SSH user
- `openclawBin`: full remote OpenClaw CLI path
- `agent`: default OpenClaw agent ID, usually `main`

Example:

```powershell
python .\plugins\agent-link\scripts\agent_link.py profile add openclaw-home --host 100.104.71.37 --user monroe --openclaw-bin /home/monroe/.local/bin/openclaw --agent main
```

