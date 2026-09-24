---
name: gluster-canary
description: Design or review disposable Gluster canaries and classify their repair evidence.
---

# gluster-canary

Use only an explicitly selected disposable volume with current topology,
daemon/brick readiness, baseline settings, and bounded cleanup. A familiar
volume name is not a safety fence. Keep arbiters out of payload-source roles.

Separate fixture construction from independent discovery. Canary state can
prove harness behavior; repair acceptance requires real operator evidence
through the core pipeline and focused post-execution verification.

Classify unit/synthetic, harness-only, diagnostic, native-heal-first,
operator-path-mechanical, and independent repair evidence explicitly.
A direct xattr/index tie is not automatically a durable protocol split-brain.
A cleanup result or zero heal count does not by itself prove repair value.

Consult the core's `docs/CANARY_CASES.md` for sanitized case references and
qualification scope. Keep public report, hypothesis and locally reproduced
result distinct. Record exact runs and evidence paths in the private ledger;
cite public sources without copying reporters' infrastructure or raw logs.

Before fixture construction, create and write-probe operator-owned state/work
roots. Create mount parents without sudo so state recording cannot fail after
fault construction due to root-owned ancestors. Inspect any partially completed
fixture before retrying; never recursively chown a mounted volume to fix the
controller workspace. If native healing leaves a ready preview with zero
actions, record native-heal-first/smoke, not successful repair execution.

For reusable VM playgrounds, fresh guest qualification and retained failure
fixtures, use [gluster-vm-lab](../gluster-vm-lab/SKILL.md).

Do not alter shared networking or services to force a fixture. Stop when
isolation cannot be demonstrated; record the missing capability without
claiming impossibility. Restore agreed settings and preserve unknown outcomes.

For local operations, consult the relevant entry under
`$GLUSTER_REPAIR_PRIVATE_ROOT/steering/`, defaulting to
`$HOME/.gluster-repair-private/steering/`. Missing private files are normal
for source review and synthetic tests. Keep inventory, personal preferences,
raw evidence, and incident history in the external private ledger. Do not copy
them into public comments, commits, issues, or examples. Private notes are
context, not fresh execution authority.

Use an installed bounded helper when it covers the task. Do not widen access
or replace a denied helper with unrestricted SSH, sudo, or an interpreter.
