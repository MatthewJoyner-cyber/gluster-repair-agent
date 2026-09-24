# Codex adapter

The portable skill directories are in ../../skills. No personal configuration
or installed helper set is bundled.

For local use, copy a selected complete skill directory into
`$HOME/.agents/skills/`, or into `.agents/skills/` in the chosen workspace.
Keep its SKILL.md and any references together. Check for an existing skill with
the same name before copying; do not overwrite customized skills.
These are the current documented discovery locations.
[Official skill documentation](https://learn.chatgpt.com/docs/build-skills)

For reusable distribution, this candidate packages all six skills through the
root [plugin manifest](../../.codex-plugin/plugin.json). The manifest has no
connector, application, credential, local-helper, marketplace, or automatic
installation configuration. It must be validated and tested in a fresh Codex
session before a release claims compatibility.
[Official distribution guidance](https://learn.chatgpt.com/docs/build-skills)

Installation does not install the core, grant sudo/SSH access, or change Codex
trust settings. Provide local helper contracts and paths only through the
private steering root. Users without private steering can still review the
public source and run synthetic tests.

The `0.1.0` package structure and skill front matter were checked locally with
Codex CLI 0.155.1 and the official skill documentation on 2026-09-20. A
disposable local marketplace installed the then-five-skill package, and fresh read-only Codex
sessions explicitly loaded `gluster-setup` and `gluster-triage`. A temporary
cachebuster reinstall was also discovered in a fresh session; the plugin and
marketplace were then removed. This is local adapter compatibility only.
Record the tested CLI version, installation method, removal/update behavior,
and core version before claiming support on another environment.

The expanded six-skill package repeated installation, fresh-session discovery,
cachebuster update discovery and removal on the same CLI on 2026-09-24. See
[validation](../../docs/VALIDATION.md) for the tested scope.

When compound shell syntax receives one opaque approval, split independently
privileged operations or use a reviewed temporary input file. Do not encode
patches or use an interpreter merely to hide the operations being approved.
Recheck installed CLI behavior and official command-policy documentation about
monthly and after upgrades; this is adapter behavior, not a permanent repair rule.
