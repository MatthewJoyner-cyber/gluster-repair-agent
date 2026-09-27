# Repository release preparation

## First beta scope (2026-09-27)

The core's `docs/FIRST_BETA_RELEASE_PLAN.md` owns the joint acceptance plan.
The companion follows the core's declared beta scope; it does not wait for
every optional core feature or Linux distribution to be qualified. This is a
best-effort open-source beta with no guarantees, subject to [COPYING](../COPYING).
The public test claim is the recorded Ubuntu LTS combination. SUSE/SLES,
openSUSE, RHEL and other distributions remain untested; reports are welcome.

Before the first companion prerelease:

1. Reconcile guidance with the final core feature table. Preserve native healing
   before tool repair, recognize that a native-healed canary needs no repair,
   and keep unqualified tool write features disabled. Guidance for separate
   administrator-approved Gluster operations must distinguish them from the
   tool's capability gate.
2. Run the local tests, seven-skill/manifest checks and the use-tool, replica-3
   setup, optional support-draft, native-healed-case and untested-distribution
   answer scenarios. Repeat plugin lifecycle only if package/adapter behavior
   or the intended CLI changed since its recorded qualification.
3. Audit inventory, links, privacy and public Git history. Confirm private
   steering/ledger setup is optional, stays outside both repositories and
   requires no maintainer-specific helper or account.
4. After the core review and companion checks pass, record the matching tested
   core version, create reviewed commits/tags and publish a clearly labelled
   `v0.1.0-beta.2` prerelease. The privately staged beta.1 tag marks an earlier
   candidate. Invite reviewed metadata-only reports; never
   submit reports or upload server file contents automatically.

The operator resumed release work after the earlier lab pause. This plan alone
does not claim acceptance or open core feature gates.

## Shared repository preparation

The separate GitHub destinations are recorded in
[MAINTAINERS.md](../MAINTAINERS.md). Apply these checks to the exact source
revision selected for publication or a later prerelease.
The original repository and its ledger remain private reference material.

## Local preparation

- Keep an exact `FILES.txt` inventory of public source, tests and documentation.
  Exclude Git metadata, caches, runtime evidence, private settings and credentials.
- Keep GPL-2.0-only notices, chosen maintainer credit and source provenance
  consistent. Preserve the frozen sanitized `HISTORY.md`; record future
  implementation detail in commit bodies rather than a replacement ledger.
- Use an independently initialized Git history and the deliberately selected
  public author identity. Preserve authorized sanitized development checkpoints;
  never import the predecessor's Git database or tags.
- Review README commands, relative links and current qualification statements.
  Run the offline suite and the privacy scan with the external identifier list.
- Keep remote creation and push separate from local preparation. The companion
  remains optional; the core must work without its skills or private settings.

## Publication checkpoint

1. Complete the first-beta scope above and the core's finite acceptance plan;
   address known serious defects without making optional coverage a blocker.
2. Freeze the exact source snapshot; repeat inventory, source notices, privacy,
   local links and relevant tests. Inspect generated files and the Git history
   separately because the source privacy scan excludes `.git`.
3. Review the final diff and public author/committer metadata, then commit when
   authorized with problem, change, rationale, validation and caveats.
4. Create the first completed-review tag only after its remediation is
   implemented and validated. Record the reviewed scope; a tag alone is not
   acceptance of every platform or repair case.
5. Verify both GitHub destinations, push only clean reviewed branches and
   deliberately selected tags, and check cross-repository and public-download
   links before announcing the release.

Read [MIGRATION.md](../MIGRATION.md) for source/state cutover. Final tests may
require fixes; rerun the checks affected by those changes before publication.

## Companion qualification checkpoint

- Reconcile guidance with the core's final reviewed behavior and scope:
  [core qualification](CORE_QUALIFICATION.md).
- Repeat source-level repair, support-draft and replica-3 setup scenarios after
  any guidance changes: [scenario checks](SCENARIO_CHECKS.md).
- Verify all seven skills and the plugin manifest, and repeat the disposable plugin
  lifecycle on the intended release CLI if the adapter or target CLI changes.
  The existing tested version and lifecycle result are in
  [VALIDATION.md](VALIDATION.md).
- Review both final repository destinations and instructions together, while
  keeping private steering and optional ledgers outside either tree:
  [private state](PRIVATE_STATE.md).

Use the companion's [TODO](../steering/TODO.md) for the remaining queue.
The seven-skill package check and fresh-session qualification-skill answer were
completed on Codex CLI 0.155.1. Recheck affected scenarios if guidance or the
target CLI changes before publication.
