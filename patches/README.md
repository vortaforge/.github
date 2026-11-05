# patches/

The organisation-wide datapack blocklist change for `vortaforge/.github`, as a
`git format-patch` mailbox.

| File | What it applies |
|---|---|
| `0001-feat-blocklist-organisation-wide-datapack-blocklist-.patch` | Adds `blocklist/`, `generated/`, `scripts/blocklist_sync.py` and the `datapack-blocklist-sync` workflow; documents the policy in `README.md` and `CONTRIBUTING.md`. |

## Apply

```bash
git clone https://github.com/vortaforge/.github.git
cd .github
git checkout -b datapack-blocklist
git am patches/*.patch        # or: git am /path/to/core/archived/patches-gh/*.patch
```

Apply `vortaforge/core`'s patch **first**: this one mirrors core's
`blocklist/blocklist.json`, and the sync workflow expects it to exist.

## Verify

```bash
python3 -c "import json;json.load(open('blocklist/blocklist.json'));print('json ok')"
python3 scripts/blocklist_sync.py --check --core ../core    # exit 0 = in sync
```

The workflow itself was validated as YAML only; it has not run.
