import pandas as pd

routing_rules = pd.read_csv(
    "data/routing_rules.csv",
    sep="\t"
)

routing_rules.columns = routing_rules.columns.str.strip()