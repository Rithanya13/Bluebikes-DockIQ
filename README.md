# 🚲 DockIQ — Prescriptive Dock Capacity Recommendations for BlueBikes

**Course:** ISOM 839 – Prescriptive Analytics  
**Program:** MS in Business Analytics, Suffolk University  
**Author:** Rithanya Chandran  

DockIQ is a **prescriptive analytics decision-support system** that recommends **where and how much bike dock capacity should be added** within the BlueBikes network, based on historically observed demand imbalance patterns.

The project moves beyond describing usage patterns and instead delivers **actionable capacity recommendations** for city planners and bike-share operations teams.

---

## 🔍 Problem Context

BlueBikes is a station-based bike-share system serving Greater Boston. One of its core operational challenges is **dock imbalance**:

- Some stations frequently run out of bikes  
- Others frequently run out of empty docks  

These imbalances degrade rider experience, increase operational rebalancing effort, and limit system efficiency.

This problem is especially visible in **Watertown, MA**, a growing border city between Boston and Cambridge. The area contains:
- Residential neighborhoods  
- Transit connectors  
- High-activity retail hubs such as **Arsenal Yards**

These features create **persistent, uneven inbound and outbound flows** throughout the day.

**Decision question:**

> Given fixed station locations and limited expansion capacity,  
> **where should dock capacity be increased to improve system availability?**

---

## 🎯 Why This Is Prescriptive Analytics

- **Descriptive analytics** explains what happened  
- **Predictive analytics** estimates what may happen  
- **Prescriptive analytics** determines **what action should be taken**

This project is **prescriptive** because it:
- Defines a concrete operational decision problem  
- Translates historical demand imbalance into **explicit capacity recommendations**  
- Produces **station-level actions**, not just insights  

The system outputs **decisions**, not dashboards.

---

## 🧠 Data Preparation & Diagnostic Analysis (Foundation Layer)

### Data Source
BlueBikes / Hubway Open Data (2020–2025)  
https://s3.amazonaws.com/hubway-data/index.html

The raw dataset spans **millions of trip records across multiple years**. To enable meaningful decision analysis, the data was:

### Cleaning & Transformation
- Consolidated multi-year trip records
- Resolved missing and inconsistent station identifiers
- Standardized station names and IDs
- Cleaned and validated timestamps and ride durations
- Removed incomplete or infeasible trip records

### Diagnostic Exploratory Analysis
Exploratory analysis was used **only as a diagnostic step**, not as the final output.

Key diagnostic patterns observed:
- Persistent imbalance at specific stations rather than random fluctuations
- Strong concentration of demand around the **Watertown / Arsenal corridor**
- Repeated peak-hour shortages at a small subset of stations

Based on these findings, the prescriptive analysis was **intentionally scoped to Watertown**, where intervention would be most operationally meaningful.

> *EDA was used to localize the decision problem — not to replace it.*

---

## ⚙️ Prescriptive Decision Logic

### Constructing Station Pressure

For each station, hourly inbound and outbound flows were aggregated to identify imbalance during operational periods.

From these flows, a **Dock Pressure Score** was computed using:
- **Peak deficit magnitude** (severity of shortages)
- **Frequency of deficit hours** (how often shortages occur)

This score captures **both intensity and persistence** of imbalance.

### Mapping Pressure → Action

Dock Pressure Scores are translated into **discrete dock expansion recommendations** using a rule-based prescriptive framework:

- Low pressure → no action  
- Moderate pressure → small expansion  
- High pressure → priority expansion  

This ensures that:
- Capacity changes are **proportional**
- Interventions are **targeted**
- Resources are **not applied uniformly**

---

## 📌 Prescriptive Outcomes

The prescriptive model identifies:
- **Arsenal Yards** as the highest-priority expansion candidate
- Sustained pressure at **160 Arsenal** and **Arsenal on the Charles**
- Several mid-pressure stations suitable for limited expansion
- Many stations requiring no intervention

These results demonstrate **decision-making under constraints**, a core requirement of prescriptive analytics.

---

## 🖥️ Streamlit Decision-Support Application

The Streamlit application represents the **final prescriptive layer** of the project.

Rather than serving as an exploratory dashboard, the app:
- Presents **final, computed decisions**
- Ranks stations by intervention priority
- Communicates recommendations clearly to non-technical stakeholders

### Application Features
- Dock Pressure Score computation
- Station-level dock expansion recommendations
- Ranked, interpretable output table
- Explanation of decision logic

👉 **Live App:**  
https://bluebikes-dockiq-fdefres2kd5cdcqhyruwmv.streamlit.app

---

## 📊 Outputs

 Dock Pressure Ranking Bar Chart
 <img width="1066" height="647" alt="image" src="https://github.com/user-attachments/assets/5be2fac2-80d1-4186-8005-52b47b8d6a71" />


 Dock Pressure vs Recommended Docks Scatter Plot
 <img width="1299" height="615" alt="image" src="https://github.com/user-attachments/assets/a3358ff4-db28-41e4-91f6-2054c4c3f5ed" />


---

## 🎥 Demo Video

<!-- INSERT LOOM OR YOUTUBE LINK HERE -->

---

## 📁 Project Structure
├── app.py                              # Streamlit decision-support application
├── Blue_Bikes EDA 2.ipynb              # Data cleaning, diagnostics, feature engineering
├── hourly_station_flow.csv             # Hourly inbound/outbound station flows
├── dock_capacity_recommendations.csv   # Final prescriptive recommendations
├── requirements.txt                    # Deployment dependencies
├── README.md                           # Project documentation
└── .gitignore


The notebook supports **analysis and justification**.  
The Streamlit app delivers the **prescriptive outcome**.

---

## 🛠️ Technology Stack
- Python
- Pandas / NumPy
- Matplotlib / Seaborn
- Streamlit
- GitHub

---

## 🚀 Future Extensions
- Incorporate demand forecasting into pressure estimation
- Add cost-aware optimization constraints
- Extend framework to multi-city planning
- Integrate real-time system feeds

---

## ✅ Academic Alignment

This project satisfies:
- ISOM 839 prescriptive analytics requirements
- Decision-focused modeling expectations
- Clear separation of diagnostic vs prescriptive layers
- Portfolio-quality documentation standards
