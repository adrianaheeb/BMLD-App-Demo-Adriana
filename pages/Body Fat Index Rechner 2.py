from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 

import streamlit as st
from utils.data_manager import DataManager

def calculate_body_fat(weight, height, age, gender, activity_level):
    if height <= 0 or weight <= 0:
        return {"error": "Gewicht und Größe müssen größer als null sein."}
    
    bmi = weight / (height / 100) ** 2
    
    if gender == 'Männlich':
        body_fat = 1.20 * bmi + 0.23 * age - 16.2
    else:
        body_fat = 1.20 * bmi + 0.23 * age - 5.4
    
    if activity_level == 'Sehr aktiv':
        body_fat -= 3
    elif activity_level == 'Mäßig aktiv':
        body_fat -= 1
    elif activity_level == 'Wenig aktiv':
        body_fat += 2
    
    body_fat = round(body_fat, 2)
    
    category = "hoch"
    if gender == 'Männlich':
        if body_fat < 6:
            category = "sehr niedrig"
        elif body_fat < 24:
            category = "im Normbereich"
    else:
        if body_fat < 16:
            category = "sehr niedrig"
        elif body_fat < 30:
            category = "im Normbereich"
    
    return {
        "Gewicht (kg)": weight,
        "Größe (cm)": height,
        "Alter (Jahre)": age,
        "Geschlecht": gender,
        "Aktivitätslevel": activity_level,
        "Körperfettanteil (%)": body_fat,
        "Kategorie": category
    }

st.title('Body Fat Index Calculator')

weight = st.number_input("Gewicht (kg)", min_value=30, max_value=200, value=70)
height = st.number_input("Größe (cm)", min_value=100, max_value=250, value=170)
age = st.number_input("Alter (Jahre)", min_value=10, max_value=120, value=25)
gender = st.radio("Geschlecht", ('Männlich', 'Weiblich'))
activity_level = st.radio("Aktivitätslevel", ['Sehr aktiv', 'Mäßig aktiv', 'Wenig aktiv'])

if st.button("Berechnen"):
    result = calculate_body_fat(weight, height, age, gender, activity_level)
    
    if "error" in result:
        st.error(result["error"])
    else:
        st.write(f"Dein geschätzter Körperfettanteil beträgt: {result['Körperfettanteil (%)']}%")
        st.write(f"Kategorie: {result['Kategorie']}")
        DataManager().append_record(session_state_key='data_df', record_dict=result)
