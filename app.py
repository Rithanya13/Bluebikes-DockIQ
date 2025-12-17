import streamlit as st
import pandas as pd

import streamlit as st
import pandas as pd

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(
    page_title="DockIQ",
    layout="wide"
)

# -------------------------------
# Dark theme (black background)
# -------------------------------
st.markdown(
    """
    <style>
    /* Main background */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }

    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff;
    }

    /* Tables */
    .stDataFrame {
        background-color: #0e1117;
    }

    /* Sidebar (if used later) */
    section[data-testid="stSidebar"] {
        background-color: #0e1117;
    }

    /* Markdown text */
    p, li, span {
        color: #e6e6e6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------------
# Page configuration
# -------------------------------------------------------
st.set_page_config(
    page_title="DockIQ – BlueBikes Dock Capacity Recommendations",
    layout="wide"
)

# -------------------------------------------------------
# Load data (cached for performance)
# -------------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("dock_capacity_recommendations.csv")

df = load_data()

# -------------------------------------------------------
# Title & description
# -------------------------------------------------------
st.title("🚲 DockIQ – BlueBikes Dock Capacity Recommendation Engine")

st.markdown("""
**DockIQ** is a **prescriptive analytics tool** that supports city planners and
BlueBikes operations teams by translating **historical demand imbalance**
into **actionable dock capacity recommendations**.

This application does **not** tune parameters or simulate scenarios.
All prescriptive logic is executed programmatically, and the app
presents the **final recommended actions**.
""")

# -------------------------------------------------------
# Focus on top priority stations
# -------------------------------------------------------
TOP_N = 10

top_df = (
    df[['station', 'dock_pressure_score', 'recommended_docks']]
    .sort_values('dock_pressure_score', ascending=False)
    .head(TOP_N)
)

st.subheader("📊 Recommended Dock Expansions (Top 10 Priority Stations)")

st.dataframe(
    top_df,
    use_container_width=True
)

# -------------------------------------------------------
# Decision logic visualization
# -------------------------------------------------------
st.subheader("📈 Decision Logic: Dock Pressure → Capacity Expansion")

st.markdown("""
This chart shows how **dock pressure** is translated into **discrete expansion decisions**.
Stations experiencing more frequent and severe shortages receive larger
recommended dock additions.
""")

st.scatter_chart(
    top_df,
    x="dock_pressure_score",
    y="recommended_docks"
)

# -------------------------------------------------------
# Interpretation guide
# -------------------------------------------------------
st.markdown("""
### 🔍 How to read this output
- **Dock Pressure Score** combines:
  - Peak bike shortages
  - Frequency of deficit hours
- **Recommended Docks** converts pressure into **concrete operational action**
- Only the **highest-priority stations** are shown to support realistic planning decisions
""")

# -------------------------------------------------------
# Footer
# -------------------------------------------------------
st.caption(
    "Built with BlueBikes open data • Prescriptive analytics project (ISOM 839)"
)