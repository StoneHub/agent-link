# Agent Link — retired (archived)

**Retired as a separate product on 2026-10-18; this repository is archived.** Threadspace owns the shared
workspace; Rooms is its backend. New integration work belongs in those existing
owners. This repository preserves the legacy SSH/OpenClaw helper and history as a read-only reference.
Deprecation does not mean a working drop-in replacement exists.

- [Threadspace product direction](https://github.com/benwilliams0540/t3code/blob/main/docs/product/threadspace.md)
- [Architecture and module ownership](https://github.com/benwilliams0540/t3code/blob/main/docs/architecture/threadspace.md)
- [Rooms backend](https://github.com/benwilliams0540/t3rooms/blob/main/README.md)
- [Migration, consumer evidence and archival gates](plugins/agent-link/docs/retirement.md)

## Responsibility and migration

Rooms owns membership, authorization, durable shared history, conversation
bindings, ordered turns and atomic results. Threadspace owns clients and shared
client state. Its agent connectors own runtime adaptation, delivery, acceptance
receipts and reconciliation; the host runtime owns actual sessions and execution.
The Python helper here is a local SSH/OpenClaw scaffold, not an application backend.

Existing installations and private profiles remain untouched. Any consumer that
surfaces later should bring its actual need to the existing Threadspace backlog. Keep private agent history private unless an explicit,
scoped handoff authorizes sharing. No automatic profile conversion, history
import, credential transfer or host reconfiguration is provided. Follow the
[migration instructions](plugins/agent-link/docs/retirement.md) before switching.

## Legacy compatibility usage

The historical plugin ID, helper path, commands and profile format are preserved
in this archive. There is no active standalone roadmap or compatibility service.
Use these only for an explicitly requested existing Agent Link workflow; new
users should start with Threadspace's product and architecture documents above.

```sh
python3 plugins/agent-link/scripts/agent_link.py --help
python3 plugins/agent-link/scripts/agent_link.py profile list
```

For an existing approved profile:

```sh
python3 plugins/agent-link/scripts/agent_link.py probe PROFILE
python3 plugins/agent-link/scripts/agent_link.py brief PROFILE
python3 plugins/agent-link/scripts/agent_link.py ask PROFILE "Approved question"
python3 plugins/agent-link/scripts/agent_link.py handoff PROFILE --summary "Approved summary"
```

`probe` contacts the remote host. `brief`, `ask` and `handoff` invoke the remote
agent and can disclose context or affect its memory. A stored profile supplies
routing, not permission to contact an agent or use its tools. The helper has no
scoped tool-grant enforcement and cannot constrain what the remote runtime does.
Use only within the user's authorized scope and host policy.

`profile add` remains available for maintaining an existing integration; inspect
`profile add --help` for fields. It adds or replaces a named profile. Profiles
remain in `~/.agent-link/profiles.json`, or the directory set by `AGENT_LINK_HOME`.
No profiles are deleted or rewritten by this deprecation.

## Preserved work

The [original design](plugins/agent-link/docs/design.md) is historical context,
not an active roadmap. Useful ideas include private-network routing, profiles as
routing hints rather than grants, concise briefings and explicit handoffs. Any
reuse should fit the existing Threadspace connector/runtime boundary and prove
its consumed behavior before replacing a consumer.
