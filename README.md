# Agent Link

Agent Link is a local-first Codex/OpenClaw plugin project for pairing persistent personal agents with transient work agents.

The first release is intentionally chat-only:

- discover or configure known agents on localhost, LAN, or Tailnet
- verify reachability and the remote agent runtime
- ask a persistent agent for a compact briefing
- send context or session summaries back to that agent
- keep remote tool access disabled until explicit scoped grants exist

## Why

Transient coding agents lose time rediscovering the user's environment. A persistent home agent often already knows the user's preferences, devices, projects, and recent context. Agent Link aims to reduce TTBU: Time To Being Useful.

## Current State

This repo contains the first scaffold:

- `plugins/agent-link/.codex-plugin/plugin.json` - Codex plugin manifest
- `plugins/agent-link/skills/agent-link/SKILL.md` - agent-facing workflow
- `plugins/agent-link/scripts/agent_link.py` - local helper for profiles, probes, briefings, and handoff messages
- `plugins/agent-link/docs/design.md` - v0.1 design
- `.agents/plugins/marketplace.json` - repo-local marketplace entry

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

## Direction

Agent Link should become A2A-compatible, but it should not wait for every local agent runtime to expose a polished A2A server. The first useful bridge can use SSH/OpenClaw CLI profiles while keeping the public model aligned with A2A Agent Cards, message tasks, and later MCP tool grants.

