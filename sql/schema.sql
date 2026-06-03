Create table dim_fund(
    amfi_code Text primary key,
    fund_house Text,
    scheme_name Text,
    category Text,
    sub_category Text,
);

create table fact_nav(
    amfi_code Text,
    nav_date Date,
    nav real,
    daily_return real,
    foreign key (amfi_code)
    references dim_fund(amfi_code)

);
create table fact_transaction(
    transaction_id integer primary key,
    investor_id text,
    amfi_code Text,
    transaction_date Date,
    transaction_type Text,
    amount_inr real,
    state text,
    city text,
    kyc_status text
);

create table fact_performance(
    amfi_code Text,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    sharpe_ratio REAL,
    expense_ratio_pct REAL,
    risk_grade TEXT,
    foreign key (amfi_code)
    references dim_fund(amfi_code)
);
