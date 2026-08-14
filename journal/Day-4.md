# Day 4 — Aug 13, 2026

**Goal:** Add a second monitored host to confirm detection rules generalize across endpoints, not just a single host.

## What I did
- Tried a Windows 11 VM on Proxmox first, but it got hung up on boot, so switched to Ubuntu instead.
- Hit repeated `no space left on device` errors installing Elastic Agent, despite a 42GB disk. Root cause: the VM was booting into Ubuntu's **live/try session** (a 1.5GB temp filesystem), not an actual install — "Try or Install Ubuntu" only opens a live desktop, and I kept missing the separate "Install Ubuntu" icon needed to actually install.
- Also hit and fixed an unrelated SSH "host key changed" warning on Windows (stale `known_hosts` entry from earlier failed attempts).
- Once properly installed, enrolled Elastic Agent on the Ubuntu VM (`lwubuntu`) into a new policy (`ubuntu-lab-2`) — confirmed Healthy in Fleet.
- Ran `nmap` **from Ubuntu targeting Kali**, simulating host-to-host scanning instead of isolated single-host activity.
- Confirmed in Discover that both `kali` and `lwubuntu` generated nmap events, and the existing "Nmap Scan Detected" rule fired for the new host **with no rule changes needed** — proving the detection logic generalizes rather than being hardcoded to one host.

## Screenshots
1. `screenshots/day4/discover-multihost-events.png` — Discover showing nmap events from both `kali` and `lwubuntu`
2. `screenshots/day4/alerts-multihost-nmap.png` — Alerts page showing the rule firing for both hosts

## Lesson learned
Most of today was infrastructure troubleshooting, not Elastic-specific work. This was a helpful and realistic reminder that SOC/lab environments involve as much systems administration as security tooling. I also confirmed a real detection-engineering principle: a rule written generically (on process/event attributes, not host-specific values) requires zero changes to cover newly enrolled endpoints.
