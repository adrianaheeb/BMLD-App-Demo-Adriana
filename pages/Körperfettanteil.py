import streamlit as st

st.title("Körperfettanteil-Rechner")

# Körperfettanteil-Berechnung basierend auf der US Navy Methode
def body_fat_percentage(weight, height, neck, waist, hip, gender):
    if gender == "Männlich":
        # Formel für Männer
        body_fat = 86.010 * (waist - neck) / height - 70.041 * (height / weight) + 36.76
    else:
        # Formel für Frauen
        body_fat = 163.205 * (waist + hip - neck) / height - 97.684 * (height / weight) - 78.387
    
    return body_fat

# Eingabefelder
gender = st.selectbox("Geschlecht", ["Männlich", "Weiblich"])
weight = st.number_input("Gewicht (kg)", min_value=1, step=0.1)
height = st.number_input("Körpergröße (cm)", min_value=100, max_value=250, step=1)
neck = st.number_input("Halsumfang (cm)", min_value=10, max_value=60, step=0.1)
waist = st.number_input("Taillenumfang (cm)", min_value=40, max_value=150, step=0.1)
hip = 0  # Für Männer bleibt dieser Wert auf 0, da er nicht gebraucht wird
if gender == "Weiblich":
    hip = st.number_input("Hüftumfang (cm)", min_value=60, max_value=160, step=0.1)

# Berechnung des Körperfettanteils
if weight and height and neck and waist and (gender == "Männlich" or hip):
    body_fat = body_fat_percentage(weight, height / 100, neck, waist, hip, gender)  # Größe in Meter
    st.write(f"Dein Körperfettanteil beträgt etwa: {body_fat:.2f}%")
    
    if body_fat < 6:
        st.write("Dein Körperfettanteil ist extrem niedrig!")
    elif 6 <= body_fat <= 24:
        st.write("Du befindest dich im gesunden Bereich!")
    elif body_fat > 24:
        st.write("Dein Körperfettanteil ist hoch. Überlege, deine Ernährung und Aktivität zu überprüfen.")
