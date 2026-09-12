# Data statistics

Counts per refresh. Update this page at every annual release (it's part
of the ship checklist in `annual_update_workflow.md`).

## Current release — 2026.2, as of 2026-09-11

| Metric | Count |
|---|---|
| Licensed establishments | 47 |
| Counties covered | 5 (St. Lucie, Martin, Palm Beach, Broward, Miami-Dade) |
| Municipalities listed in the corridor | 112 |
| Sweep rows processed | 399 (372 establishments + 27 evidence/license records) |
| Licensed statuses represented | 1 (Clear) |
| Watchlist entries (subscriber tier) | 44 (3 revoked · 30 no-license-found · 3 inactive · 8 expired) |

### Licensed by county

| County | Records |
|---|---|
| St. Lucie | 16 |
| Martin | 1 |
| Palm Beach | 26 |
| Broward | 3 |
| Miami-Dade | 1 |

### The first county sweep (2026.2)

The 2026.2 release is the project's first full corridor sweep: every
massage-establishment directory listing from Fort Pierce to Homestead
(US-1 / Federal Hwy corridor, 5 counties, 112 municipalities) checked
against the FL DOH MQA Verification Portal on 2026-09-09/10/11. Of 372
establishment rows, 89 were verified in this pass (12 GREEN, 22 BLUE,
42 YELLOW, 13 RED) and 283 remain unchecked — honestly excluded from both
tiers until someone looks at them. A further 27 rows are license-record
evidence captured during verification (22 RED, 2 YELLOW, 3 GREEN). The
methodology, inclusion bars, and evidence-row handling are documented in
[County-sweep-2026.2.md](County-sweep-2026.2.md).

The seed record from 2026.1 (Halo Asian Spa, MM41109) survives as one of
the 47, re-verified 2026-09-09 with the DOH Address of Record and its
predecessor license history (MM34578, voluntarily relinquished) in notes.

## Historical releases

| Tag | As-of date | Licensed | Unlicensed | Notes |
|---|---|---|---|---|
| data-2026.2 | 2026-09-11 | 47 | 44 | First county sweep: Fort Pierce → Homestead corridor |
| data-2026 | 2026-09-07 | 1 | 0 | Initial seed release |

## Status taxonomy

Licensed tier statuses (from the MQA portal):

`Clear · Active · Delinquent · Expired · Inactive · Probation`

Unlicensed tier statuses (what the converter maps portal outcomes to):

`no_license_found · expired · inactive · revoked · delinquent`

### How the sweep's working colors map to the two tiers

The sweep spreadsheet uses a working color taxonomy (GREEN/BLUE/YELLOW/RED/
GRAY). The mapping — implemented in `admin_scripts/xlsx_to_fedspa.py` — is:

| Sweep color | Portal license status | Lands in |
|---|---|---|
| GREEN / BLUE | Clear | Licensed tier (BLUE = zero-issue history) |
| YELLOW | Clear | Licensed tier — predecessor-license caveats carried in notes |
| RED | Revoked / Disc Relinquish / Null And Void / Vol Relinquish / VR Pend Bd Act | Watchlist |
| YELLOW | No Match Found / Multiple Candidates-Unconfirmed / Closed | Watchlist |
| GRAY / none | Not Checked | Excluded from both tiers (honesty over volume) |

## County coverage ambitions

The corridor (St. Lucie, Martin, Palm Beach, Broward, Miami-Dade) is now
swept. The refresh procedure still targets statewide coverage — Orange,
Hillsborough, and the remaining South Florida interior counties next
(highest establishment counts per DOH annual reports among unswept areas).
