
import streamlit as st
import pandas as pd
import pickle
import os

st.set_page_config(
    page_title="Appliance Energy Prediction",
    page_icon="⚡",
    layout="centered"
)

st.title("⚡ Appliance Energy Consumption Prediction")
st.write("Predict appliance energy consumption based on temperature.")

MODEL_FILE = "appliance_energy_model.pkl"
DATA_FILE = "appliance_energy.csv"

# Load dataset
try:
    data = pd.read_csv(DATA_FILE)
    st.success("Dataset loaded successfully.")
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

# Display dataset
with st.expander("View Dataset"):
    st.dataframe(data)

# Load model
try:
    with open(MODEL_FILE, "rb") as file:
        model = pickle.load(file)
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.info(
        "The uploaded model file may not be a valid Python pickle file "
        "or may have been created using a different serialization method."
    )
    st.stop()

st.subheader("Enter Temperature")

temperature = st.number_input(
    "Temperature (°C)",
    min_value=-50.0,
    max_value=100.0,
    value=25.0,
    step=0.1
)

if st.button("Predict Energy Consumption ⚡"):

    input_data = pd.DataFrame({
        "Temperature (°C)": [temperature]
    })

    try:
        prediction = model.predict(input_data)

        st.success(
            f"Predicted Energy Consumption: {prediction[0]:.2f} kWh"
        )

    except Exception as e:
        st.error(f"Prediction error: {e}")
