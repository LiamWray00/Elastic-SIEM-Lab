# Day 1 — Aug 10, 2026

**Goal:** Use my Elastic Security SIEM lab and detect simulated attacker activity end-to-end.

## What I did
- Created an Elastic Cloud account and provisioned a **Security-type project**
- Deployed a Kali Linux VM on Proxmox as the monitored endpoint; installed **Elastic Agent + Elastic Defend** (Traditional Endpoints, Complete EDR), enrolled it into my Fleet, and confirmed **Healthy** status.
- Generated attacker-style traffic with **Nmap** from Kali (`-sS`, `-sT`, full port scans).
- Verified telemetry in **Discover** via ES|QL (`FROM logs-* | WHERE process.name == "nmap"`) — confirmed processes and the network events captured.
- Built a custom **dashboard** ("Kali Lab Overview") visualizing event volume over time by process.
- Created a custom **detection rule** ("Nmap Scan Detected", KQL: `process.name: "nmap"`), enabled it, and confirmed real alerts fired with full attribution (host, user, process lineage, source/dest IP/port).
- Found the rule generated **104 alerts from a single scan**, hitting Kibana's per-execution alert cap — flagged as a tuning issue for Day 2.

## Screenshots
1. `fleet-agent-healthy.png` — Fleet → Agents: `kali` Healthy, `kali-lab-2` policy
2. `screenshots/day1/detection-rules-list.png` — Detection rules list: rule Enabled, Last response Succeeded
3. `104-alert-warning.png` — 104-alert warning (best screenshot — a real problem found, not just the happy path)
4. `events-over-time.png` — Dashboard: Events Over Time chart

## Lesson learned
Elastic Cloud project type matters — only a Security project includes the SIEM apps (Alerts, Detection rules, Cases). Also discovered that a broad rule query matching every network event per scanned port creates significant alert noise (104 alerts from one scan) — identified as a tuning target for Day 2.
