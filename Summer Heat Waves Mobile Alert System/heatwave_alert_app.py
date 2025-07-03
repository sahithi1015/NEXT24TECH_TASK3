import streamlit as st
import joblib

# Load model
model = joblib.load("heatwave_model.pkl")

st.set_page_config(page_title="Heatwave Alert", page_icon="🌡️")
st.title("🌞 Summer Heatwave Alert System (India)")

# Collect user inputs
temp = st.slider("Average Temperature (°C)", 20.0, 50.0, 35.0)
humidity = st.slider("Average Humidity (%)", 10.0, 100.0, 60.0)
wind = st.slider("Wind Speed (km/h)", 0.0, 50.0, 10.0)

# Predict
if st.button("Check Heatwave Risk"):
    prediction = model.predict([[temp, humidity, wind]])

    if prediction[0]:
        st.error("🚨 Heatwave Alert!\nHigh risk detected. Stay indoors, hydrate regularly, and avoid outdoor activity.")
    else:
        st.success("✅ Conditions are safe.\nNo heatwave predicted. Keep cool and carry on.")

# Footer
st.markdown("---")

