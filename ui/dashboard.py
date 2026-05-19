import streamlit as st
import re
import pandas as pd

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="AI RTL Optimizer",
    layout="wide"
)

# -----------------------------------
# TITLE
# -----------------------------------

st.title("AI RTL Optimizer")

st.write("AI-Assisted RTL Analysis and Optimization Tool")

# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.header("Tool Information")

st.sidebar.write("""
Features:
- RTL Parsing
- Timing Analysis
- Optimization Suggestions
- ML Delay Estimation
- RTL Complexity Scoring
- RTL Quality Grading
""")

# -----------------------------------
# FILE UPLOAD
# -----------------------------------

uploaded_file = st.file_uploader(
    "Upload Verilog RTL File",
    type=["v"]
)

# -----------------------------------
# MAIN ANALYSIS
# -----------------------------------

if uploaded_file is not None:

    # Read RTL code
    code = uploaded_file.read().decode("utf-8")

    # -----------------------------------
    # DISPLAY RTL CODE
    # -----------------------------------

    st.subheader("RTL Code")

    st.code(code, language="verilog")

    # -----------------------------------
    # MODULE NAME
    # -----------------------------------

    module = re.search(r'module\s+(\w+)', code)

    if module:
        st.success(f"Module Detected: {module.group(1)}")

    # -----------------------------------
    # FEATURE EXTRACTION
    # -----------------------------------

    adders = code.count("+")
    multipliers = code.count("*")
    ands = code.count("&")
    ors = code.count("|")

    operators = re.findall(r'[\+\-\*/&|]', code)

    # -----------------------------------
    # RTL METRICS
    # -----------------------------------

    st.subheader("RTL Metrics")

    metrics = {
        "Adders": adders,
        "Multipliers": multipliers,
        "AND Gates": ands,
        "OR Gates": ors
    }

    df = pd.DataFrame(
        metrics.items(),
        columns=["Metric", "Count"]
    )

    st.table(df)

    # -----------------------------------
    # RTL ANALYSIS
    # -----------------------------------

    st.subheader("RTL Analysis")

    st.write("Operators Found:", operators)

    if "*" in operators:
        st.warning("Multiplier detected")

    if len(operators) >= 2:
        st.warning("Complex combinational path detected")

    # -----------------------------------
    # OPTIMIZATION SUGGESTIONS
    # -----------------------------------

    st.subheader("Optimization Suggestions")

    if "*" in operators:
        st.write("• Consider pipelining multiplier stage")
        st.write("• Use shift-add optimization if area is critical")

    if len(operators) >= 2:
        st.write("• Split combinational logic into stages")

    # -----------------------------------
    # ML DELAY PREDICTION
    # -----------------------------------

    st.subheader("ML Delay Prediction")

    estimated_delay = (adders * 2) + (multipliers * 5)

    st.info(f"Estimated Delay: {estimated_delay}")

    # -----------------------------------
    # RTL COMPLEXITY SCORE
    # -----------------------------------

    st.subheader("RTL Complexity Score")

    complexity_score = (
        (adders * 10) +
        (multipliers * 25) +
        (len(operators) * 5)
    )

    # Limit score to 100
    if complexity_score > 100:
        complexity_score = 100

    st.progress(complexity_score / 100)

    st.success(f"Complexity Score: {complexity_score}/100")

    # -----------------------------------
    # RTL QUALITY GRADE
    # -----------------------------------

    st.subheader("RTL Quality Grade")

    if complexity_score < 20:
        grade = "A"

    elif complexity_score < 40:
        grade = "B"

    elif complexity_score < 60:
        grade = "C"

    else:
        grade = "D"

    st.info(f"RTL Quality Grade: {grade}")

    # -----------------------------------
    # RTL OPERATOR DISTRIBUTION
    # -----------------------------------

    st.subheader("RTL Operator Distribution")

    chart_data = pd.DataFrame({
        "Operator": ["Adders", "Multipliers", "AND", "OR"],
        "Count": [adders, multipliers, ands, ors]
    })

    st.bar_chart(
        chart_data.set_index("Operator")
    )

    # -----------------------------------
    # REPORT GENERATION
    # -----------------------------------

    report = f"""
===================================
        RTL ANALYSIS REPORT
===================================

Module Name:
{module.group(1)}

-----------------------------------
RTL METRICS
-----------------------------------

Adders          : {adders}
Multipliers     : {multipliers}
AND Gates       : {ands}
OR Gates        : {ors}

-----------------------------------
ANALYSIS
-----------------------------------

Operators Found : {operators}

Estimated Delay : {estimated_delay}

Complexity Score: {complexity_score}/100

RTL Grade       : {grade}

-----------------------------------
OPTIMIZATION SUGGESTIONS
-----------------------------------
"""

    if "*" in operators:
        report += "\n- Consider pipelining multiplier stage"

    if len(operators) >= 2:
        report += "\n- Split combinational logic into stages"

    # -----------------------------------
    # DISPLAY REPORT
    # -----------------------------------

    st.subheader("Generated Report")

    st.text(report)

    # -----------------------------------
    # DOWNLOAD BUTTON
    # -----------------------------------

    st.download_button(
        label="Download Report",
        data=report,
        file_name="rtl_report.txt",
        mime="text/plain"
    )