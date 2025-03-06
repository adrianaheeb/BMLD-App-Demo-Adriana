import streamlit as st

def body_fat_percentage(weight, height, age, gender, activity_level):
    if height == 0:
        st.error("Die Größe darf nicht null sein.")
        return None
    if weight == 0:
        st.error("Das Gewicht darf nicht null sein.")
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

st.title('Körperfettanteil Rechner mit Berücksichtigung des Aktivitätslevels')

weight = st.number_input("Gewicht (kg)", min_value=30, max_value=200, value=70)
height = st.number_input("Größe (cm)", min_value=100, max_value=250, value=170)
age = st.number_input("Alter (Jahre)", min_value=10, max_value=120, value=25)
gender = st.radio("Geschlecht", ('Männlich', 'Weiblich'))
activity_level = st.selectbox("Aktivitätslevel", ['Sehr aktiv', 'Mäßig aktiv', 'Wenig aktiv'])

if st.button("Berechnen"):
    body_fat = body_fat_percentage(weight, height, age, gender, activity_level)
    st.write(f"Dein geschätzter Körperfettanteil beträgt: {body_fat}%")
