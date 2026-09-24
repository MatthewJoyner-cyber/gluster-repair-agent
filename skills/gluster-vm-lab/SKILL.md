---
name: gluster-vm-lab
description: Create or reuse Gluster VM playgrounds and development environments, or qualify repair-tool installation, privileged metadata and canary behavior on fresh guests.
---

# gluster-vm-lab

Use this skill for a developer/tester playground, a reusable development
environment, or fresh-system qualification. Match the workflow to the claim:
ordinary edit/test cycles can reuse guests; fresh-install proof needs a clean
baseline. Do not rebuild or run the whole qualification matrix for each edit.

An extra account on
an already configured server proves only fresh-user behavior. Containers can
exercise some code paths but do not replace a fresh guest's boot, service,
sudoers, SSH and filesystem checks. Three guests on one host simulate peers;
they do not provide three independent physical failure domains.

Read the relevant reference for the current stage:

- [Provisioning and lifecycle](references/provisioning.md): image, storage,
  resources, identities, network separation, resuming and retaining a lab.
- [Qualification method](references/qualification.md): downloaded-source
  simulation, first access, real bootstrap, backup, canaries and reboot tests.
- [Development playground](references/development.md): repeatable edit/deploy/test
  loops, checkpoints, experiments and promoting a result into release evidence.

## Before acting

Identify the requested outcome and existing authority. Read only the relevant
external private lab record under `$GLUSTER_REPAIR_PRIVATE_ROOT`, defaulting
to `$HOME/.gluster-repair-private`; consult its steering index for local helpers
and its ledger for lab state. Establish the exact lab resources, ownership,
storage backing and current state before changing them. Missing private records
do not block explaining a plan, but do not guess an existing lab's identity.

Use an installed bounded VM helper when its contract covers the operation.
This skill supplies procedures, not a hypervisor wrapper or permission grant.
If no local helper exists, prepare reviewable commands for the installed
hypervisor using the agreed manifest and its current documentation; do not
invent a bundled helper or treat its absence as a reason to block planning.
Do not bypass a denied helper with unrestricted SSH, sudo or an interpreter.
Prepare a concrete plan before asking for any missing provisioning authority;
do not ask again for operations already authorized within that plan.

Separate guest administrator privileges from the repair service's actual
shipped policy. Full guest test-administrator sudo is appropriate only when
authorized for those guests. It never grants host access or justifies widening
the service policy to make a test pass.

## Evidence and continuation

Keep a private stage record: intended check, source/image hashes and versions,
manifest identities, command exit/completion, independent assertions, result
paths, partial writes, next action and lifecycle instruction. Store secrets
separately; never put keys, seeds, raw topology or personal paths in public
source or reports. Public conclusions use synthetic aliases and scoped results.

Advance only when the stage's independent checks pass. A zero exit code,
disappeared process or deleted temporary directory is not acceptance. On an
unknown or partial result, preserve evidence and inspect current state before
retrying; do not reset or recreate fixtures over the failed state.

Respect the latest lifecycle instruction. If asked to retain the lab, export
nonsecret evidence, shut down gracefully, verify every guest is off and keep
disks, definitions and protected credentials. Do not turn an earlier cleanup
plan into authority to destroy a retained lab. Resume by verifying identities
and dependencies, not by rerunning creation. Rebuild from a clean baseline only
when the next claim requires freshness or the existing state cannot prove it.
