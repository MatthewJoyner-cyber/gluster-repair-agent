# Provisioning and lifecycle

## Select the environment

Read the selected core's current bootstrap contract and supported layouts.
Inspect available RAM/CPU, local disk backing, virtualization access, existing
domains/networks and route overlap before proposing resources. Keep guest
disks independent of the Gluster storage being tested; a pathname alone does
not prove local backing. Never attach production bricks to the lab.

A small tested shape was three headless guests, each with one vCPU and 4 GiB
RAM, a sparse OS overlay and a separate tiny brick disk. That is a starting
point, not an OS minimum or a performance recommendation. Size OS/package/log
space and brick capacity for the chosen workload; leave host memory reserve
and account for overlay growth. Start one guest first and measure memory/free
space before booting the remainder. Disable lab autostart unless requested.

Use an official, version-pinned cloud image. Verify signed checksum metadata
with an independently trusted vendor key, verify the image digest, and inspect
its format/backing chain. Record provenance privately. Keep a read-only base
and separate guest overlays. A cloud image tests a preinstalled OS, not the OS
installer or a person's first password-entry experience.

Cloud-init may establish only the initial test administrator, fresh lab keys
and necessary guest configuration. Let the shipped bootstrap create the repair
account, service keys and sudoers. Wait for cloud-init to finish before judging
the baseline. Give each guest a unique instance identity, machine ID and SSH
host keys; verify host keys through a trusted console/provisioning channel
before pinning them. Never disable host-key verification to fix first access.

## Network and peer readiness

Create a dedicated lab network after checking route overlap. NAT alone is not
a firewall boundary. Define guest-to-host and guest-to-other-network access,
including IPv6, and verify the intended restrictions. Allow package access only
as needed; do not change the host's existing networks or shared firewall policy
to induce a fixture. Record the exact lab-owned network/firewall objects.

All peers must resolve the names Gluster actually advertises. Probing an IP
does not remove this requirement. If using guest hosts-file mappings, ensure
cloud-init does not later replace them and recheck after reboot. Inspect the
installed cloud-init version's configuration before choosing settings.

Wait for connected membership on every intended peer, not just a successful
probe exit. Verify selected disks are mounted and brick paths belong to those
guest disks before formatting or creating a volume. If creation fails and
volume listings are empty, inspect partial brick identity metadata first.
Preserve residue; do not force, reformat or clear trusted xattrs blindly. A new
empty directory on the verified disposable disk can support a new attempt
while retaining the failed evidence.

## Manifest and lifecycle

Before mutation, record canonical lab root, domain and network UUIDs, disk and
backing paths, ownership marker, image digest, source snapshot and lifecycle
instruction in protected private state. Names alone are insufficient identity
guards. Any helper should accept bounded named operations and verify these
identities before mutating or deleting resources.

For retained labs, verify UUIDs/disks/network, boot the existing guests, wait
for readiness and collect fresh peer/volume/heal state. Preserve the prior
baseline and failure evidence. Reusing an installed guest cannot establish a
fresh-install claim; use a known pre-install snapshot or new overlay for that
specific test without discarding the retained lab.

For shutdown, finish or record interrupted tests, export nonsecret results,
unmount test clients where appropriate, shut down gracefully and verify actual
power state. A shutdown request is not evidence that a guest has stopped. If
shutdown fails, report the state; do not silently force it off or undefine it.

For authorized removal, first retain evidence and verify all manifest-bound
resources. Remove only that lab's guests, disks, network, firewall objects and
temporary access; preserve shared bases and unrelated resources. Check host
inventory afterwards. Never infer removal authority from passing tests.

## Primary references

Consult versions matching the environment; these pages were checked when this
procedure was prepared on 2026-09-24:

- [libvirt network XML](https://libvirt.org/formatnetwork.html): forwarding,
  isolation and network configuration.
- [cloud-init modules](https://docs.cloud-init.io/en/latest/reference/modules.html):
  guest identity, SSH and hosts-file management.
- [Gluster quick start](https://docs.gluster.org/en/latest/Quick-Start-Guide/Quickstart/):
  peer, brick and volume setup. Do not copy example `force` commands into a lab
  without an independently justified need.
