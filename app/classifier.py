import pandas as pd

routing_rules = pd.read_csv(
    "data/routing_rules.csv",
    sep="\t"
)

routing_rules.columns = routing_rules.columns.str.strip()


def classify_ticket(subject, description):
    text = f"{subject} {description}".lower()

    for _, rule in routing_rules.iterrows():
        keyword = str(rule["Keyword"]).lower()

        if keyword in text:
            return {
                "category": rule["Category"],
                "subcategory": rule["Subcategory"],
                "assignment_group": rule["AssignmentGroup"]
            }

    return {
        "category": "Unknown",
        "subcategory": "Unknown",
        "assignment_group": "Service Desk"
    }