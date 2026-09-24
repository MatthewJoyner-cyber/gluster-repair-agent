# Reusable development playground

Use retained guests for troubleshooting, reproducing reports with synthetic
data, trying a repair change, running canaries, or developing inside a guest.
The guest boundary supports testing; it is not proof that arbitrary code is
safely isolated. Verify the storage/network boundary described in
[provisioning](provisioning.md), keep production credentials out, and give
developers only the guest/host authority actually needed and approved.

## Choose a working mode

- **Host edit, guest test:** maintain the source checkout on the development
  host, run focused offline tests there, then copy the selected snapshot to an
  ordinary guest user's separate checkout and verify hashes. Keep host source
  storage separate from brick disks; avoid writable mounts of personal folders.
- **Guest development:** clone or copy approved source into the ordinary guest
  user's checkout and edit/test there. Keep source under version control and
  export uncommitted diffs plus untracked intended source before rolling back
  or replacing a disk. A snapshot is not a substitute for source backup.
- **Release qualification:** use the reviewed exact file inventory, fresh
  operator state and the relevant clean baseline. Follow
  [qualification](qualification.md); exploratory success alone is not release
  acceptance.

Use the supported service account/install layout. For deployed behavior, run
the shipped bootstrap from the development checkout and verify installed hashes
and help outside that checkout. For source-only tests, state that scope. Avoid
mixing a new controller with stale remote helpers. Temporary instrumentation is
development code; record it and remove or review it before release validation.

## Repeatable edit/test loop

1. Resume the retained lab by manifest identity and inspect its current health,
   settings and unresolved runs. An empty heal list does not erase prior errors.
2. Select one bug or experiment and a synthetic fixture on an explicitly chosen
   lab volume. Save a healthy baseline or a known failed reproduction as needed;
   do not overwrite the only copy of either.
3. Record source revision plus dirty diff/untracked source, dependency versions,
   and exact deployed-file hashes. Choose focused tests for the behavior changed;
   run broader checks when shared behavior or a failure justifies them.
4. Deploy the bounded change, run the scenario and independently inspect the
   result. Retain errors, partial writes and archives before attempting recovery.
   Keep original failure and corrected run distinct.
5. Export source changes and useful evidence. Leave the lab running only when
   requested for ongoing work, otherwise follow the agreed retention/shutdown
   plan. Never auto-delete a playground because tests passed.

Coordinate developers sharing a lab: reserve the chosen volume/fixture and
serialize fault injection, healing changes and reboot tests. One person's
baseline must not silently become another person's experiment. Separate cloned
labs when independent destructive experiments are needed; give clones new
network/machine/SSH identities and their own disk overlays.

Keep the reservation in the agreed private lab run record with operator, scope,
start time and status. Check with the current operator before taking over an
active or stale reservation; elapsed time alone does not free a running test.
Use the shipped bootstrap for deployed changes unless the core documents a
supported incremental update path; check installed hashes either way.

## Checkpoints and resetting

Distinguish clean OS, prerequisites installed, tool installed, healthy cluster
and failed fixture checkpoints. A tool-installed checkpoint cannot establish
fresh bootstrap. Record exactly which state the next test requires.

For a consistent cluster checkpoint, quiesce writes, stop test clients and
shut down all relevant guests before capturing their disks/state, or use a
documented coordinated snapshot procedure. Independent disk snapshots of a
running replica set are not automatically a consistent baseline. Include OS
and brick disks, protect seed/key material, and record backing dependencies.

Before rollback or reset, preserve developer source, uncommitted work and
failure evidence and confirm the intended checkpoint. Do not revert just one
peer into an older cluster state as routine cleanup. That can itself be a
recovery experiment and needs explicit scope and current evidence.

A retained playground needs no from-scratch rebuild merely because it is old.
Rebuild or branch from a clean checkpoint when testing first installation,
changing a platform baseline, investigating contamination, or otherwise needing
state the retained guests cannot prove. Publish only sanitized conclusions and
reproducible synthetic fixtures; private images and raw lab ledgers stay local.
