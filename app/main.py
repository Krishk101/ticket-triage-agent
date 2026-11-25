from classifier import classify_ticket
from priority import calculate_priority


def main():
    subject = "VPN not connecting"
    description = "Unable to connect to corporate VPN after password change"

    classification = classify_ticket(subject, description)

    impact = "Medium"
    urgency = "High"

    priority = calculate_priority(impact, urgency)

    response = {
        **classification,
        "impact": impact,
        "urgency": urgency,
        "priority": priority,
    }

    print("\n=== Ticket Analysis ===")
    print(response)


if __name__ == "__main__":
    main()