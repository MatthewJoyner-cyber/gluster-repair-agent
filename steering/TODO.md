# Companion release TODO

Use [release preparation](../docs/RELEASE_PREPARATION.md) for the publication
sequence. Verify both repository destinations and selected release revisions.

First beta is best effort, with the public test claim limited to the declared
Ubuntu LTS baseline. The core's `docs/FIRST_BETA_RELEASE_PLAN.md` and this
repository's release preparation guide define the finite queue. Optional
disabled core features and other Linux distributions are post-beta work;
reports from SUSE/SLES, openSUSE and RHEL are welcome without a test claim.
The operator resumed release work after the earlier lab pause.

- [x] Publish the matching signed `v0.1.0-beta.3` companion prerelease with
  the clean core on 2026-09-27. Public API checks confirmed prerelease status
  and notes; the unauthenticated archive matched all 47 tagged files byte for
  byte. See [validation](../docs/VALIDATION.md).

- [x] Let the named privacy check accept an external private-identifier file
  (2026-09-24). Preserve caller-relative paths, refuse internal pattern files,
  and test detection without printing private matches; 26 local tests pass.
- [x] Review the core's R1-R13 fixes within the first-beta scope. The only
  live-qualified repair claim is the supervised nonempty missing-replica file
  path on the recorded Ubuntu/Gluster lab; other recipes remain experimental.
  See the [core qualification boundary](../docs/CORE_QUALIFICATION.md).
- [x] Align operator guidance with the core's 2026-09-26 exact-version heal
  gates. The skill directs users to the current capability report and refuses
  unqualified full-heal/native-resolver writes; later changes require a fresh
  scope review.
- [x] After final guidance edits, 45-file inventory, 51 links, 26 local
  scenario/contract tests, six skill validators, and current-tree/history privacy scans
  passed. Existing six-skill install/discovery/update/removal evidence from
  2026-09-24 still applies; skill, adapter and intended CLI behavior did not
  change in this checkpoint.
- [x] Review public metadata and the final local source snapshot under the
  current release authorization. Signed local review markers now record the
  bounded scope. Publication and public download checks remain in the core's
  first-beta plan.
- [x] Validate the new major-version qualification skill and its package
  inventory, then repeat plugin discovery/lifecycle checks on the final
  companion candidate. Its process must retain the core's exact-version gates
  and use only the focused compatibility evidence requested for a release.
  Completed 2026-09-27: seven validators, 26 local tests, 46-file inventory,
  privacy audit, exact installed hashes, fresh-session skill read/answer,
  install and removal passed on CLI 0.155.1. The prior cachebuster update
  proof remains applicable because the CLI/adapter did not change; local
  marketplace `upgrade` is Git-only. See [validation](../docs/VALIDATION.md).

Future change details belong in commits. No original ledger is imported.
