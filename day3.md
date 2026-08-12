# Day 3 — Aug 12, 2026

**Goal:** Move from detection to investigation — use Elastic Security's Timeline feature to triage the SSH brute-force alert, rather than just confirming it fired.

## What I did
- Located the "SSH Brute Force Detected" alerts from Day 2 (initially not visible under the default "Last 24 hours" filter — had to widen the Alerts time range and check the Open/Acknowledged/Closed status tabs to find them).
- Opened **Investigate in Timeline** on one of the alerts, which auto-populated a scoped query (`process.name: "sshd"`, filtered to `host.name: "kali"`) across the relevant time window.
- Reviewed the resulting 75 correlated events using Timeline's **event renderers** — human-readable narrative lines (e.g. "root @ kali forked process sshd via parent process sshd with result unknown") instead of raw JSON.
- Confirmed the process lineage behind the brute-force detection: the main `sshd` listener process repeatedly forking a new child `sshd` process per incoming connection attempt — the process-level signature of a brute-force attack.
- Checked the **Correlation** tab (EQL sequence queries) — empty by default, since it requires a defined multi-step event sequence rather than a plain field query; noted as a possible future exercise rather than something to force today.

## Screenshots
1. `screenshots/day3/timeline-ssh-bruteforce-investigation.png` — Timeline view showing the correlated sshd process events and readable narrative for the brute-force alert

## Lesson learned
Detection (a rule firing) and investigation (understanding what actually happened) are different skills supported by different tooling. Elastic Security's Timeline pulls in correlated context automatically from an alert and renders raw process/network events into readable narratives, which is closer to what a SOC analyst actually does during triage than just reading an alert's summary line. Also learned that alerts can silently drop out of view under narrow default time filters — worth checking both the time range and status tabs (Open/Acknowledged/Closed) before assuming data is missing.

