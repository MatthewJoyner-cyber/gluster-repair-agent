# Core qualification boundary

The companion does not qualify the separately installed Gluster Repair Tool.
It can explain the tool, help collect bounded evidence, prepare previews and
support drafts, and guide an operator through authorized workflows. It must
not describe the core as release-qualified for live repairs until the core's
own review is completed and tagged.

Scoped qualification completed on 2026-09-24 using three fresh Ubuntu 24.04
guests, Python 3.12.3 and Gluster 11.1:

- installation ownership, real sudoers checks, restricted service login, all
  six directed peer SSH connections and account/key preservation on reinstall;
- remote backup recovery and a fresh verified round trip with trusted/user
  xattrs, numeric ownership, access/default ACLs, timestamps, symlinks and
  cross-artifact hardlinks; and
- three replica-3 canary builders followed by native healing to zero pending
  entries and ready repair previews with no proposed writes.

These results establish the stated installation, backup and native-heal scope.
They do not establish repair-apply acceptance.

The 2026-09-26 core compatibility profile admits pending-index heal only for
the tested Gluster 11.1 release. Shared heal dispatch enforces that profile;
full namespace heal and native per-file split-brain resolver writes are blocked
until their exact command and response behavior is live-qualified. Other
Gluster releases need separate version and output evidence. Check the current
core capability report and compatibility guide before operator instructions.

The core still requires:

- disposable live qualification of saved execution-origin binding, including
  same-name volume recreation and live object changes;
- stable repairable fixtures and remaining reboot/failure coverage;
- intended operator collection coverage for diagnostic metadata schemas; and
- broader interpreter/distribution and clean-host failure coverage, with
  supported combinations limited to those actually tested.

Until then, the companion must state that local tests and synthetic evidence do
not authorize a live repair. It may direct the user to the core's current TODO,
review tag, validation record, installed help, and fresh evidence. A later
completed-review tag establishes only the reviewed scope recorded by that tag;
it does not replace operator authority, backups, or current evidence.
