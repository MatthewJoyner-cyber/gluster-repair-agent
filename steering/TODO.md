# Companion release TODO

Use [release preparation](../docs/RELEASE_PREPARATION.md) for the final pre-push
sequence. Repository names are selected; creation and publication follow acceptance.

- [x] Let the named privacy check accept an external private-identifier file
  (2026-09-24). Preserve caller-relative paths, refuse internal pattern files,
  and test detection without printing private matches; 26 local tests pass.
- [ ] Resolve the core safety review before qualifying repair-capable guidance.
  Track the required live/privileged and clean-host work in the core's current
  TODO and [core qualification boundary](../docs/CORE_QUALIFICATION.md).
- [x] Align operator guidance with the core's 2026-09-26 exact-version heal
  gates. The skill directs users to the current capability report and refuses
  unqualified full-heal/native-resolver writes; final core review remains open.
- [ ] After final fixes, rerun the inventory/privacy checks and scenario suite;
  repeat plugin lifecycle qualification if package behavior or target CLI changes.
  The six-skill install/discovery/update/removal test passed on 2026-09-24.
- [ ] Review public metadata and the final source snapshot under the current
  release authorization. The initial commit is recorded; no completed-review
  tag exists yet.
Future change details belong in commits. No original ledger is imported.
