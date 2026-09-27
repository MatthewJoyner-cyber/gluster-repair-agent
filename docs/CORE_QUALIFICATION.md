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
One 2026-09-27 full-heal command smoke succeeded on a quiet 11.1 lab volume;
it did not test a pending repair effect and did not open the core gate.

Later scoped Ubuntu checks also passed installed refusal for same-name volume
recreation and same-size/mtime changed data, one empty-file mechanical restore,
post-repair sequential reboots, installer failure cases, and metadata-only
workflow/AFR/arbiter/offline-status projection. These are bounded results, not
qualification of every repair recipe. The core validation record owns details.

On 2026-09-27 a current-candidate nonempty missing-replica workflow exposed a
staging ownership defect on its first execution. The core fixed that defect,
then used a fresh fixture and one new apply run to preserve digest, GFID,
UID/GID, mode and a user xattr across all three replicas. The failed fixture
was corrected and the lab returned to a quiet, powered-off state. This is one
scoped mechanical repair proof, not qualification of every recipe. The core's
local scope review and source checks passed; its completed-review tag and
publication checks remain before any public release claim. Its
`docs/FIRST_BETA_RELEASE_PLAN.md` defines acceptance.
Full-heal/resolver writes stay disabled; their extra qualification and wider
platform/schema coverage are follow-up work, not first-beta blockers.
The public test claim is Ubuntu LTS. Other Linux distributions are untested,
including SUSE/SLES, openSUSE and RHEL; a supported OS does not by itself prove
that its Gluster package or this tool is supported on that combination.

Until then, the companion must state that local tests and synthetic evidence do
not authorize a live repair. It may direct the user to the core's current TODO,
review tag, validation record, installed help, and fresh evidence. A later
completed-review tag establishes only the reviewed scope recorded by that tag;
it does not replace operator authority, backups, or current evidence.
