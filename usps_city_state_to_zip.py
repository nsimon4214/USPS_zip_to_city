import pandas as pd
import requests
import time
import os

# --- Prompt for input file ---
input_filename = input("Enter the name of your input CSV file (e.g. input.csv): ").strip()

# Validate input
if not os.path.isfile(input_filename):
    print(f"❌ File not found: {input_filename}")
    exit(1)

# Normalize headers
df = pd.read_csv(input_filename)
df.columns = df.columns.str.strip().str.lower()  # expects 'state', 'city'

# Prepare output filename
base_name = os.path.splitext(os.path.basename(input_filename))[0]
output_filename = f"{base_name}_results.csv"

# USPS API details
url = "https://tools.usps.com/tools/app/ziplookup/zipByCityState"
headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0"
}

results = []
delay = 0.25  # initial delay

for index, row in df.iterrows():
    city = row["city"]
    state = row["state"]

    print(f"[{index + 1}/{len(df)}] Looking up ZIPs for: {city}, {state} (delay: {delay:.2f}s)")

    data = {
        "city": city,
        "state": state
    }

    try:
        response = requests.post(url, headers=headers, data=data, timeout=10)
        response.raise_for_status()
        json_data = response.json()

        if json_data.get("resultStatus") == "SUCCESS":
            zip_list = json_data.get("zipList", [])
            if zip_list:
                for z in zip_list:
                    results.append({
                        "state": state,
                        "city": city,
                        "zip_code": z["zip5"]
                    })
            else:
                results.append({
                    "state": state,
                    "city": city,
                    "zip_code": "NOT FOUND"
                })

            # 🟢 Success: try reducing delay slightly (but not below 0.1s)
            delay = max(0.1, delay - 0.05)

        else:
            results.append({
                "state": state,
                "city": city,
                "zip_code": "NOT FOUND"
            })
            delay = min(delay + 0.25, 5.0)  # ⚠️ Slightly slow down

    except requests.exceptions.Timeout:
        print(f"⏱️ Timeout for {city}, {state}")
        results.append({
            "state": state,
            "city": city,
            "zip_code": "TIMEOUT"
        })
        delay = min(delay + 0.5, 5.0)  # ❌ Increase delay

    except Exception as e:
        print(f"🔥 Error with {city}, {state}: {e}")
        results.append({
            "state": state,
            "city": city,
            "zip_code": "ERROR"
        })
        delay = min(delay + 0.5, 5.0)  # ❌ Increase delay

    time.sleep(delay)

# Save results
pd.DataFrame(results).to_csv(output_filename, index=False)
print(f"\n✅ Done! Results saved to '{output_filename}'")
