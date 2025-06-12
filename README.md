# 🔋 EV Charging Client (Python)

This is a Python-based client that communicates with a simulated electric vehicle (EV) charging station using RESTful JSON APIs. It retrieves electricity prices, household energy usage, and battery status to optimize charging operations under specific constraints.

---

## 📚 Overview

This project demonstrates basic **Battery Management Services** by simulating interaction with a charging station. The system ensures:

- Battery is charged from **20% to 80%**
- Charging happens only when:
  - Total load (household + charger) is under **11 kW**
  - (By default) Electricity price is lowest

You can easily switch the strategy to optimize based on **lowest household consumption** instead of electricity price.

---

## 🧰 Features

- 🛰️ REST API communication with simulated station
- ⚡ Automatic start/stop charging logic
- 💰 Price-based optimization
- 📈 Load-aware decision making
- 🔌 Configurable charging limits

---
