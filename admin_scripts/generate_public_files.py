#!/usr/bin/env python3
"""
FED-SPA public file generator.

Fans the single source of truth out to every platform that bundles or fetches
data. Run after editing data/public/licensed.json:

  python3 admin_scripts/generate_public_files.py

What it does:
  1. web/data/licensed.json          full list (fetched at runtime by the PWA)
  2. web/data/unlicensed.encrypted.json  subscriber blob for the PWA
  3. web/data/licensed.csv           CSV export of the licensed list (stdlib csv)
  4. extension/data/*                same two JSON files, bundled into the zip
  5. android/app/src/main/assets/data/*        full list + encrypted blob
  6. android_auto/app/src/main/assets/data/licensed.json   licensed only
  7. watch/app/src/main/assets/data/licensed.json          licensed only
  8. ios/Resources/Data/*             full list + encrypted blob
  9. <repo-root>/data/*               GitHub-Pages mirror of the web copies
                                     (root index.html is the Pages entry;
                                     before the 2026.2 refresh this copy
                                     silently drifted to the seed record)

Admin-only fields (verified_by, raw source notes) are stripped from the
generated copies; the repo originals keep everything.

The CSV export covers the ROADMAP's most-requested "give me the data" format
as a generated static file (no backend, no third-party code - stdlib csv).
It ships to web/data/ and the root data/ mirror (the two download surfaces).
"""

import csv
import io
import json
import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

STRIP_FIELDS = ["verified_by"]
ADMIN_ONLY_NOTE = "Do not edit generated files. Edit data/public/licensed.json and run generate_public_files.py."

SOURCE_LIC = ROOT / "data" / "public" / "licensed.json"
SOURCE_ENC = ROOT / "data" / "private" / "unlicensed.encrypted.json"
CSV_PATH = ROOT / "web" / "data" / "licensed.csv"
ROOT_DATA_MIRROR = ROOT / "data"   # GitHub-Pages mirror of web/data (see header)

CSV_COLUMNS = [
    "license_number", "business_name", "profession", "status",
    "expiration_date", "original_issue_date",
    "street", "street2", "city", "state", "zip",
    "county", "discipline_on_file", "public_complaint",
    "data_as_of", "last_checked", "notes",
]

DESTS = [
    # (target dir, licensed, encrypted unlicensed)
    (ROOT / "web" / "data", True, True),
    (ROOT / "extension" / "data", True, True),
    (ROOT / "android" / "app" / "src" / "main" / "assets" / "data", True, True),
    (ROOT / "android_auto" / "app" / "src" / "main" / "assets" / "data", True, False),
    (ROOT / "watch" / "app" / "src" / "main" / "assets" / "data", True, False),
    (ROOT / "ios" / "Resources" / "Data", True, True),
    # repo-root mirror: root index.html/js/css are the GitHub-Pages copies
    # and load ./data/licensed.json - kept byte-identical to web/data by
    # the fan-out so Pages never serves a stale dataset again
    (ROOT_DATA_MIRROR, True, True),
]


def flatten_row(p: dict) -> dict:
    """Flatten a parlor record into CSV columns (address.* -> flat keys)."""
    addr = p.get("address") or {}
    return {
        "license_number": p.get("license_number", ""),
        "business_name": p.get("business_name", ""),
        "profession": p.get("profession", ""),
        "status": p.get("status", ""),
        "expiration_date": p.get("expiration_date") or "",
        "original_issue_date": p.get("original_issue_date") or "",
        "street": addr.get("street") or "",
        "street2": addr.get("street2") or "",
        "city": addr.get("city") or "",
        "state": addr.get("state") or "",
        "zip": addr.get("zip") or "",
        "county": p.get("county", ""),
        "discipline_on_file": p.get("discipline_on_file", ""),
        "public_complaint": p.get("public_complaint", ""),
        "data_as_of": p.get("data_as_of") or "",
        "last_checked": p.get("last_checked") or "",
        "notes": p.get("notes") or "",
    }


def generate_csv(doc: dict) -> str:
    """Render the licensed list as CSV (stdlib csv module, same source doc)."""
    rows = [flatten_row(p) for p in doc.get("parlors", [])]
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=CSV_COLUMNS, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
    return buf.getvalue()


def main() -> int:
    if not SOURCE_LIC.exists():
        print(f"[x] Missing {SOURCE_LIC}")
        return 1
    doc = json.loads(SOURCE_LIC.read_text())

    # Strip admin-only fields from the distribution copy.
    parlors = []
    for p in doc.get("parlors", []):
        q = {k: v for k, v in p.items() if k not in STRIP_FIELDS}
        parlors.append(q)
    public = {
        "version": doc.get("version", 1),
        "as_of": doc.get("as_of", date.today().isoformat()),
        "update_frequency": doc.get("update_frequency", "annual"),
        "source_url": doc.get("source_url", ""),
        "parlors": parlors,
        "generated_note": ADMIN_ONLY_NOTE,
    }

    enc_exists = SOURCE_ENC.exists()
    enc_is_placeholder = False
    envelope = None
    if enc_exists:
        envelope = json.loads(SOURCE_ENC.read_text())
        enc_is_placeholder = not envelope.get("data")

    written = 0
    for dest, want_lic, want_enc in DESTS:
        if want_lic:
            dest.mkdir(parents=True, exist_ok=True)
            (dest / "licensed.json").write_text(json.dumps(public, indent=2) + "\n")
            written += 1
        if want_enc:
            dest.mkdir(parents=True, exist_ok=True)
            if enc_exists and not enc_is_placeholder:
                shutil.copyfile(SOURCE_ENC, dest / "unlicensed.encrypted.json")
                written += 1
            else:
                # Keep a placeholder so every consumer can code against the
                # same filename before the first real blob exists.
                (dest / "unlicensed.encrypted.json").write_text(
                    json.dumps(
                        {"v": 1, "kdf": "PBKDF2-SHA256", "iterations": 310000,
                         "salt": "", "iv": "", "data": "",
                         "note": "placeholder - run admin_scripts/encrypt_unlicensed.js"},
                        indent=2,
                    )
                    + "\n"
                )
                written += 1

    # CSV export of the licensed list (ROADMAP "give me the data" item).
    # web/data/ is the download surface; JSON parity is checked by CI drift.
    csv_text = generate_csv(doc)
    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    CSV_PATH.write_text(csv_text)
    (ROOT_DATA_MIRROR / "licensed.csv").write_text(csv_text)
    written += 2
    print(f"[+] CSV export -> web/data/licensed.csv + data/licensed.csv ({len(parlors)} rows)")

    print(f"[+] Generated {written} file(s) across {len(DESTS)} platform destinations.")
    print("    Admin-only fields stripped from distribution copies.")
    if enc_is_placeholder:
        print("    NOTE: unlicensed blob is still the placeholder -")
        print("    run admin_scripts/encrypt_unlicensed.js once you have entries.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
