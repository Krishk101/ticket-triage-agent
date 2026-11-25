import streamlit as st
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "app"))

from classifier import classify_ticket
from priority import calculate_priority

st.set_page_config(
    page_title="Ticket Triage Agent",
    page_icon="🎫"
)

st.title("🎫 Ticket Triage Agent")

subject = st.text_input("Subject")

description = st.text_area(
    "Description",
    height=150
)

impact = st.selectbox(
    "Impact",
    ["Low", "Medium", "High"]
)

urgency = st.selectbox(
    "Urgency",
    ["Low", "Medium", "High"]
)

if st.button("Analyze Ticket"):

    classification = classify_ticket(
        subject,
        description
    )

    priority = calculate_priority(
        impact,
        urgency
    )

    result = {
        **classification,
        "impact": impact,
        "urgency": urgency,
        "priority": priority
    }

    st.success("Ticket Processed")

    st.json(result)