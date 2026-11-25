import pandas as pd

priority_rules = pd.read_csv(
    "data/priority_rules.csv",
    sep="\t"
)

priority_rules.columns = priority_rules.columns.str.strip()


def calculate_priority(impact, urgency):
    result = priority_rules[
        (priority_rules["Impact"] == impact)
        & (priority_rules["Urgency"] == urgency)
    ]

    if not result.empty:
        return result.iloc[0]["Priority"]

    return "P4"