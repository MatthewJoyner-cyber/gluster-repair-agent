# Companion development rules

Use steering/TODO.md for the queue and MIGRATION.md for repository boundaries.
Keep portable repair reasoning in skills and agent-specific discovery in adapters.
Do not add a second repair engine or hardcode a user's installed helpers.

Personal preferences, topology, incidents, and operational logs stay in the
external private steering/ledger. No live credentials or personal identifiers
belong in examples, tests, comments, commit messages, or templates.

Use detailed commit bodies for new implementation history: problem, change,
rationale, validation, caveats. Do not import the predecessor's ledger or tags.
Preserve unrelated work and commit/publish only with user authority.

Prefer bounded helpers when available. Keep independently privileged commands
reviewable; never evade a denied helper through broader permissions.
Run local tests and the candidate privacy scan for relevant changes.
