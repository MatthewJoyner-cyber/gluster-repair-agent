# Private remote-operation contract

This local-only record describes a bounded helper that a maintainer has
already installed and reviewed. It is not a credential store and does not
authorize an operation on its own.

- Helper command/path:
- Allowed host aliases:
- Allowed inspection roots:
- Allowed edit roots:
- Allowed named inspection actions:
- Allowed named edit actions:
- Required SSH host-key policy:
- Required local approval/authority:
- Evidence-log location:
- Last contract review date:

For every new host, path root, privilege, or write action, update the installed
helper and this record together, test its refusal boundaries, and seek the
required authority. Do not bypass a refused bounded helper with raw SSH, sudo,
or an interpreter. Do not store account names, IP addresses, credentials, or
raw incident evidence here; use the private ledger where necessary.
