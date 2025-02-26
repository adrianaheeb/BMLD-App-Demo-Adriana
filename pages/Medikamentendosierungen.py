import streamlit as st

st.title("Medikamentendosierungen")

st.write("Diese Seite ist eine Unterseite der Startseite.")

def calculate_dose(weight):
    # Dafalgan dosage: 10-15 mg per kg of body weight, max 1000 mg per dose
    dose_per_kg = 15
    max_dose = 1000
    dose = weight * dose_per_kg
    if dose > max_dose:
        dose = max_dose
    return dose

st.header("Dafalgan Dosierungsrechner")

weight = st.number_input("Geben Sie das Gewicht in kg ein:", min_value=0.0, step=0.1)

if weight > 0:
    dose = calculate_dose(weight)
    st.write(f"Die empfohlene Dosis für {weight} kg beträgt {dose} mg.")
else:
    st.write("Bitte geben Sie ein gültiges Gewicht ein.")