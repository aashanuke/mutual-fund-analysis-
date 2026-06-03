select
    strftime('%Y-%m', created_at) as date,
    avg(nav) as avg_nav
from fact_nav
group by month 
order by month;

select
    state,
    count(*) as total_transactions
from fact_transaction
group by state
order by total_transactions desc;

select
    amfi_code,
    return_1yr_pct
from fact_performance
order by return_1yr_pct desc
limit 5;

select
    avg(Amount_inr) as avg_transaction_amount
from fact_transaction;

select
    kyc_status,
    count(*) as total
from fact_transaction
group by kyc_status;

select
    transaction_type,
    count(*) as total
from fact_transaction
group by transaction_type;

select
    amfi_code,
    sharpe_ratio
from fact_performance
order by sharpe_ratio desc
limit 5;

select
    avg(expense_ratio_pct) as avg_expense_ratio
from fact_performance;

select
    risk_grade,
    count(*) as total
from fact_performance
group by risk_grade;


