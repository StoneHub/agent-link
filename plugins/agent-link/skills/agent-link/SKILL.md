---
name: agent-link
description: Deprecated compatibility workflow for an explicitly requested existing Agent Link SSH/OpenClaw profile. Read its retirement guide before using it. New shared workspace and agent integration work belongs to Threadspace clients/connectors and the Rooms backend.
---

# Agent Link — deprecated

Agent Link is retired as a separate product. Read
[retirement and migration](../../docs/retirement.md) before changing an integration.
This product is retired; repository archival is pending direct confirmation. Preserve private profile data and history; route any
later demonstrated integration need to the existing Threadspace backlog. Runtime
parity and host inventory are future work, not source-retirement gates.

## Existing consumer workflow

1. Confirm the user requested the legacy workflow and authorized the target and
   content. A profile or network reachability is routing information, not consent.
2. Inspect `python3 plugins/agent-link/scripts/agent_link.py --help` from the repo
   root, then `profile list` only when needed. Profile output contains host details;
   keep it private. Maintain profiles only within the requested scope.
3. Run `probe PROFILE` only when remote contact is authorized. Run `brief`, `ask`
   or `handoff` only when that agent interaction and disclosure are authorized.
   Handoff can change remote memory. Keep sensitive context out unless explicitly
   approved. The helper cannot enforce the remote runtime's tool policy.
4. Report the actual result. A failed or uncertain reply does not prove a message
   was unaccepted; reconcile with the runtime owner before repeating a write.

For new work, use the product/architecture links in the retirement guide. Rooms
owns durable shared records; Threadspace connectors own runtime adaptation. Keep
personal history, credentials and host policy under their existing owners.
