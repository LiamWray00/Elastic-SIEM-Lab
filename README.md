Elastic SIEM Home Lab

A hands-on home lab simulating a small SOC environment: an endpoint monitored by Elastic Security, generating and detecting simulated attacker behavior (network reconnaissance and SSH brute-force).

Architecture
Kali Linux VM (endpoint)
   │  Elastic Agent + Elastic Defend (Complete EDR)
   ▼
Elastic Cloud — Security project
   │  Fleet (agent management)
   │  Discover (ES|QL/KQL querying)
   │  Dashboards (Lens visualizations)
   │  Detection Engine (custom + threshold rules)
   ▼
   
Alerts (triaged, attributed to host/user/process)
What I built
Deployed Elastic Agent with the Elastic Defend integration (Traditional Endpoints, Complete EDR preset) on a Kali Linux VM, enrolled via Fleet.
Queried live endpoint telemetry in Discover using ES|QL.
Built a dashboard visualizing process/network event volume over time.
Simulated and detected two attack scenarios:
Network reconnaissance (Nmap) — custom query rule (process.name: "nmap" and event.category: "process"), tuned after an initial version caused alert flooding (104 alerts → 2 alerts per scan).
SSH brute force (Hydra) — threshold rule (process.name: "sshd", ≥10 events per host in 5 minutes), since single sshd events are normal but a burst indicates an attack.
Verified rules using both live alerts and the rule execution history, confirming correct behavior (quiet when idle, firing precisely during attack windows).

Key screenshots

screenshots/day1/fleet-agent-healthy.png	Elastic Agent enrolled and healthy on Kali
screenshots/day1/discover-nmap-events.png	Nmap process/network events captured in Discover
screenshots/day1/alert-flood-104.png	Initial rule hitting Kibana's per-execution alert cap (104 alerts from one scan)
screenshots/day2/nmap-rule-tuned.png	Tuned rule: same scan, 2 alerts instead of 104
screenshots/day2/hydra-throttled.png	Hydra brute-force attempt, throttled by SSH's connection protection
screenshots/day2/discover-sshd-burst.png	695 sshd process events captured during the attack
screenshots/day2/threshold-rule-definition.png	SSH Brute Force Detected — threshold rule config
screenshots/day2/execution-log.png	Rule execution history: 0 alerts when idle, 1 alert during the actual attack window
