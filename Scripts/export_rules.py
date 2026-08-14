"""
export_rules.py

Exports Elastic Security detection rules via the Kibana Detection Engine API,
instead of using the Kibana UI's manual export flow.

Setup:
    pip install requests

Usage:
    1. Fill in KIBANA_URL and API_KEY below.
    2. Run: python export_rules.py
    3. Output is saved to rules_api_export.ndjson in the current directory.
"""

import requests

# --- Configuration ---
KIBANA_URL = "https://liam-kali-project-f93e8f.kb.us-central1.gcp.elastic.cloud" # no trailing slash
API_KEY = "my-API-key"  # from Stack Management -> API keys

# --- Request setup ---
headers = {
    "Authorization": f"ApiKey {API_KEY}",
    "kbn-xsrf": "true",
    "Content-Type": "application/json",
}

# Detection Engine's rule export endpoint. Passing no rule_id filters
# exports all rules; you can add ?exclude_export_details=true too.
url = f"{KIBANA_URL}/api/detection_engine/rules/_export"

def main():
    response = requests.post(url, headers=headers)

    if response.status_code != 200:
        print(f"Request failed: {response.status_code}")
        print(response.text)
        return

    output_file = "rules_api_export.ndjson"
    with open(output_file, "wb") as f:
        f.write(response.content)

    print(f"Export successful. Saved to {output_file}")
    print("--- Preview of first 300 characters ---")
    print(response.text[:300])

if __name__ == "__main__":
    main()
