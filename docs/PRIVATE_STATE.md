# Optional private steering and ledger

The companion works without private files. Users who want continuity can create
`$HOME/.gluster-repair-private/` with `python3 scripts/init_private.py`. Keep
it outside all repositories and export bundles.

## Steering

`steering/START_HERE.md` holds the current local context: selected core and
agent checkout/install roots, approved bounded helpers, supported versions,
operator preferences, and support-draft preferences. It is not execution
authority and must not contain credentials.

`steering/REMOTE_OPERATION.md` records the contract for an already installed
bounded remote/privileged helper: selected aliases, root allowlists, named
actions, host-key policy, required authority, evidence-log location, and review
date. The template contains no site configuration. Keep account names, IPs,
credentials, and raw evidence in the private ledger instead.

## Ledger

Use the private `ledger/` directory for three records:

- `TODO.md`: current local tasks and their next safe action.
- `LEDGER.md`: dated observations, decisions, support-draft status, known
  caveats, and links to local evidence without copying it.
- `RUNS.md`: one dated entry per live or lab run: target scope, evidence source,
  authority, writes attempted, verification, cleanup, and remaining unknowns.

Record host names, organization details, paths, account names, case identifiers,
and raw evidence only in these private files. Public commits and support drafts
use a reviewed, sanitized conclusion instead. Never treat a ledger entry as
fresh evidence or permission for a later repair.
