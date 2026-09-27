# Gluster Repair Agent Companion

Portable skills and a Codex adapter for working with the separately installed
Gluster Repair Tool. It is an optional guide, not an autonomous repair agent.

The root [plugin manifest](.codex-plugin/plugin.json) packages the seven skills
for reusable Codex distribution. It has no marketplace entry and is not
installed by this source tree. Local discovery can instead use a selected skill
directory under `.agents/skills/` in a repository or `$HOME/.agents/skills/`.

The companion contains guidance, private-file templates, and a local privacy
audit. It has no cluster credentials, hardcoded host inventory, private helper
dependency, or alternate repair engine. The core runs without it.
Read the [beta.3 release notes](docs/RELEASE_NOTES_v0.1.0-beta.3.md) for the
matching core release and qualification limits.

## Layout

- skills/: focused maintainer, operator, triage, canary, setup and VM lab instructions.
- [VM playground and qualification](skills/gluster-vm-lab/SKILL.md): reusable
  developer/tester environments, fresh-install tests, checkpoints and retention.
- [Gluster major-version qualification](skills/gluster-version-qualification/SKILL.md):
  focused interface review and bounded compatibility evidence for a new release.
- adapters/codex/: discovery and installation guidance.
- scripts/: private-directory initialization, candidate privacy audit, and
  bounded source/candidate helper commands.
- [Portable helper boundary](docs/PORTABLE_HELPERS.md): public helper scope and
  private-operation limits.
- [Companion role](docs/ROLE.md): setup, troubleshooting, documentation/forum
  use, and support-case boundaries.
- [Core qualification boundary](docs/CORE_QUALIFICATION.md): what the
  companion cannot claim until the separately installed engine is qualified.
- .codex-plugin/plugin.json: portable plugin metadata for the seven skills.
- templates/: blank private steering and operational ledger documents.
- steering/TODO.md: companion-specific release work.
- MIGRATION.md: separation, cutover, and commit-history rules.
- [HISTORY.md](HISTORY.md): summarized origins of the portable agent workflow.
- [Source provenance](PROVENANCE.md): public ownership and contribution record.
- [Validation](docs/VALIDATION.md): completed checks and remaining limits.
- [Release preparation](docs/RELEASE_PREPARATION.md): local readiness and
  publication gates. Repository destinations are in [MAINTAINERS.md](MAINTAINERS.md).
- [Scenario checks](docs/SCENARIO_CHECKS.md): source-level checks for repair,
  support-draft, and replica-3 setup questions.

The original ledger stays private. The core's HISTORY.md is its frozen
implementation prehistory. This companion does not invent a prior release
history; future implementation details belong in its commits.

## Private steering and ledger

Personal settings go in
`$HOME/.gluster-repair-private/steering/`; personal incidents and detailed
operational records go in the sibling `ledger/` directory. The optional
GLUSTER_REPAIR_PRIVATE_ROOT environment variable must point under the user's
home and outside repositories.

To create blank private files without overwriting existing ones:

```bash
python3 scripts/init_private.py
```

The initializer creates only local files; it installs no skills, modifies no
agent configuration, and grants no access. Never fill the templates in this
repository with personal information.

See [the boundary guide](docs/PRIVACY.md) and
[the private steering/ledger guide](docs/PRIVATE_STATE.md) and
[the Codex adapter](adapters/codex/README.md).

## Checks

```bash
python3 -m unittest discover -s tests -v
python3 scripts/check_candidate.py --root . inventory
python3 scripts/audit_tree.py . --public-identity 'chosen public name' \
  --public-copyright-holder 'chosen public name'
```

Audit another candidate by passing its directory. Supply each intentionally
public copyright holder with `--public-copyright-holder`; it is accepted only
in an exact source copyright notice. Optionally pass
`--private-patterns /path/outside/repos/patterns.txt`; one literal identifier
per line. Keep that list private. The tool reports file/line/category without
printing the matching values. A passed heuristic scan cannot prove absence of
all personal information; inspect generated artifacts and Git identity too.

For the companion's named helper, use:

```bash
python3 scripts/check_candidate.py --root . privacy \
  --private-patterns /path/outside/repos/patterns.txt \
  --public-identity 'chosen public name' \
  --public-copyright-holder 'chosen public name'
```

The identifier file must exist outside the candidate. Relative file paths
are interpreted from your calling directory, even when `--root` selects a
different directory.

The core's execution, backup and bootstrap findings have local candidate fixes.
Scoped Ubuntu installation and privileged backup checks passed. One supervised
nonempty missing-replica repair passed on a disposable Ubuntu 24.04/Gluster
11.1 lab after a staging defect was fixed; broader recipe and platform
qualification remain open. These skills preserve the review boundaries and
cannot make unqualified engine code safe. The first beta's scoped core review
and adapter checks are recorded in [validation](docs/VALIDATION.md).

The selected copyright holder is listed in [MAINTAINERS.md](MAINTAINERS.md).
This companion is licensed under [GPL-2.0-only](COPYING). Its provenance record is in
[LICENSE-STATUS.md](LICENSE-STATUS.md).
