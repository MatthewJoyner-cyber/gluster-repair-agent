---
name: gluster-version-qualification
description: Review a new Gluster major release for Gluster Repair Tool compatibility using focused interface checks and bounded lab evidence. Use for a new major-version claim, not routine canary development or ordinary support triage.
---

# Gluster version qualification

Start with the installed core revision, its completed-review marker,
`docs/GLUSTER_COMPATIBILITY.md`, and
`docs/MAJOR_VERSION_QUALIFICATION.md`. Confirm the exact Gluster package and OS
combination being considered. Check current official release and upgrade notes
for changes to interfaces the tool actually uses; distinguish an upstream
native-heal fix from a changed tool contract.

Define the proposed claim before testing: read-only diagnosis, a named repair
recipe, or a specific native Gluster command. Check version and feature gates,
volume type and brick layout, heal/status output, worker metadata, privilege
and installation paths. Use focused offline fixtures for changed output. Do
not assume that a major number or a passing parser implies safe writes.

On a disposable lab, use the existing
[VM qualification workflow](../gluster-vm-lab/SKILL.md) for source hashes,
install state, evidence and cleanup. Run one healthy-volume read-only smoke.
For a repair-write claim, give normal native healing its chance on an existing
representative case. If it clears, record that result and the tool's zero-action
preview. A separate controlled mechanical check may hold healing off on a
disposable volume while reusing an existing fault builder. Label that result
operator-seeded; require fresh independent evidence, a reviewed preview and
backup, one apply, brick verification and restored healing. Add another
topology only when it is part of the claim or addresses a concrete interface
concern. Keep unqualified feature
gates closed; a failed or ambiguous assertion narrows the claim.

Report exact versions, topology, tool commit, evidence class, passed and
skipped checks, cleanup state, and remaining limits. Store raw hostnames,
addresses, paths and logs only in the operator's private ledger. Update public
compatibility and validation notes with sanitized conclusions; change the
core's exact-version profile only after the relevant feature has live proof.
Never promote a broad major-version claim from one minor release or one lab.
