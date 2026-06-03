import pandas as pd 
nav = pd.read_csv("data/raw/02_nav_history.csv")
print("original shape: ")
print(nav.shape)
print(nav.head())

nav["date"] = pd.to_datetime(nav["date"], errors="coerce")
print(nav.dtypes)

nav = nav.sort_values(by=['amfi_code', 'date'])
print("\nData Sorted Successfully")
nav = nav.drop_duplicates()
print("\nDuplicates Removed")
print("Current Shape:", nav.shape)

nav["nav"]= nav["nav"].ffill()
print("\nMissing NAV values:")
print(nav["nav"].isnull().sum())

nav= nav[nav["nav"]>0]
print("\nvalid NAV records:")
print(nav.shape)

nav.to_csv("data/processed/clean_nav.csv", index=False)
print("\nclean_nav.csv saved successfully")

# CLEAN INVESTOR TRANSACTIONS

inv = pd.read_csv("data/raw/08_investor_transactions.csv")
print("\nOriginal Transaction Shape:")
print(inv.shape)
print("\nTransaction Columns:")
print(inv.columns)
print("\nFirst 5 Rows:")
print(inv.head())
print(inv.columns)
# Standardize transaction types
inv['transaction_type'] = (
    inv['transaction_type']
    .str.strip()
    .str.title()
)

print("\nUnique Transaction Types:")
print(inv['transaction_type'].unique())
inv['transaction_type'].unique()

valid_types = ['Sip', 'Lumpsum', 'Redemption']

inv = inv[
    inv['transaction_type'].isin(valid_types)
]

inv = inv[inv['amount_inr'] > 0]

print("\nTransaction Shape After Validation:")
print(inv.shape)

inv['transaction_date'] = pd.to_datetime(
    inv['transaction_date']
)

print("\nUpdated Transaction Data Types:")
print(inv.dtypes)

valid_kyc = ['Verified', 'Pending', 'Rejected']

inv = inv[
    inv['kyc_status'].isin(valid_kyc)
]

print("\nUnique KYC Status Values:")
print(inv['kyc_status'].unique())

print("\nFinal Transaction Shape:")
print(inv.shape)

inv.to_csv(
    "data/processed/clean_transactions.csv",
    index=False
)
print("\nclean_transactions.csv saved successfully")

#clean scheme performance 
perf = pd.read_csv("data/raw/07_scheme_performance.csv")
print("\nOriginal Performance Shape:"   )
print(perf.shape)
print("\nPerformance Columns:")
print(perf.columns)
print("\nFirst 5 Rows:")
print(perf.head())

return_cols = [
    'return_1yr_pct',
    'return_3yr_pct',
    'return_5yr_pct'
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors='coerce'
    )

print("\nUpdated Return Column Data Types:")
print(
    perf[return_cols].dtypes
)
# Flag negative Sharpe ratios
perf['negative_sharpe_flag'] = (
    perf['sharpe_ratio'] < 0
)

print("\nNegative Sharpe Ratio Count:")
print(
    perf['negative_sharpe_flag'].sum()
)
# Validate expense ratio range
perf = perf[
    (perf['expense_ratio_pct'] >= 0.1) &
    (perf['expense_ratio_pct'] <= 2.5)
]

print("\nPerformance Shape After Expense Ratio Validation:")
print(perf.shape)

perf.to_csv(
    "data/processed/clean_performance.csv",
    index=False
)
print("\nclean_performance.csv saved successfully")