# Portable helper boundary

This companion can define small, auditable helpers for source work. It cannot
safely ship a universal remote or privileged wrapper: host names, SSH identity,
approved roots, service accounts, and sudo policy are maintainer-specific and
belong in private steering.

## Public helper contracts

The companion provides parameterized helpers with named, bounded subcommands:

- **Inspect:** `scripts/inspect_tree.py` provides Git status/diff checks,
  bounded literal search, and bounded file windows under an explicitly selected
  repository root. It accepts no shell expression or arbitrary command.
- **Reviewed edit:** `scripts/apply_reviewed_patch.py` checks a readable patch against one selected Git root,
  displays the target paths and diff check, then applies only after a distinct
  explicit apply command. Reject path traversal, multiple roots, and hidden
  repository metadata. Its `apply` action repeats the patch check first.
- **Named checks:** `scripts/check_candidate.py` runs declared tests, Python
  syntax, the privacy audit, or an inventory check for one selected companion
  candidate. It accepts no arbitrary test command, shell expression, package
  operation, or installation action.
  The `privacy` check accepts `--private-patterns` for an external identifier
  file, resolved relative to the calling directory. It refuses files inside
  the candidate (including symlink targets) and reports locations without
  printing matching values. Other checks reject this privacy-only option.

Each helper must validate its root and paths, keep its output bounded, avoid
embedding maintainer paths or identities, and have temporary-directory tests.
It must never use an interpreter or encoded payload to conceal an operation
from an approval prompt.

## Private operation contracts

Remote inspection, edits, and privileged Gluster actions need a local wrapper
with explicit host and path allowlists. Keep that wrapper, its policy, and its
operational logs outside the public repository. The public skills may direct a
maintainer to use an already installed bounded helper, but must not imply that
one is bundled or authorized.

Review this boundary whenever Codex command-policy behavior changes and at
least monthly, because it exists to preserve readable, narrow approvals.
