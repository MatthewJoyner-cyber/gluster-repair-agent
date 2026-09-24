---
name: gluster-maintainer
description: Maintain or review Gluster Repair Tool source, tests, documentation, and release candidates.
---

# gluster-maintainer

Read the core's current TODO, open review, and relevant safety invariants.
Check the newest completed-review tag before reviewing recent commits; if none
exists, state a baseline. Keep changes within the user's request.

Preserve the manager/worker architecture and evidence-to-plan boundary.
Add meaningful regressions for safety defects and test the changed interfaces.
Run the full suite for shared behavior. Synthetic tests are not live acceptance.

For experiments or deployed-host regressions, use the reusable
[VM playground workflow](../gluster-vm-lab/SKILL.md). Reuse guests for ordinary
development; fresh-install claims require an appropriate clean baseline.
Retain actual completion/exit status, test logs and exact source hashes outside
the repository. A disappearing process or temporary tree is not a passed test.
State skipped checks and filesystem limitations; do not merge offline,
installed-tree, privileged fidelity and repair-apply evidence into one claim.

Record future implementation detail in commits: problem, behavior, rationale,
validation, caveats. HISTORY.md is frozen prehistory, not a running ledger.
Update current docs and TODO with the code; tag a review only after its fixes
are implemented and validated. Commit and publish only when authorized.

For local operations, consult the relevant entry under
`$GLUSTER_REPAIR_PRIVATE_ROOT/steering/`, defaulting to
`$HOME/.gluster-repair-private/steering/`. Missing private files are normal
for source review and synthetic tests. Keep inventory, personal preferences,
raw evidence, and incident history in the external private ledger. Do not copy
them into public comments, commits, issues, or examples. Private notes are
context, not fresh execution authority.

Use an installed bounded helper when it covers the task. Do not widen access
or replace a denied helper with unrestricted SSH, sudo, or an interpreter.
