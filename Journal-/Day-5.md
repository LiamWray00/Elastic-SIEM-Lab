# Day 5 — Aug 14, 2026

**Goal:** Export detection rules programmatically via Kibana's API instead of the manual UI export, to demonstrate scripted interaction with the platform.

## What I did
- Created a dedicated Kibana **API key** (Stack Management → API keys) scoped for this task rather than reusing personal login credentials.
- Wrote a short Python script (`export_rules.py`) using the `requests` library to call Kibana's Detection Engine API (`/api/detection_engine/rules/_export`) and pull all detection rules as NDJSON.
- Ran the script locally (`pip install requests`, then `python export_rules.py`) and confirmed a successful export: 3 rules returned — **SSH Brute Force Detected**, **Nmap Scan Detected**, and the built-in **Endpoint Security (Elastic Defend)** rule — saved to `rules_api_export.ndjson`.
- Before publishing, scanned the exported file for sensitive fields (passwords, tokens, connectors, credentials) to confirm it was safe to make public — confirmed clean, since no rule has an action/connector attached.
- Removed the real API key from the script and replaced it with a placeholder before uploading it publicly.
- Uploaded both the script and its output to the repo (`scripts/export_rules.py`, `rules/rules_api_export.ndjson`).

## Lesson learned
The Kibana UI's Saved Objects export doesn't work for detection rules (they're excluded by type, discovered on Day 3), but the Detection Engine's own REST API exports them cleanly and can be automated. This is a more realistic, repeatable way to manage rules-as-config than manual UI export, and is the kind of small script a detection engineering workflow would use for backups, version control, or CI/CD rather than relying on manual clicks.
