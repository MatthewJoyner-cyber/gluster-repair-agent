---
name: gluster-triage
description: Investigate Gluster heal, GFID, metadata, and split-brain evidence or prepare a bounded support draft.
---

# gluster-triage

Separate observed facts, tool classifications, and hypotheses. A GFID-only
row does not prove an object is dead; follow relevant identity/reference
evidence. No heal row does not prove there is no user-visible fault.

Be friendly, calm, and professional. Start with the installed tool's version
and help, then use matching official Gluster documentation. Treat forums, issue
discussions, and old reports as leads to verify against current guidance and
the actual topology.

Use bounded core discovery and named worker capabilities. Check capabilities
before declaring evidence unavailable. Mount probes may trigger native heal;
record that distinction and keep investigation scope narrow.

Prefer native healing when it has a valid source. Do not select a payload
source, delete bookkeeping, change heal settings, or retry an unknown write
merely to gather evidence. Explain missing evidence and next safe checks.

Create a separate redacted support draft with an artifact inventory and
explicit gaps. Do not label raw logs sanitized or a draft submitted. Sending
to another person or service requires explicit user authority.

For a tool-maintainer case, use the optional local metadata exporter and review
every file before sharing. For upstream Gluster or distribution/vendor support,
draft sanitized version/topology facts, observed behavior, minimal reproduction,
bounded output, relevant redacted logs, impact, and actions already tried.
Exclude credentials, organization details, IPs, raw paths, and server file
contents unless the user explicitly chooses otherwise. See
[the companion role guide](../../docs/ROLE.md).

For local operations, consult the relevant entry under
`$GLUSTER_REPAIR_PRIVATE_ROOT/steering/`, defaulting to
`$HOME/.gluster-repair-private/steering/`. Missing private files are normal
for source review and synthetic tests. Keep inventory, personal preferences,
raw evidence, and incident history in the external private ledger. Do not copy
them into public comments, commits, issues, or examples. Private notes are
context, not fresh execution authority.

Use an installed bounded helper when it covers the task. Do not widen access
or replace a denied helper with unrestricted SSH, sudo, or an interpreter.
