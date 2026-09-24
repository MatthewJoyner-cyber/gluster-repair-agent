# Qualification method

Use the installed core's actual help, bootstrap contract and release TODO.
Keep each stage's result distinct; passing installation is not repair acceptance.
Record unsupported or untested cases rather than silently passing them.

## Fresh installation from user source

1. Prove the repair account, group, home, install tree and sudoers drop-in are
   absent in each fresh guest. Capture OS, Python, Gluster and prerequisite
   versions. Keep a restorable pre-install baseline for tests that require it.
2. Model a download: copy only the reviewed public file inventory into an
   ordinary guest administrator's checkout. Exclude `.git`, caches, keys,
   personal settings and runtime artifacts; verify per-file hashes after copy.
   SCP is a source-transfer simulation, not proof of a public GitHub download.
3. Separate initial access from bootstrap. Exercise missing private/public
   keys, locked keys without an agent, unknown/changed host keys, failed login,
   missing sudo and insufficient installer privileges on disposable targets.
   Manual console/password steps remain manual coverage when not performed.
4. Run preflight and real installation separately. `sudo -n true` succeeding
   does not prove permission for the installer's actual command. Do not stream
   multiple commands into a shell whose child SSH can consume the same stdin;
   use distinct invocations or a reviewed script file. Verify effects even
   when the command exits zero.
5. Check the real account, group, home/shell, SSH/key modes, root-owned installed
   code, real `visudo` validation and all shipped entry-point help/import checks
   outside the checkout. Test service login, required helper access, denial of
   unrelated direct sudo commands and inability to edit installed code. These
   denials do not prove every allowed helper argument is safe.
6. Test service-key login with pinned host keys in all six directed peer pairs.
   Then exercise actual tool-generated transfers; login alone is not transfer
   or metadata proof. Reinstall and compare account records and key bytes,
   authorized-key uniqueness and installed-file hashes.

Inject transfer, validation and sudoers failures only in the disposable test
scope. Record partial side effects and whether working access survived.
Installation is not transactional: remote staging cleanup can coexist with a
new controller key. Preserve that distinction in the result and before retries.

## Privileged backup fidelity

Use disposable fixtures containing numeric ownership, mode, nanosecond mtime,
access/default ACLs, user/trusted xattrs, symlinks and hardlinks spanning artifact
roots. Test through the unprivileged operator, real service SSH and deployed
privileged helpers, not merely a local root copy. Compare content and metadata
independently before/after capture, verified cleanup and restore. Fixture
contents are permitted test data; never export real server file contents in a
support bundle.

Retain independent fixture assertions: content digest, numeric UID/GID, mode,
mtime precision, ACL entries, xattr names/values, symlink target and shared inode
identity for expected hardlinks. Use trusted guest-side inspection tools such
as `stat`, `getfacl` and `getfattr`, rather than relying only on the repair
tool's own success report. State unsupported metadata explicitly.

On partial restore or verification failure, keep the archive and destination
state. Inspect the exact discrepancy before any recapture, cleanup or retry.
Fake-super capture and privileged destination representations can differ;
comparison must use a compatible read-back representation. A transfer exit
alone is not fidelity proof. The core's missing-child check uses `--delete`
only together with `--dry-run`; never turn that verification into deletion.

After a fix, verify recovery from the retained archive as well as a new complete
round trip. Preserve original failure and rerun evidence separately. The wider
platform and original repair-step backup scope require their own qualification.

## Canary and repair proof

Before constructing a fixture, create and actually write-probe the ordinary
operator's state/work roots. Create mount parents as that user before using
privilege for the mount leaf. Avoid root-owned ancestors that prevent saving
state after a fault is already built. On such a failure, inspect live state and
retain logs; repair only verified controller paths, never recursively chown a
mounted tree. Use a new fixture ID and newly absent state root when testing the
fresh-workspace fix.

Use shipped builders on a verified disposable replica-3 volume. Record baseline
settings and independent fresh brick roles, heal rows, object identity and
relevant metadata/logs. Builder state alone is not repair discovery. If native
healing clears the fault before a preview, zero proposed writes is a smoke or
native-heal-first result, not repair-apply proof. A stable repairable fixture,
independent discovery, reviewed plan, actual authorized writes and focused
post-repair verification are required for that stronger claim.

## Reboot, retention and results

When reboot testing is authorized, restart one guest at a time. Before the next,
verify its boot and mounts, service login, peer membership, bricks/self-heal
readiness and bounded heal convergence on every test volume. Stop the sequence
on a warning, degraded state, timeout or uncertainty; preserve diagnostics.
An earlier reboot before the volume existed does not qualify this stage.

Check hostname resolution and management-peer state from every guest. Brick
heal output can remain quiet while a management peer has lost name resolution.
A cloud-init system drop-in alone did not preserve hosts entries in one tested
image whose seed enabled hosts management. Verify the effective configuration
or template and repeat the reboot; retain the failed and corrected runs.

Set startup/heal time budgets and the expected healthy baseline before the
test, based on fixture size and observed platform behavior. Poll at a bounded
interval and retain the last state on timeout; never continue to the next
guest merely because the budget expired. Require all expected peers/bricks
online and the intended heal state, not just an SSH response.

Retain process exit/completion and logs, exact source hashes, independent
assertions, failure artifacts and qualified/skipped/deferred status privately.
Export results before shutdown; exclude credentials, cloud-init seeds and live
mounted work roots. Link private records rather than copying them into source.
A temporary directory disappearing does not establish test completion.

Record separately: fresh baseline, first access, install, peer transfers,
reinstall, privileged fidelity, native healing, repair apply, reboot and cleanup.
If asked to retain the lab, cleanup is deferred, not passed; verify it is off.
