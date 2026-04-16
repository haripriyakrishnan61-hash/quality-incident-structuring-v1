import streamlit as st

st.title("Quality Incident Structuring Tool")

# Input box
user_input = st.text_area("Enter issue description:")

# Simple rule-based classification
def classify_issue(issue):
    issue = issue.lower()

    if "temperature" in issue or "transport" in issue or "shipment" in issue:
        return "Logistics / Distribution"
    elif "packaging" in issue or "label" in issue:
        return "Packaging / Labeling"
    elif "malfunction" in issue or "defect" in issue:
        return "Product / Manufacturing"
    elif "supplier" in issue:
        return "Supplier Issue"
    elif "complaint" in issue:
        return "Post-Market"
    else:
        return "Quality / Compliance"

# Generate report
def generate_report(issue):
    issue_type = classify_issue(issue)

    return f"""
### General Information
- Issue Type: {issue_type}
- Source: Internal / External

### Problem Description
- Observation: {issue}
- Requirement Violated: To be determined

### Risk Assessment
- Severity: Medium
- Patient Impact: Medium

### Actions
- Immediate Containment: Under evaluation
- Recommended Corrective Action: Investigation required

### Status
- Open
"""

# Button logic
if st.button("Generate Report"):
    if user_input.strip() == "":
        st.warning("Please enter an issue description.")
    else:
        report = generate_report(user_input)
        st.markdown(report)
