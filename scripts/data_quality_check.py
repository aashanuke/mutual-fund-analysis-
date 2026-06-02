import pandas as pd

fund_master = pd.read_csv("../data/raw/01_fund_master.csv")
nav_history = pd.read_csv("../data/raw/02_nav_history.csv")

print("=" * 60)
print("DATA QUALITY VALIDATION")
print("=" * 60)

print("\nFund Master Shape:")
print(fund_master.shape)

print("\nNAV History Shape:")
print(nav_history.shape)

print("\nMissing Values in Fund Master:")
print(fund_master.isnull().sum())

print("\nMissing Values in NAV History:")
print(nav_history.isnull().sum())

missing_codes = fund_master[
    ~fund_master['amfi_code'].isin(nav_history['amfi_code'])
]
print("\nChecking AMFI Code Consistency...")
if len(missing_codes) == 0:
    print("\nAll AMFI codes exist in NAV history")
else:
    print("\nMissing AMFI Codes Found:")
    print(missing_codes[['amfi_code']])
report_path = "../reports/data_quality_report.txt"
with open(report_path, "w") as f:
    f.write("DATA QUALITY REPORT\n")
    f.write("=" * 50 + "\n\n")
    f.write(f"Fund Master Shape: {fund_master.shape}\n")
    f.write(f"NAV History Shape: {nav_history.shape}\n\n")
    f.write("Missing Values in Fund Master:\n")
    f.write(str(fund_master.isnull().sum()))
    f.write("\n\nMissing Values in NAV History:\n")
    f.write(str(nav_history.isnull().sum()))
    if len(missing_codes) == 0:
        f.write("\n\nAll AMFI codes exist in NAV history")
    else:
        f.write("\n\nMissing AMFI Codes:\n")
        f.write(str(missing_codes[['amfi_code']]))
print(f"\nReport saved to: {report_path}")