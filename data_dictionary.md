# Mutual Fund Analytics — Data Dictionary

---

# 1. clean_nav.csv

| Column | Data Type | Description |
|---|---|---|
| amfi_code | INTEGER | Unique AMFI mutual fund identifier |
| date | DATETIME | NAV date |
| nav | FLOAT | Net Asset Value of fund |

Source: 02_nav_history.csv

---

# 2. clean_transactions.csv

| Column | Data Type | Description |
|---|---|---|
| investor_id | TEXT | Unique investor identifier |
| transaction_date | DATETIME | Transaction date |
| amfi_code | INTEGER | Mutual fund AMFI code |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | FLOAT | Transaction amount in INR |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | Tier classification |
| age_group | TEXT | Investor age category |
| gender | TEXT | Investor gender |
| annual_income_lakh | FLOAT | Annual income in lakhs |
| payment_mode | TEXT | UPI / Net Banking / etc |
| kyc_status | TEXT | KYC verification status |

Source: 08_investor_transactions.csv

---

# 3. clean_performance.csv

| Column | Data Type | Description |
|---|---|---|
| amfi_code | INTEGER | Mutual fund AMFI code |
| scheme_name | TEXT | Mutual fund scheme name |
| fund_house | TEXT | AMC / fund house |
| category | TEXT | Fund category |
| plan | TEXT | Direct / Regular |
| return_1yr_pct | FLOAT | 1 year return percentage |
| return_3yr_pct | FLOAT | 3 year return percentage |
| return_5yr_pct | FLOAT | 5 year return percentage |
| benchmark_3yr_pct | FLOAT | Benchmark return |
| alpha | FLOAT | Alpha metric |
| beta | FLOAT | Beta metric |
| sharpe_ratio | FLOAT | Risk-adjusted return metric |
| sortino_ratio | FLOAT | Downside risk metric |
| std_dev_ann_pct | FLOAT | Annualized standard deviation |
| max_drawdown_pct | FLOAT | Maximum drawdown percentage |
| aum_crore | FLOAT | Assets under management |
| expense_ratio_pct | FLOAT | Expense ratio percentage |
| morningstar_rating | INTEGER | Fund rating |
| risk_grade | TEXT | Fund risk classification |
| negative_sharpe_flag | BOOLEAN | Indicates negative Sharpe ratio |

Source: 07_scheme_performance.csv