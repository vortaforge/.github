# blocklist/ (organisation-wide)

**Generated. Do not edit by hand.** The source of truth is
`vortaforge/core`'s `blocklist/blocklist.json`; this copy is written by
`scripts/blocklist_sync.py` and committed by
`.github/workflows/datapack-blocklist-sync.yml`.

| File | Meaning |
|---|---|
| `blocklist.json` | The mirror, normalised (sorted entries, `generated_on`, `generated_from`). |
| `../generated/blocklist.json` | The same data for tooling that should not read the editable path. |
| `../generated/profile-scan.json` | Output of the last public-profile scan (accounts, verdicts, matched tokens). |

## How enforcement works

1. `vortaforge/core`'s guard (`scripts/datapack_guard.py`) refuses pull requests
   from blocked logins unless a maintainer adds the `datapack-approved` label.
2. This repository's sync workflow keeps the org-wide list current and opens an
   issue when the profile scan matches an account.
3. The account is only ever blocked after a human resolves the issue - except
   that pull requests stay refused (fail-closed) while it is unresolved.

## The profile scan

- Runs against accounts that already interacted with the organisation (recent
  PR/issue authors). Never a global search.
- Reads **public** profile fields only: `bio`, `company`, `name`, `blog`.
- Matches the tokens in `policy.profile_tokens` (`datapack`, `mcfunction`,
  `pack.mcmeta`, ...), unless the profile carries a
  `policy.profile_exempt_tokens` phrase.
- Writes `generated/profile-scan.json`; never prints a token or credential.

## Changing the list

```bash
# in a vortaforge/core checkout
$EDITOR blocklist/blocklist.json
python3 scripts/datapack_guard.py --audit-refs --blocklist

# in this repository, to preview/refresh the mirror locally
python3 scripts/blocklist_sync.py --check --core ../core   # exit 1 = drift
python3 scripts/blocklist_sync.py --write --core ../core
```

Every entry needs a `reason`, an `added_on` and an `added_by`. Exact logins
only - no wildcards; use `ref_patterns` for branch/tag names and `user_ids` for
rename-proof numeric ids (`gh api users/<login> --jq .id`). This file is public
and will be read by the blocked person, so the reason must be a policy decision,
not an insult.
