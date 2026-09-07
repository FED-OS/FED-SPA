# FED-SPA — Project TODO

The living task tracker for the FED-SPA project (Florida Establishment Directory — Spa & Parlor Assurance). Maintainers and contributors: check items off, add new ones with an owner and a release target, and keep the [ROADMAP](ROADMAP.md) for direction and this file for concrete work. Items here are concrete and completable; standing policy lives in [GOVERNANCE](GOVERNANCE.md).

Status legend: `[ ]` open · `[x]` done · `[\]` in progress · `[-]` declined (with reason — declined items stay visible on purpose).

## Now — current cycle

- [x] Ship release `2026.1` (data as of 2026-09-07) — seed record Halo Asian Spa MM41109, empty watchlist envelope, all six surfaces
- [x] Freeze the crypto envelope spec at v1 ([wiki/Crypto-envelope-spec.md](wiki/Crypto-envelope-spec.md)) and land the five byte-compatible implementations
- [x] Land CI: schema validation → fan-out drift check → web smoke tests → envelope round-trip → packaged artifact (GitHub-owned actions only)
- [x] Complete the community layer: issue templates, PR template, discussions welcome, wiki (6 pages), prompts library (5 prompts), root docs

## Next — the next release window

- [ ] **Coverage: first county sweep.** Prioritize by the feature-request signal naming counties (Issues), check every establishment against the portal per [docs/annual_update_workflow.md](docs/annual_update_workflow.md), PR the records with check dates. *Owner: data lead.*
- [ ] **Seed record expiry watch.** MM41109 expires 2027-08-31 — inside the app's "expiring soon" window. Re-check at the next cycle; document the status transition honestly in the [refresh log](wiki/Annual-refresh-log.md) whether it renewed or lapsed. *Owner: data lead.*
- [ ] **First watchlist entries.** Only when the bar is met: a documented zero-match search with terms and date in `status_note`. No quotas, no shortcuts. *Owner: data lead.*
- [ ] **Subscriber code distribution channel.** Stand up the channel table in [docs/password_distribution.md](docs/password_distribution.md) with real links before the first non-empty watchlist ships. *Owner: code distributor.*
- [ ] **iOS project file generation run-through.** Do the `ios/README.md` first-open recipe once on a clean machine, note any drift between the recipe and reality, fix the doc. *Owner: iOS surface owner.*

## Standing — every annual cycle

- [ ] Run the annual refresh end-to-end (`admin_scripts/merge_and_encrypt.sh`), including the verify step that decrypts the shipped envelope with the correct code
- [ ] Rotate the subscriber code with the release; rotate the Ko-fi link if the handle changed
- [ ] Append the release row to [wiki/Annual-refresh-log.md](wiki/Annual-refresh-log.md) and the entry to `data/meta/changelog.md`
- [ ] Tag `data-<year>` and ship every surface from the same tag — no partial releases ([DEPLOYMENT.md](DEPLOYMENT.md))
- [ ] Post-ship checklist: spot-check `as_of` and record count on all six surfaces

## Watch items — not scheduled, just watched

- [ ] GitHub ships first-party mobile build actions → add Android/iOS compilation to CI (constraint-compatible; see [BUILD.md](BUILD.md))
- [ ] Florida publishes an official open-data export of licensed establishments → evaluate manual annual import, validated against the portal
- [ ] Sustained contributor growth → the community coverage program sketched in [ROADMAP.md](ROADMAP.md) (each contributor takes a county)
- [ ] Sustained demand for the dataset in tabular form → CSV export from the fan-out script

## Declined — visible on purpose

- [-] Backend / API / accounts / sync — violates constraint 1; the argument is in the [FAQ](FAQ.md)
- [-] Third-party anything, on any surface — violates constraint 2
- [-] Live data / auto-refresh / update nudges — violates the honesty of the annual cadence ([ADR-006](ADR.md))
- [-] Reviews, ratings, photos, user-generated content — makes us a platform and a data processor; outside scope by design
- [-] Bulk scraping of the MQA portal — manual, documented, per-record verification is the dataset's entire integrity

## Done — recent history

- [x] 2026: project structured, three constraints locked, logo + icon sets generated, schema committed, seed record verified, `2026.1` shipped with all six surfaces and the full community layer. *(Older completed items roll into [CHANGELOG.md](CHANGELOG.md) — this section keeps only the last cycle or two.)*
