import streamlit as st
import pandas as pd

st.set_page_config(page_title="DockIQ", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("dock_capacity_recommendations.csv")

df = load_data()

st.title("🚲 DockIQ – BlueBikes Dock Capacity Recommendation Engine")

st.markdown("""
**DockIQ** is a prescriptive analytics tool that helps city planners and BlueBikes
operations teams decide **where to add dock capacity** based on historical demand imbalance.
""")

st.subheader("📊 Recommended Dock Expansions")
st.dataframe(
    df[['station', 'dock_pressure_score', 'recommended_docks']]
      .sort_values('dock_pressure_score', ascending=False),
    use_container_width=True
)

st.markdown("""
### 🔍 How to read this
- **Dock Pressure Score** combines peak deficits and frequency of shortages  
- **Recommended Docks** translates pressure into concrete action
""")

st.caption("Built with BlueBikes open data • Prescriptive analytics project (ISOM 839)")