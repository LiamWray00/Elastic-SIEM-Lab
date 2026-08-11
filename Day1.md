Day 1 — Aug 10, 2026

Goal: Stand up an Elastic Security SIEM lab and detect simulated attacker activity end-to-end.

What I did
Created an Elastic Cloud trial and provisioned a Security-type project (first attempt used a plain Elasticsearch project — no Alerts/Rules pages exist there — recreated correctly as a Security project).

Deployed a Kali Linux VM as the monitored endpoint; installed Elastic Agent + Elastic Defend (Traditional Endpoints, Complete EDR), enrolled it into Fleet, confirmed Healthy status.

Generated attacker-style traffic with Nmap (-sS, -sT, full port scans).
Verified telemetry in Discover via ES|QL (FROM logs-* | WHERE process.name == "nmap") — confirmed process + network events captured.

Built a custom dashboard ("Kali Lab Overview") visualizing event volume over time by process.

Authored a custom detection rule ("Nmap Scan Detected", KQL: process.name: "nmap"), enabled it, confirmed real alerts fired with full attribution (host, user, process lineage, source/dest IP/port).

Found the rule generated 104 alerts from a single scan, hitting Kibana's per-execution alert cap — flagged as a tuning issue for Day 2.

Screenshots
screenshots/day1/fleet-agent-healthy.png — Fleet → Agents: kali Healthy, kali-lab-2 policy
screenshots/day1/discover-nmap-events.png — Discover: nmap process/network events
screenshots/day1/alerts-summary-clean.png — Alerts summary: 4 alerts, clean scan
screenshots/day1/detection-rules-list.png — Detection rules list: rule Enabled, Last response Succeeded
screenshots/day1/alert-flood-104.png — 104-alert warning (best screenshot — a real problem found, not just the happy path)
screenshots/day1/dashboard-events-over-time.png — Dashboard: Events Over Time chart
Lesson learned

Elastic Cloud project type matters — only a Security project includes the SIEM apps (Alerts, Detection rules, Cases). Also discovered that a broad rule query matching every network event per scanned port creates significant alert noise (104 alerts from one scan)
