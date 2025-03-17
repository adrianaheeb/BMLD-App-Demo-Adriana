# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st

def body_fat_percentage(weight, height, age, gender, activity_level):
    if height <= 0:
        st.error("Die Größe muss größer als null sein.")
        return None
    if weight <= 0:
        st.error("Das Gewicht muss größer als null sein.")
        return None
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

    return round(body_fat, 2)

st.title('Body Fat Index Calculator')

weight = st.number_input("Gewicht (kg)", min_value=30, max_value=200, value=70)
height = st.number_input("Größe (cm)", min_value=100, max_value=250, value=170)
age = st.number_input("Alter (Jahre)", min_value=10, max_value=120, value=25)
gender = st.radio("Geschlecht", ('Männlich', 'Weiblich'))
activity_level = st.radio("Aktivitätslevel", ['Sehr aktiv', 'Mäßig aktiv', 'Wenig aktiv'])


if st.button("Berechnen"):
    body_fat = body_fat_percentage(weight, height, age, gender, activity_level)
    
    if body_fat is not None:  # Sicherstellen, dass keine None zurückgegeben wird
        st.write(f"Dein geschätzter Körperfettanteil beträgt: {body_fat}%")
    if gender == 'Männlich':
        if body_fat < 6:
            st.write("Der Körperfettanteil ist sehr niedrig.")
        elif body_fat < 24:
            st.write("Der Körperfettanteil ist im Normbereich.")
        else:
            st.write("Der Körperfettanteil ist hoch.")
    else:
        if body_fat < 16:
            st.write("Der Körperfettanteil ist sehr niedrig.")
        elif body_fat < 30:
            st.write("Der Körperfettanteil ist im Normbereich.")
        else:
            st.write("Der Körperfettanteil ist hoch.")

from utils.data_manager import DataManager
DataManager().append_record(session_state_key='data_df', record_dict="result")
result = {
    'Gewicht': weight,
    'Größe': height,
    'Alter': age,
    'Geschlecht': gender,
    'Aktivitätslevel': activity_level,
    'Körperfettanteil': body_fat
}