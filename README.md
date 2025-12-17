🚲 Bluebikes DockIQ

Prescriptive Decision Intelligence for Bike Dock Allocation in Watertown

DockIQ is a prescriptive analytics decision intelligence system that converts historical Bluebikes demand imbalance into actionable, station-level dock capacity recommendations to support operational planning and infrastructure decisions in Watertown, MA.

The system is designed to help planners move beyond descriptive dashboards toward clear, prioritized actions under real-world constraints.

⸻

🎯 Why This Is Prescriptive Analytics

Analytics maturity progresses through three levels:
	•	Descriptive analytics explains what has happened
	•	Predictive analytics estimates what may happen
	•	Prescriptive analytics determines what should be done

DockIQ operates at the prescriptive level by transforming observed demand imbalance into explicit capacity decisions—recommending where dock capacity should be expanded or reduced to improve system-wide availability.

The output of the system is decisions, not just insights.

⸻

🧠 Data & Feature Engineering

Data Source:
Bluebikes historical trip data (2020–2025)
https://s3.amazonaws.com/hubway-data/index.html

Data Preparation

Raw trip-level data was processed to support decision-making:
	•	Integrated inbound and outbound trip flows
	•	Filtered to Watertown and Arsenal-area stations
	•	Standardized station identifiers and locations
	•	Aggregated trips into station- and hour-level flow metrics

Engineered Decision Signals

Key signals derived from the data include:
	•	Hourly inbound and outbound demand
	•	Net flow imbalance by station
	•	Peak shortage magnitude
	•	Frequency of shortage periods

These signals form the foundation of the prescriptive logic, enabling the system to distinguish between transient variation and persistent structural imbalance.

⸻

📊 Exploratory Analysis (Decision-Oriented)

Exploratory analysis revealed persistent, spatially concentrated imbalance across Watertown stations.
In particular:
	•	Arsenal Yards consistently exhibits elevated outbound pressure driven by retail, transit, and commuter activity
	•	Nearby residential stations show complementary inbound-heavy patterns

These findings establish the need for intervention and guide the design of the prescriptive decision framework.

⸻

⚙️ Prescriptive Decision Framework

DockIQ applies a structured prescriptive framework to translate demand imbalance into capacity adjustment recommendations.

Decision Variable
	•	Recommended dock capacity adjustment at each station

Decision Logic

A composite Dock Pressure Score is computed for each station, capturing:
	•	Severity of peak bike shortages
	•	Persistence of imbalance across time

Stations are then prioritized, and capacity recommendations are generated in proportion to observed operational pressure.

This approach enables:
	•	Transparent decision-making
	•	Clear prioritization under constraints
	•	Operationally realistic recommendations

⸻

📌 Prescriptive Findings & Recommendations

Key outcomes from the system include:
	•	Arsenal Yards is identified as a top-priority candidate for dock expansion
	•	Several nearby stations exhibit lower pressure and can absorb capacity reductions
	•	Reallocating docks within Watertown improves availability without additional infrastructure
	•	A small number of targeted interventions delivers disproportionate system-wide benefit

These results demonstrate trade-offs, prioritization, and constrained decision-making, which are core characteristics of prescriptive analytics.

⸻

🖥️ Streamlit Decision Support Application

The deployed Streamlit application presents the final prescriptive output of DockIQ.

The application:
	•	Computes station-level pressure metrics
	•	Ranks stations by operational urgency
	•	Displays clear, actionable dock capacity recommendations
	•	Supports planners in identifying where intervention matters most

The application is designed as a decision-support interface, not a visualization-only dashboard.

👉 Live Streamlit App:
https://bluebikes-dockiq-fdefres2kd5cdcqhyruwmv.streamlit.app

├── app.py                              # Prescriptive decision-support application  
├── Blue_Bikes EDA 2.ipynb              # Data preparation & analytical foundation  
├── hourly_station_flow.csv             # Station-level demand flow metrics  
├── dock_capacity_recommendations.csv   # Prescriptive capacity recommendations  
├── requirements.txt                    # Deployment dependencies  
├── README.md                           # Project documentation  
└── .gitignore                          # Version control exclusions

🛠️ Technology Stack
	•	Python
	•	Pandas / NumPy
	•	Prescriptive decision logic
	•	Streamlit
	•	GitHub

⸻

🎓 Academic Context

ISOM 839 – Prescriptive Analytics
Suffolk University

⸻

👩‍💻 Author

Rithanya Chandran
MS in Business Analytics
Suffolk University

⸻

🚀 Future Extensions
	•	Integrate demand forecasting into the decision framework
	•	Extend the model to explicit budget-constrained optimization
	•	Scale to multi-city capacity planning
	•	Incorporate real-time system data
