import requests
import pandas as pd
import os
schemes = {
    "HDFC_Top_100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}
output_folder = "../data/raw"
os.makedirs(output_folder, exist_ok=True)
for scheme_name, scheme_code in schemes.items():
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    print(f"\nFetching data for {scheme_name}")
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        nav_data = data.get("data", [])
        df = pd.DataFrame(nav_data)
        output_file = f"{output_folder}/{scheme_name}_NAV.csv"
        df.to_csv(output_file, index=False)
        print(f"Saved: {output_file}")
    else:
        print(f"Failed to fetch {scheme_name}")