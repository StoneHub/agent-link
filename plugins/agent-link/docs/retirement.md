# Retirement and migration

Tracking: [retirement issue #2](https://github.com/StoneHub/agent-link/issues/2).

Decision date: 2026-10-18. Agent Link is deprecated as a separate product in favor
of Threadspace, with Rooms as its backend. Source deprecation preserves the
legacy helper and plugin identity; it does not archive this repository or change
an installed plugin, profile, remote host or runtime.

## Authoritative owners

- [Threadspace product direction](https://github.com/benwilliams0540/t3code/blob/main/docs/product/threadspace.md)
- [Architecture and module owners](https://github.com/benwilliams0540/t3code/blob/main/docs/architecture/threadspace.md)
- [Rooms backend](https://github.com/benwilliams0540/t3rooms/blob/main/README.md)
- [Backend conversation contract](https://github.com/benwilliams0540/t3rooms/blob/main/docs/design/persistent-room-conversations.md)
- [Resident connector host](https://github.com/benwilliams0540/t3code/blob/main/packages/rooms-agent-connector-host/README.md)
- [Current Threadspace milestone and acceptance](https://github.com/benwilliams0540/t3code/issues/26)

Reviewed source baselines: Agent Link `28bad254bf7716cda9d741153ea74420680c7806`,
Threadspace `d224442a20ec75f983e2d696b784f6b2f1bb3a62`, Rooms
`235d376b879326aece915b560ddd91aff91119f7`. Links to `main` follow later changes.
Source documentation and protocol behavior do not establish a working replacement
on a particular host or installed client.

| Legacy concern | Destination for new work | Migration limit |
| --- | --- | --- |
| Local routing/profile configuration and probing | Threadspace connector host configuration and transport setup | No converter from Agent Link profiles; verify actual supported runtime and host |
| Brief, ask and handoff messages | Explicit authorized Threadspace conversation through its agent connector | No command-for-command replacement or automatic private memory import established |
| Shared membership, history, bindings and ordered work | Rooms backend | Preserve authorization, attribution, request identity, idempotence and atomic results |
| Runtime sessions, execution and tools | Threadspace connector adaptation and actual host runtime | Keep host tool/approval policy; do not move execution into Rails |
| UI, connection/feed/conversation state | Threadspace clients and shared client modules | Verify consumed contracts on the intended clients |

## Consumer evidence

- The preceding allowed-checkout review reported only Fleet's
  `docs/runbooks/windows-controller.md` referencing Agent Link, with no application
  dependency found. That exact runbook reference was rechecked during this change.
  This is a documentation consumer, not evidence of a running installation.
- This Mac has no default `~/.agent-link` directory at review time. The preceding
  review reported no installed Agent Link Codex plugin. Neither establishes absence
  of custom `AGENT_LINK_HOME` stores, Windows installations or other-host consumers.
- Other hosts and unindexed repositories remain unverified. No credentials,
  profile contents or remote agents were inspected or contacted for this retirement.
- No existing issue or open PR covered retirement when checked. The retirement
  issue tracks remaining consumer reconciliation and final archival criteria.

The helper, plugin name `agent-link`, marketplace source, command arguments,
stdout/exit behavior and profile schema/storage remain available because the
external runbook and unverified other-host usage lack a completed migration.
Only CLI help/docstring and discovery descriptions change. The original design
and implementation remain in Git and in this checkout for inspection and reuse.

## Existing consumer migration instructions

1. The consumer owner inventories their explicitly authorized machines: entry
   points, installed plugin version, profile store location (including custom
   `AGENT_LINK_HOME`), scheduled callers and which commands are actually used.
   Record metadata and owner in the retirement issue; keep private contents local.
2. Choose the relevant existing Threadspace owner above. Verify its real supported
   host/runtime capabilities and configuration. If no suitable implementation
   exists, keep the legacy workflow and track the specific gap with that owner.
3. Prepare an explicit migration for that consumer. Keep profiles and private
   history intact; separately authorize any shared context handoff. A room
   membership or SSH profile is not a tool grant or credential migration.
4. Verify with the intended runtime and authorized client identities: distinct
   conversations, continued sessions, scoped membership, retained history, stable
   request IDs, safe retry/reconnect and visible uncertain acceptance/cancellation.
   Reconcile uncertain writes before retrying. Source fixtures alone are insufficient.
5. Switch that consumer only after acceptance. Its owner updates callers/docs and
   records exact revisions, observed behavior and rollback path in the issue.
   Retain the old helper/profile until that consumer confirms it can stop using it.

## Remaining before final archival

The retirement issue owner coordinates consumer owners; Threadspace/Rooms owners
implement any accepted gaps in their own repositories. Fleet's documentation owner
reconciles the Windows runbook separately. This task does not edit those repos.

Archive only after known references and authorized host inventories are resolved,
remaining consumers have verified migration or an explicit retained legacy owner,
and useful work/history has an accessible home. Removing plugins/profiles,
changing hosts and archiving the GitHub repository each require separate authority.
No such action is part of source deprecation.

The canonical local checkout is retained at
`/Users/monroe/Developer/GitRepos/agent-link` for ongoing review and compatibility
work, owned by the Agent Link retirement task. It is not a disposable review clone;
any future removal requires a separate decision. No services or build outputs are
created by this change.
