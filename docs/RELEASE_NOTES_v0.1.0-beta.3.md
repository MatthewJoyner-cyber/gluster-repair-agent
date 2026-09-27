# Gluster Repair Agent Companion v0.1.0-beta.3

First public beta of the optional Codex companion for the separately
installed `gluster-repair-tool` at the matching tag.
It packages seven focused skills for operator guidance, evidence-first triage,
setup, maintainer work, canary labs, VM playgrounds and qualification of a new
Gluster version. It is guidance, not an independent repair engine.

Read the [README](../README.md) and [Codex adapter guide](../adapters/codex/README.md)
for local discovery and installation. Private steering and ledgers are optional
and live outside either source repository. The companion does not create
cluster credentials or upload evidence.

The guidance follows the core's narrow beta scope: Gluster-native healing
first; review current health, backup and preview before a write; only the
supervised nonempty missing-replica file repair has the stated live proof on
Ubuntu 24.04 LTS and Gluster 11.1. Other repair recipes are experimental, and
tool-driven full namespace heal and native per-file resolver writes stay
disabled. See the [core qualification boundary](CORE_QUALIFICATION.md).
Other distributions and Gluster 11.2 are not claimed as tested.

Local qualification covered 26 companion tests, seven skill validators,
source inventory/privacy checks, exact installed package hashes and a fresh
read-only Codex skill question on CLI 0.155.1. It did not requalify any core
repair write. See [validation](VALIDATION.md).

Use this repository's GitHub issues for companion setup or guidance feedback.
Share reviewed metadata and synthetic aliases only; keep credentials, private
topology and server file contents out of reports. The plugin uses base version
`0.1.0`; `beta.3` identifies this Git candidate.
