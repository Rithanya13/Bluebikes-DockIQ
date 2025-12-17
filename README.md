🚲 Bluebikes DockIQ

Prescriptive Optimization for Bike Dock Allocation in Watertown

A prescriptive analytics system that recommends optimal bike dock reallocation across Bluebikes stations under real-world constraints, built for operational decision-making.


🔍 The Problem

Bluebikes is a station-based bike-share system serving Greater Boston. One of its core operational challenges is dock imbalance: some stations regularly run out of bikes, while others run out of empty docks. These imbalances lead to poor user experience, operational inefficiencies, and increased rebalancing costs.

This problem is especially visible in Watertown, MA, a growing border city between Boston and Cambridge. Watertown contains a mix of residential neighborhoods, transit connectors, and retail hubs such as Arsenal Yards, creating uneven inbound and outbound bike flows throughout the day.

City planners and bike-share operators face a constrained decision problem:

Given limited budget and fixed station locations, how should docks be reallocated across stations to improve system-wide availability?

⸻

🎯 Why This Is Prescriptive Analytics
	•	Descriptive analytics explains what happened (historical station usage).
	•	Predictive analytics estimates what may happen (future demand).
	•	Prescriptive analytics determines what actions should be taken.

This project is prescriptive because it goes beyond identifying high-demand stations. It formulates a decision problem and produces actionable recommendations—how many docks to add or remove at each station—under explicit constraints.

The system outputs decisions, not just insights.

⸻

🧠 Data & Feature Engineering

Data Source - https://s3.amazonaws.com/hubway-data/index.html

Cleaning & Transformation

The raw data required substantial preparation:
	•	Unioned inbound and outbound trip records
	•	Filtered trips to Watertown stations only
	•	Resolved inconsistent station identifiers
	•	Verified station locations against official Bluebikes maps
	•	Aggregated trip-level data into station-level metrics

Engineered Features
	•	Total inbound trips per station
	•	Total outbound trips per station
	•	Net demand imbalance indicators
	•	Current dock capacity per station

These features serve as inputs to the prescriptive decision model, not as final outputs.

⸻

📊 Exploratory Findings (Diagnostic, Not the Goal)

Exploratory analysis revealed:
	•	Persistent imbalance across Watertown stations
	•	Arsenal Yards consistently exhibits high outbound demand due to retail and transit activity
	•	Nearby residential stations tend to receive more bikes than they send

These findings motivate intervention, but they do not prescribe action. EDA is used here as a diagnostic step, not the solution.

⸻

⚙️ Prescriptive Optimization Model

Decision Variables
	•	x_i: Number of docks to add (or remove) at station i

Objective

Maximize overall system availability by:
	•	Increasing capacity at high-pressure stations
	•	Reducing excess capacity where docks are underutilized

Constraints
	•	Budget constraint: Total dock changes cannot exceed available budget
	•	Capacity bounds: Each station must remain within minimum and maximum dock limits
	•	Feasibility: Dock adjustments must be realistic and implementable

The model selects the optimal set of dock reallocations that improves coverage while respecting all constraints.

⸻

📌 Prescriptive Findings & Recommendations

Key prescriptive outcomes from the model include:
	•	Arsenal Yards requires dock expansion due to sustained outbound demand
	•	Several nearby residential stations can safely reduce excess capacity
	•	Reallocating docks within Watertown improves availability without adding new infrastructure
	•	A small number of targeted dock changes yields disproportionate system-wide benefits

These results demonstrate trade-offs and decision-making under constraints—hallmarks of prescriptive analytics.

⸻

🖥️ Streamlit Application

## 🖥️ Streamlit Application

The deployed Streamlit application presents the **prescriptive analytics output** of the DockIQ system. Rather than serving as an interactive parameter-tuning tool, the app focuses on clearly communicating **actionable dock capacity recommendations** derived from historical demand imbalance.

The application:
- Computes a Dock Pressure Score for each station based on inbound–outbound imbalance patterns
- Translates pressure scores into **concrete dock expansion recommendations**
- Displays a ranked, station-level table showing where operational intervention is most needed
- Provides interpretability guidance to help decision-makers understand the recommendations

The Streamlit app represents the **final decision-support layer** of the project. All prescriptive logic is executed programmatically, and the app is designed to present **clear, operationally meaningful actions**, not just descriptive metrics or visualizations.

👉 **Live Streamlit App:**  
https://bluebikes-dockiq-fdefres2kd5cdcqhyruwmv.streamlit.app/

⸻
## 📁 Project Structure


📷 Example Output

(Add 1–2 screenshots here showing recommended dock changes or before/after capacity comparison)

⸻

🎥 Demo Video

📺 Loom Demo (3–5 minutes):
(replace MP4 files with a Loom or YouTube link and paste it here)

⸻

🛠️ Technology Stack
	•	Python
	•	Pandas / NumPy
	•	Optimization Solver (Linear Programming)
	•	Streamlit
	•	GitHub

⸻

🎓 Academic Context

This project was developed as the final project for:

ISOM 839 – Prescriptive Analytics
Suffolk University
Fall 2025

⸻

👩‍💻 Author

Rithanya Chandran
MS in Business Analytics
Suffolk University

⸻

🚀 Future Extensions
	•	Incorporate demand forecasting into the optimization loop
	•	Extend the model to multi-city allocation
	•	Add operational cost modeling for bike rebalancing
	•	Integrate real-time system data

⸻

✅ This README Now Meets:
	•	ISOM 839 rubric
	•	Prof. Hasan’s written feedback
	•	Prescriptive analytics definition
	•	Portfolio-quality standards

If you want next:
	•	A commit message
	•	A Loom script
	•	Or help aligning code wording to this README
