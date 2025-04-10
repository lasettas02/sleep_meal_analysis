# Sleep and Meal Pattern Analysis Using MiBand Data

This repository contains the full code and anonymized datasets for a field study conducted as part of the JBM170 course at TU/e. The project investigates how daily food intake patterns (timing and amount) influence sleep quality, using biometric and self-logged data.

## 📁 Project Structure

- `x1_sleep_meal_data.csv` – Combined sleep and meal data for participant x1
- `final_sleep_meal_data.csv` – Combined and cleaned data for participants x2–x5
- `cleaned_summary_sleep_meal_*.csv` – Cleaned summaries for modeling and EDA
- `*.py` – Python scripts for cleaning, analysis, and modeling
- `README.md` – Project documentation
- `LICENSE` – Open source license
- `requirements.txt` – Python dependencies

## 💡 Project Goal

To analyze how behavioral variables such as:
- number of meals,
- meal timing,
- workout presence,
- and late-night eating  
affect sleep quality as measured through custom-calculated sleep scores derived from wearable sensor data.

## 🧠 Methodology

- Data collected from MiBand 6 devices + manually logged meals
- Cleaned and merged in Python using pandas
- Sleep score calculated from biometric signals
- Linear regression used for predictive modeling
- All results anonymized using `x1` through `x5` labels

## 🔒 Anonymization & Ethics

All data has been anonymized and is fully compliant with GDPR and FAIR principles. Participant names have been replaced with `x1` through `x5`.

## 🔁 Reuse

You are free to use, modify, and build upon this work under the MIT license. See `LICENSE`.
