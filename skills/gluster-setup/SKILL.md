---
name: gluster-setup
description: Plan and verify a safe Gluster and Gluster Repair Tool setup, including replica-3 volumes.
---

# gluster-setup

Be friendly, clear, and professional. Establish the requested scope before
giving commands: new lab or production, Gluster/OS versions, three distinct
failure domains, brick paths, client mount needs, backups, and who may change
the cluster.

For a reusable developer playground or fresh-system installation test, use
[gluster-vm-lab](../gluster-vm-lab/SKILL.md). Three guests on one host can test
peer behavior but are not three independent production failure domains.

Use official documentation that matches the installed Gluster version. For a
new replica-3 volume, first validate time/name resolution, firewall reachability,
peer connectivity, empty intended bricks, capacity, and recovery expectations.
From an approved peer, draft the selected `peer probe` steps, then a `volume
create <volume> replica 3 <host1>:<brick1> <host2>:<brick2> <host3>:<brick3>`
command and a separate `volume start <volume>` command. Do not add `force` or
run setup commands unless their need and authorization are explicit.

Verify every advertised peer hostname resolves from every guest, even when
probes use IP addresses; wait for connected membership on all peers. A failed
create can leave brick identity metadata despite an empty volume list. Inspect
and preserve residue before retrying; do not clear xattrs or reformat blindly.

After authorized setup, verify peer status, volume info/status, every brick and
self-heal daemon, client mount behavior, and `volume heal <volume> info`.
Record topology and results privately. A familiar name or three endpoints alone
does not prove a safe replica-3 configuration.

Then install or select the repair-tool checkout separately. Run its offline
help/tests first, set only documented state paths, and collect bounded health
and heal evidence before attempting a repair. See [the companion role guide](../../docs/ROLE.md).

For a fresh install, keep initial administrator access distinct from the
service policy. Preflight success is not installation proof: independently
check the created account, installed files, actual sudoers and service login.
Keep streamed shell stdin away from child SSH consumption; use separate
invocations or a reviewed script file. See the VM skill's qualification method.
