# Companion release TODO

Use [release preparation](../docs/RELEASE_PREPARATION.md) for the final pre-push
sequence. Repository names are selected; creation and publication follow acceptance.

First beta is best effort, with the public test claim limited to the declared
Ubuntu LTS baseline. The core's `docs/FIRST_BETA_RELEASE_PLAN.md` and this
repository's release preparation guide define the finite queue. Optional
disabled core features and other Linux distributions are post-beta work;
reports from SUSE/SLES, openSUSE and RHEL are welcome without a test claim.
The operator resumed release work after the earlier lab pause.

- [x] Let the named privacy check accept an external private-identifier file
  (2026-09-24). Preserve caller-relative paths, refuse internal pattern files,
  and test detection without printing private matches; 26 local tests pass.
- [x] Review the core's R1-R13 fixes within the first-beta scope. The only
  live-qualified repair claim is the supervised nonempty missing-replica file
  path on the recorded Ubuntu/Gluster lab; other recipes remain experimental.
  See the [core qualification boundary](../docs/CORE_QUALIFICATION.md).
- [x] Align operator guidance with the core's 2026-09-26 exact-version heal
  gates. The skill directs users to the current capability report and refuses
  unqualified full-heal/native-resolver writes; final core review remains open.
- [x] After final guidance edits, 45-file inventory, 51 links, 26 local
  scenario/contract tests, six skill validators, and current-tree/history privacy scans
  passed. Existing six-skill install/discovery/update/removal evidence from
  2026-09-24 still applies; skill, adapter and intended CLI behavior did not
  change in this checkpoint.
- [ ] Review public metadata and the final source snapshot under the current
  release authorization. The initial commit is recorded; no completed-review
  tag exists yet.
Future change details belong in commits. No original ledger is imported.
