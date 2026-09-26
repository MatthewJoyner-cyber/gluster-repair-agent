---
name: gluster-operator
description: Guide evidence-based Gluster repair previews, operator decisions, execution review, and verification using the core CLI.
---

# gluster-operator

Identify the user's target and current core version/review status. Check
current topology, brick roles, heal settings, and affected object identity.
Inspect the core CLI help rather than inventing wrapper flags.
Check the installed core's capability report and current compatibility profile
before suggesting a heal or native split-brain command. At the 2026-09-26 core
checkpoint, only pending-index heal on Gluster 11.1 has scoped live command
qualification. Full namespace heal and native per-file resolver writes are
blocked by the core pending separate live proof. Do not bypass a blocked
command through a raw Gluster invocation or development canary.

Before suggesting any live repair, read the core's current TODO/review status
and [core qualification boundary](../../docs/CORE_QUALIFICATION.md). Until its
scoped review is completed and tagged, explain that local tests or this
companion do not qualify the engine or authorize a live write.

Collect bounded evidence, build a core plan, and explain targets, preservation,
and verification before seeking any required write authority. Never treat an
old plan, setup state, or a classification label as sufficient authorization.

An arbiter never supplies payload. Preserve unresolved copies and refer
ambiguity back to evidence and planning. A resolver timeout or lost connection
may follow a write: verify the exact outcome before another attempt.
Do not implement repairs outside the core or bypass an unresolved core defect.

On backup/restore verification failure, retain the archive and partially
restored state. A successful transfer does not establish metadata fidelity;
fake-super capture and privileged restore may need a compatible read-back
comparison. Inspect the core's backup contract and independent metadata before
retrying. Never turn a `--dry-run` missing-child check into actual deletion.

After an authorized run, verify targeted effects, restore agreed temporary
settings, and record actual writes, unknown outcomes, and next evidence.

For local operations, consult the relevant entry under
`$GLUSTER_REPAIR_PRIVATE_ROOT/steering/`, defaulting to
`$HOME/.gluster-repair-private/steering/`. Missing private files are normal
for source review and synthetic tests. Keep inventory, personal preferences,
raw evidence, and incident history in the external private ledger. Do not copy
them into public comments, commits, issues, or examples. Private notes are
context, not fresh execution authority.

Use an installed bounded helper when it covers the task. Do not widen access
or replace a denied helper with unrestricted SSH, sudo, or an interpreter.
