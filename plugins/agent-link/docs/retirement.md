# Retirement and migration

Tracking: [retirement issue #2](https://github.com/StoneHub/agent-link/issues/2).

Decision date: 2026-10-18. Agent Link is retired as a separate product in favor
of Threadspace, with Rooms as its backend. Monroe authorized merging this notice
and archiving the repository now, preserving all source/history. The active
repositories are `t3code` and `t3rooms`. Runtime parity and other-host inventory
are later product work, not retirement or archival prerequisites. Installations,
private profiles, credentials, remote hosts and runtimes remain untouched.

## Authoritative owners

- [Authoritative reconciliation and later work](https://github.com/benwilliams0540/t3code/blob/main/docs/operations/agent-link-retirement.md)
- [Threadspace product direction](https://github.com/benwilliams0540/t3code/blob/main/docs/product/threadspace.md)
- [Architecture and module owners](https://github.com/benwilliams0540/t3code/blob/main/docs/architecture/threadspace.md)
- [Rooms backend](https://github.com/benwilliams0540/t3rooms/blob/main/README.md)
- [Backend conversation contract](https://github.com/benwilliams0540/t3rooms/blob/main/docs/design/persistent-room-conversations.md)
- [Resident connector host](https://github.com/benwilliams0540/t3code/blob/main/packages/rooms-agent-connector-host/README.md)
- [Current Threadspace milestone and acceptance](https://github.com/benwilliams0540/t3code/issues/26)

Reviewed source baselines: Agent Link `28bad254bf7716cda9d741153ea74420680c7806`,
Threadspace `d224442a20ec75f983e2d696b784f6b2f1bb3a62`, Rooms
`235d376b879326aece915b560ddd91aff91119f7`. Links to `main` follow later changes.
The final retirement direction is integrated in Threadspace main at
`39d876a7fe9bba48a47701a2641655b2304f9422` (PR #50).
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
  issue records the completed source retirement; later demonstrated needs belong
  in the existing Threadspace backlog.

The helper, plugin name `agent-link`, marketplace source, command arguments,
stdout/exit behavior and profile schema/storage are preserved as historical
source, not an actively maintained compatibility product. Only CLI help/docstring
and discovery descriptions change. The original design and implementation remain
in Git and in this checkout for inspection and reuse. No source is imported into
Threadspace merely to keep the former project alive.

## Later consumer migration guidance

Retirement is complete independently of runtime parity. If an actual consumer
surfaces, its owner records the demonstrated need in the existing Threadspace
backlog: [#11 runtime acceptance](https://github.com/benwilliams0540/t3code/issues/11),
[#26 product milestone](https://github.com/benwilliams0540/t3code/issues/26), or
[#23 project context](https://github.com/benwilliams0540/t3code/issues/23).
The authoritative reconciliation above maps each former helper capability.

Keep existing profiles and personal history private and intact. No automatic
profile conversion, personal-memory import or CLI parity is provided. Any later
shared summary needs explicit destination and content authorization. Room
membership and SSH routing hints do not grant runtime tools or credentials.
Verify a proposed replacement on its intended runtime/clients when that product
work is undertaken, preserving scope, stable request IDs, idempotence, receipts
and honest uncertain-write behavior. Reconcile uncertain writes before retrying.
Those are future integration requirements, not gates on this archive.

## Final disposition

Source retirement is merged. Automatic approval review blocked repository
archival pending direct Monroe confirmation; the exact blocker and next action
are recorded in [issue #2](https://github.com/StoneHub/agent-link/issues/2#issuecomment-6247278009).
The repository remains unarchived until that action succeeds.

Merge PR #3 to `main`, close retirement issue #2 and archive this GitHub repository
under Monroe's explicit direction. Preserve its files and Git history. Fleet's
Windows controller reference was reconciled separately on Fleet main at
[`82a9bbb`](https://github.com/StoneHub/fleet/commit/82a9bbb). It directs new shared
work to Threadspace and does not block this retirement. Other-host inventory is needed only
before later removal or claims about installed usage, not before source archival.

No plugins are uninstalled, profiles removed, hosts changed or runtime parity
claimed. Threadspace/Rooms owners own future accepted needs in their existing
repositories; Agent Link has no continuing active development lane.

The canonical local checkout is retained at
`/Users/monroe/Developer/GitRepos/agent-link` as the preserved archival checkout,
owned by Monroe. It is not a disposable review clone; any future removal requires
a separate decision. Remove the merged task branch after integration. No services
or build outputs were created by this change.
