import pandas as pd 
from sqlalchemy import create_engine
engine = create_engine('sqlite:///bluestock_mf.db')
print("database created")
nav= pd.read_csv("data/processed/clean_nav.csv")
nav.to_sql("fact_nav",
           engine,
           if_exists="replace",
           index=False
)

print("fact_nav loaded")

inv = pd.read_csv("data/processed/clean_transactions.csv")
inv.to_sql("fact_transactions",
              engine,
              if_exists="replace",
              index=False
)
print("fact_transactions loaded")  

perf = pd.read_csv("data/processed/clean_performance.csv")
perf.to_sql("fact_performance",
              engine,
              if_exists="replace",
              index=False
)
print("fact_performance loaded")
print("\nAll datasets loaded successfully.")

