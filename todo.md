# FED-SPA — Project TODO

The living task tracker for the FED-SPA project (Florida Establishment Directory — Spa & Parlor Assurance). Maintainers and contributors: check items off, add new ones with an owner and a release target, and keep the [ROADMAP](ROADMAP.md) for direction and this file for concrete work. Items here are concrete and completable; standing policy lives in [GOVERNANCE](GOVERNANCE.md).

Status legend: `[ ]` open · `[x]` done · `[\]` in progress · `[-]` declined (with reason — declined items stay visible on purpose).

## Now — current cycle

- [x] Ship release `2026.1` (data as of 2026-09-07) — seed record Halo Asian Spa MM41109, empty watchlist envelope, all six surfaces
- [x] Freeze the crypto envelope spec at v1 ([wiki/Crypto-envelope-spec.md](wiki/Crypto-envelope-spec.md)) and land the five byte-compatible implementations
- [x] Land CI: schema validation → fan-out drift check → web smoke tests → envelope round-trip → packaged artifact (GitHub-owned actions only)
- [x] Complete the community layer: issue templates, PR template, discussions welcome, wiki (7 pages), prompts library (5 prompts), root docs
- [x] Ship release `2026.2` (data as of 2026-09-11) — first county sweep: 47 licensed records (Fort Pierce → Homestead corridor, 5 counties), 44 watchlist entries, CSV export, root data/ Pages mirror added to the fan-out

## Next — the next release window

- [ ] **Second corridor pass.** 283 establishment rows remain unchecked from the 2026.2 sweep (see [wiki/County-sweep-2026.2.md](wiki/County-sweep-2026.2.md)). Check them against the portal per [docs/annual_update_workflow.md](docs/annual_update_workflow.md), PR the records with check dates. *Owner: data lead.*
- [ ] **Production re-encryption of the 2026.2 envelope.** The committed blob was generated with a workflow-test password; re-encrypt with the production subscriber code before publishing, then rotate the code per the standing cycle. *Owner: code distributor.*
- [ ] **Interior counties.** Wellington, Coral Springs, Miami interior — the unswept South Florida interior with the highest establishment counts per DOH annual reports. *Owner: data lead.*
- [ ] **Seed record expiry watch.** MM41109 expires 2027-08-31 — inside the app's "expiring soon" window (it did not lapse at the 2026.2 sweep; license shows Clear through 2027-08-31). Re-check at the next cycle; document the status transition honestly in the [refresh log](wiki/Annual-refresh-log.md) whether it renewed or lapsed. *Owner: data lead.*
- [ ] **Watchlist re-check pass.** The 44 watchlist entries carry their documented search terms in `reason` — re-run those searches; a renewal moves an entry out of the watchlist. *Owner: data lead.*
- [ ] **Subscriber code distribution channel.** The 2026.2 watchlist is live and non-empty — the channel table in [docs/password_distribution.md](docs/password_distribution.md) needs real links before subscribers are charged. *Owner: code distributor.*
- [ ] **iOS project file generation run-through.** Do the `ios/README.md` first-open recipe once on a clean machine, note any drift between the recipe and reality, fix the doc. *Owner: iOS surface owner.*

## Standing — every annual cycle

- [ ] Run the annual refresh end-to-end (`admin_scripts/merge_and_encrypt.sh`), including the verify step that decrypts the shipped envelope with the correct code
- [ ] Rotate the subscriber code with the release; rotate the Ko-fi link if the handle changed
- [ ] Append the release row to [wiki/Annual-refresh-log.md](wiki/Annual-refresh-log.md) and the entry to `data/meta/changelog.md`
- [ ] Tag `data-<year>.<n>` (e.g. `data-2026.2`) and ship every surface from the same tag — no partial releases ([DEPLOYMENT.md](DEPLOYMENT.md))
- [ ] Post-ship checklist: spot-check `as_of` and record count on all six surfaces

## Watch items — not scheduled, just watched

- [ ] GitHub ships first-party mobile build actions → add Android/iOS compilation to CI (constraint-compatible; see [BUILD.md](BUILD.md))
- [ ] Florida publishes an official open-data export of licensed establishments → evaluate manual annual import, validated against the portal
- [ ] Sustained contributor growth → the community coverage program sketched in [ROADMAP.md](ROADMAP.md) (each contributor takes a county)
- [x] Sustained demand for the dataset in tabular form → CSV export from the fan-out script (shipped in 2026.2: `web/data/licensed.csv` + root mirror)

## Declined — visible on purpose

- [-] Backend / API / accounts / sync — violates constraint 1; the argument is in the [FAQ](FAQ.md)
- [-] Third-party anything, on any surface — violates constraint 2
