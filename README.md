# vortaforge/.github

Organization-wide defaults for [VortaForge](https://github.com/vortaforge).

- `profile/README.md` - the public organization profile page
- `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SUPPORT.md` - default community health files
- `CREDITS.md` - AI-assistance disclosure for this repository
- `TRANSFER.md` - dated handover record; read its status update before treating it as the current maintenance state

## Datapack policy (2026-11-05)

`vortaforge/core` retired its datapack programme: datapacks have no type
safety, no security model, no debugging, no warnings and scored low in review,
and the maintainer gave up on them after real problems as a plain player using
a datapack with no client mod installed. This repository carries the
organisation-wide half of that decision:

- `blocklist/blocklist.json` - account blocklist (datapack developers,
  datapack tooling authors, bot/AI accounts). **Generated**; do not edit by
  hand.
- `generated/blocklist.json` - the same data in a stable form for tooling.
- `scripts/blocklist_sync.py` - mirrors `vortaforge/core`'s blocklist here, and
  runs the public-profile scan that flags accounts whose GitHub bio/company
  looks like datapack development.
- `.github/workflows/datapack-blocklist-sync.yml` - daily sync + profile scan.
  A hit opens an issue for a human decision; it never blocks anybody silently,
  and it only reads public profile fields for accounts that already interacted
  with the organisation.

Pull requests from a blocked account are refused by
[`vortaforge/core`'s guard](https://github.com/vortaforge/core/blob/main/scripts/datapack_guard.py)
unless a maintainer adds the `datapack-approved` label. The full policy,
including the kill switch and how the archived packs are stored, is in
[`vortaforge/core/docs/ARCHIVAL.md`](https://github.com/vortaforge/core/blob/main/docs/ARCHIVAL.md).

Read [`blocklist/README.md`](blocklist/README.md) before changing an entry.

GitHub uses these files for any repository in the organization that does not
provide its own copy. `LICENSE`, `CODEOWNERS`, `.gitignore`, `.gitattributes` and
workflows are **not** inherited and must live in each repository.
