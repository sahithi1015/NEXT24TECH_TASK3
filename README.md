# NEXT24TECH_TASK3
AIML Internship

# 🌞 Summer Heat Waves Mobile Alert System

## 🔍 Project Overview
The **Summer Heat Waves Mobile Alert System** is an AI-based solution designed to help communities stay safe during extreme heat conditions. With rising global temperatures, this system utilizes machine learning to **predict potential heatwave events** and sends **timely mobile alerts** to users across India based on local weather conditions.

---

##  Key Features

-  **Weather Data Analysis**: Uses historical and real-time weather data for India.
-  **Machine Learning Model**: Trained model (`heatwave_model.pkl`) that predicts possible heatwave events.
-  **Mobile Alert Integration**: Provides alerts through a mobile-friendly application (`heatwave_alert_app`).
-  **Location-Based Forecasting**: Tailored alerts based on the user's region.
-  **Early Warning System**: Helps in proactive health safety and emergency preparedness.

---

##  How It Works

1. **Data Collection**: Historical weather data is collected and preprocessed.
2. **Model Training**: A machine learning model is trained to identify patterns that lead to heatwaves.
3. **Prediction Engine**: New or live weather inputs are passed to the model.
4. **Alert System**: If a potential heatwave is detected, alerts are pushed to users' devices.

---

##  Technologies Used

- **Python** 
- **Pandas, NumPy, Scikit-learn** for data processing and ML modeling
- **Pickle** for model serialization (`.pkl` file)
- **streamlit**

---

##  Dataset Info

- **Source**: [India Heatwave Dataset on Kaggle](https://www.kaggle.com/datasets/ashirwadk24/india-heatwave-dataset)
- **Features Used**:
  - Date
  - State
  - City
  - Temperature
  - Heatwave Label (Yes/No)
- **Purpose**: To train and test models for forecasting heatwave occurrences in different regions of India.

---

##  Future Enhancements

- 🌐 Real-time weather API integration for live predictions.
- 🌡️ Heat index and UV radiation level analysis.
- 📲 Push notifications using Firebase/OneSignal.
- 👵 Elderly & vulnerable population targeted alerts.
- 🗣️ Multi-language alert messages (regional languages).


## Output Images
![image](https://github.com/user-attachments/assets/42175867-91c6-470d-9638-e6a5d0f4b5a6)


![image](https://github.com/user-attachments/assets/15937a4d-0ee7-40cc-a88e-76d2fa0740e8)

