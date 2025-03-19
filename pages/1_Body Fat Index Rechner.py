from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 

import streamlit as st

def calculate_body_fat_index(weight, waist, wrist, hip, forearm):
    # Simplified formula for demonstration purposes
    body_fat = (weight * 0.732) + 8.987 + (waist / 3.14) - (wrist / 3.14) + (hip / 3.14) - (forearm / 3.14)
    return body_fat

st.title("Body Fat Index Rechner")

st.header("Geben Sie Ihre Daten ein:")

weight = st.number_input("Gewicht (kg)", min_value=0.0, format="%.2f")
waist = st.number_input("Taillenumfang (cm)", min_value=0.0, format="%.2f")
wrist = st.number_input("Handgelenkumfang (cm)", min_value=0.0, format="%.2f")
hip = st.number_input("Hüftumfang (cm)", min_value=0.0, format="%.2f")
forearm = st.number_input("Unterarmumfang (cm)", min_value=0.0, format="%.2f")

if st.button("Berechnen"):
    body_fat_index = calculate_body_fat_index(weight, waist, wrist, hip, forearm)
    st.success(f"Ihr Body Fat Index ist: {body_fat_index:.2f}")

from utils.data_manager import DataManager

if st.button("Berechnen"):
    body_fat_index = calculate_body_fat_index(weight, waist, wrist, hip, forearm)
    st.success(f"Ihr Body Fat Index ist: {body_fat_index:.2f}")
    result = {
        'weight': weight,
        'waist': waist,
        'wrist': wrist,
        'hip': hip,
        'forearm': forearm,
        'body_fat_index': body_fat_index
    }
    DataManager().append_record(session_state_key='data_df', record_dict=result)  # update data in session state and storage
