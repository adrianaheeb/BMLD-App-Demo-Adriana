import streamlit as st

def body_fat_percentage(weight, height, age, gender):

    if height == 0:
        st.error("Die Größe darf nicht null sein.")
        return None
    bmi = weight / (height / 100) ** 2
    
    if gender == 'Männlich':
        body_fat = 1.20 * bmi + 0.23 * age - 16.2
    else:
        body_fat = 1.20 * bmi + 0.23 * age - 5.4
    
    return round(body_fat, 2)

st.title('Körperfettanteil Rechner')

weight = st.number_input("Gewicht (kg)", min_value=30, max_value=200, value=70)
height = st.number_input("Größe (cm)", min_value=100, max_value=250, value=170)
age = st.number_input("Alter (Jahre)", min_value=10, max_value=120, value=25)
gender = st.selectbox("Geschlecht", options=["Männlich", "Weiblich"])

if st.button("Berechnen"):
    body_fat = body_fat_percentage(weight, height, age, gender)
    if body_fat is not None:
        if body_fat < 6:
            st.write("Du hast einen sehr niedrigen Körperfettanteil.")
        elif body_fat < 24:
            st.write("Du hast einen normalen Körperfettanteil.")
        elif body_fat < 31:
            st.write("Du hast einen erhöhten Körperfettanteil.")
        else:
            st.write("Du hast einen sehr hohen Körperfettanteil.")