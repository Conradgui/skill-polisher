# Release Drift

Read this reference when an existing skill may differ across its runtime folder, repository,
published artifact, or installed copy. Keep the audit read-only unless the user separately requests
repair or publication.

## Reconstruct release state

Identify the canonical runtime artifact and compare only the layers relevant to the user's claim:

1. **Runtime**: `SKILL.md`, referenced resources, scripts, and assets.
2. **Harness metadata**: identity, invocation policy, UI fields, and declared dependencies.
3. **Repository contract**: installable allow-list, lifecycle state, human documentation,
   attribution, and supported platforms.
4. **Version state**: changelog or release intent, package or plugin version, tag, and published
   release identity.
5. **Evidence state**: CI result, fresh-clone validation, installer discovery, and installed-file
   comparison.

Report source, version, remote publication, CI, and installation as separate states. A clean local
tree does not prove publication; a published tag does not prove installation; a successful install
does not prove the installed content matches the current source.

## Apply proportional rigor

Start with local identity, metadata, links, and hashes. Query remote or installed state only when the
reviewed claim depends on it. Run fresh-clone, cross-platform, or installer replay checks when a
release-affecting change or an explicit support claim makes them decision-relevant.

When drift is found, identify the authoritative owner before recommending synchronization. Preserve
attribution and coexistence with upstream or neighboring skill identities. Route a first release or
new identity through `Skill Creator Pro`; keep maintenance of an existing release in Skill Polisher.
