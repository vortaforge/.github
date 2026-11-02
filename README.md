# VortaForge organization defaults

This repository contains the shared community-health guidance for the
[VortaForge](https://github.com/vortaforge) organization and the README shown on
its public organization profile. It complements, rather than replaces, the
project-specific instructions in [vortaforge/core](https://github.com/vortaforge/core).

## Contents at a glance

| File | Purpose |
| --- | --- |
| [`profile/README.md`](profile/README.md) | Public introduction to the organization and its main projects. |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Default contribution and review guidance. |
| [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) | Expected conduct and how to report conduct concerns. |
| [`SECURITY.md`](SECURITY.md) | Private vulnerability-reporting instructions. |
| [`SUPPORT.md`](SUPPORT.md) | Where to ask questions and report ordinary bugs. |
| [`TRANSFER.md`](TRANSFER.md) | Dated handover record and subsequent status updates. |
| [`CREDITS.md`](CREDITS.md) | Attribution and disclosure of AI-assisted changes. |
| [`LICENSE`](LICENSE) | License for this repository; check each other repository's own license. |

## How the defaults work

GitHub can display supported community-health files from a public `.github`
repository when an organization-owned repository does not provide its own file
of that type. A repository's own applicable file takes precedence. The shared
files do not appear in the other repository's Git history or downloaded clone;
see GitHub's documentation for the supported file types and precedence. [1](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)

The public organization overview uses `profile/README.md`; it is distinct from
this repository's root README. [2](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/customizing-your-organizations-profile)

A default `LICENSE` is **not** inherited. `CODEOWNERS`, `.gitignore`,
`.gitattributes` and workflows are not provided to other repositories by this
mechanism either; maintain each where it is needed. This repository does not
itself change organization settings, repository permissions, billing,
credentials or ownership.

## Contributing and getting help

1. Read the affected repository's README and project-specific guidance first.
2. Search existing issues and pull requests before opening a duplicate; use
   [`SUPPORT.md`](SUPPORT.md) for ordinary questions and bug reports.
3. For proposed changes, follow [`CONTRIBUTING.md`](CONTRIBUTING.md), preserve
   existing copyright and origin notices, and explain the scope and checks in
   the pull request. A project can have stricter local instructions.
4. Do **not** post security details publicly. Follow
   [`SECURITY.md`](SECURITY.md) and use a private channel.

For `vortaforge/core`, the contribution guide identifies
`./gradlew ci -PconfirmZip=yes` as the canonical local gate. A passing build is not proof of
runtime datapack behavior; follow the project's own safety rules and report
what was and was not tested.

## Maintenance and handover

[`TRANSFER.md`](TRANSFER.md) is a historical record with later updates. It must
not be read as proof that ownership has already changed or that every old
credential has been cleaned up. The current maintainer remains responsible
until a successor explicitly accepts and the current handover checklist is
completed. Check the main repository's
[handover runbook](https://github.com/vortaforge/core/blob/main/HANDOVER.md) and
recent activity for current status.

The projects are volunteer-maintained. Response times, availability and
support for archived projects are not guaranteed.

## License and attribution

This repository's terms are in [`LICENSE`](LICENSE); contribution and origin
notices are in [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`CREDITS.md`](CREDITS.md).
Other repositories may have different terms, so inspect their own `LICENSE` and
`NOTICE` files before using or redistributing them.
