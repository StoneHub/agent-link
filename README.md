# Agent Link

Agent Link is a local-first Codex/OpenClaw plugin project for pairing persistent personal agents with transient work agents.

The goal is to reduce **TTBU: Time To Being Useful**. A fresh coding agent should not spend the first several minutes rediscovering who the user is, where the persistent agent lives, how to reach it, what agent ID to use, or what context matters. Agent Link stores that known-good path and gives the agent a small set of safe commands for getting briefed and handing work back.

The first release is intentionally chat-only:

- discover or configure known agents on localhost, LAN, or Tailnet
- verify reachability and the remote agent runtime
- ask a persistent agent for a compact briefing
- send context or session summaries back to that agent
- keep remote tool access disabled until explicit scoped grants exist

## Why

Transient coding agents lose time rediscovering the user's environment. A persistent home agent often already knows the user's preferences, devices, projects, and recent context. Agent Link aims to reduce TTBU: Time To Being Useful.

This project is designed for setups where:

- a persistent home or server agent keeps long-lived memory and device context
- a developer uses short-lived Codex, CLI, or IDE agents for focused work
- the machines can reach each other over localhost, LAN, SSH, or a Tailnet
- the user wants chat and context handoff before allowing remote tools

## Design Principles

- **Chat first**: v0.1 moves text context only. No remote tool execution.
- **Tailnet-friendly**: private-network hosts should be first-class, not an afterthought.
- **No trust by reachability**: being on the same Tailnet or LAN is not authorization.
- **Explicit grants later**: printers, scanners, smart-home controls, files, and other tools need scoped approval before use.
- **A2A-compatible direction**: use Agent2Agent concepts for public interoperability instead of inventing a new protocol.
- **MCP later for tools**: use MCP-style tool grants only after the chat/pairing layer is boring and reliable.

## Current State

This repo contains the first working scaffold:

- `plugins/agent-link/.codex-plugin/plugin.json` - Codex plugin manifest
- `plugins/agent-link/skills/agent-link/SKILL.md` - agent-facing workflow
- `plugins/agent-link/scripts/agent_link.py` - local helper for profiles, probes, briefings, and handoff messages
- `plugins/agent-link/docs/design.md` - v0.1 design
- `.agents/plugins/marketplace.json` - repo-local marketplace entry

The helper currently supports an SSH + OpenClaw CLI bridge. That is intentionally practical: it lets Agent Link help existing OpenClaw hosts before every runtime exposes a polished A2A server.

## Quick Start

Add the known OpenClaw host:

```powershell
python .\plugins\agent-link\scripts\agent_link.py profile add openclaw-home --host 100.104.71.37 --user monroe --openclaw-bin /home/monroe/.local/bin/openclaw --agent main
```

Probe it:

```powershell
python .\plugins\agent-link\scripts\agent_link.py probe openclaw-home
```

Ask for a briefing:

```powershell
python .\plugins\agent-link\scripts\agent_link.py brief openclaw-home
```

Ask the persistent agent a specific question:

```powershell
python .\plugins\agent-link\scripts\agent_link.py ask openclaw-home "What should this coding agent know before working on Agent Link?"
```

Send a handoff summary before ending a session:

```powershell
python .\plugins\agent-link\scripts\agent_link.py handoff openclaw-home --summary "Scaffolded the repo, added a Codex plugin manifest, wrote the v0.1 helper, and validated profile probing."
```

## Commands

```text
profile add     Add or replace a named agent profile
profile list    Show configured profiles
probe           Verify SSH, OpenClaw CLI, and Gateway reachability
brief           Ask the persistent agent for a concise working briefing
ask             Send a chat-only message to the linked agent
handoff         Send a session summary back to the linked agent
```

Profiles are stored under `~/.agent-link/profiles.json` by default. Set `AGENT_LINK_HOME` to use a different config directory for tests or isolated work.

## Security Model

Agent Link v0.1 does not store passwords. It expects SSH key auth, platform credential helpers, or another user-approved transport.

Profiles are routing hints, not trust grants. A profile can say where an agent lives and how to call it, but future versions still need explicit pairing, revocation, audit logs, and scoped tool grants before any physical or high-impact action is allowed.

Examples of actions that must stay out of v0.1:

- printing or scanning
- smart-home control
- file migration or deletion
- shell execution on another host
- reading secrets or credential stores

## Roadmap

- v0.1: SSH/OpenClaw chat bridge, profiles, probe, brief, ask, handoff
- v0.2: pairing metadata, local profile verification, better transcript storage
- v0.3: A2A Agent Card export/import and A2A-compatible message surface
- v0.4: context packets and project handoff artifacts
- v0.5: explicit MCP/tool grants with confirmations and audit logs

## Direction

Agent Link should become A2A-compatible, but it should not wait for every local agent runtime to expose a polished A2A server. The first useful bridge can use SSH/OpenClaw CLI profiles while keeping the public model aligned with A2A Agent Cards, message tasks, and later MCP tool grants.

The long-term shape is a user-installable bridge for persistent personal agents and transient work agents: local-first, private-network friendly, explicit about trust, and useful within seconds.
