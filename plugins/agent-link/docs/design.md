# Agent Link Design

Date: 2026-04-28

## Goal

Reduce Time To Being Useful for agents that join a user's work midstream.

Agent Link connects a transient work agent, such as Codex IDE or a CLI coding agent, to a persistent personal agent, such as OpenClaw running on a home/Tailnet host. The first version shares chat and context only. Remote tool execution is deliberately out of scope until explicit grants are designed.

## User Model

The user installs Agent Link on machines that run agents. A persistent agent can stay online with memory, home devices, printers, scanners, messaging channels, and project context. A transient agent can connect, ask for a briefing, work, and send a handoff summary back.

## Version 0.1 Scope

- Maintain named profiles for known agents.
- Support SSH + OpenClaw CLI as the first practical transport.
- Probe reachability, OpenClaw CLI path, version, gateway status, and default agent.
- Ask the remote agent for a concise environment/preference/project briefing.
- Send chat messages to the remote agent.
- Send a session handoff summary to the remote agent.
- Store no passwords and grant no remote tools.

## Non-Goals

- No automatic trust from Tailnet membership.
- No printer/scanner or Home Assistant action forwarding.
- No broad shell bridge.
- No hidden credential storage.
- No remote MCP tool grants in v0.1.

## Future Protocol Shape

Agent Link should align with A2A rather than invent a new public protocol.

- Agent identity maps to an A2A Agent Card.
- Chat and long-running work map to A2A messages/tasks.
- File/context handoff maps to A2A parts/artifacts.
- Tool grants map to explicit MCP server/tool scopes exposed by the remote agent only after approval.

## Security Defaults

- Profiles identify hosts but do not imply trust.
- Human pairing/approval remains required before a profile is treated as trusted.
- Tool access starts empty.
- Physical actions such as printing, scanning, smart-home actions, or file migration require later scoped grants and confirmations.
- Logs should avoid secrets and raw credentials.

## First TTBU Path

1. Agent loads the `agent-link` skill.
2. Agent lists known profiles.
3. Agent probes the selected profile.
4. Agent asks for a briefing.
5. Agent works with the user.
6. Agent sends a handoff summary back.

The target experience is seconds, not minutes.

