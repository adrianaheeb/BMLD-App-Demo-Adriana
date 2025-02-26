import streamlit as st

st.title("Medikamentendosierungen")

def calculate_dose(weight, medication):
    dosages = {
        "Dafalgan": {"dose_per_kg": 15, "max_dose": 1000},
        "Ibuprofen": {"dose_per_kg": 10, "max_dose": 800},
        "Aspirin": {"dose_per_kg": 10, "max_dose": 1000},
        "Diclofenac": {"dose_per_kg": 2, "max_dose": 150},
        "Naproxen": {"dose_per_kg": 5, "max_dose": 500}
    }
    if medication in dosages:
        dose_per_kg = dosages[medication]["dose_per_kg"]
        max_dose = dosages[medication]["max_dose"]
        dose = weight * dose_per_kg
        if dose > max_dose:
            dose = max_dose
        return dose
    else:
        return None

st.header("NSAID Dosierungsrechner")

medication = st.selectbox("Wählen Sie ein Medikament:", ["Dafalgan", "Ibuprofen", "Aspirin", "Diclofenac", "Naproxen"])
weight = st.number_input("Geben Sie das Gewicht in kg ein:", min_value=0.0, step=0.1)

if weight > 0:
    dose = calculate_dose(weight, medication)
    if dose is not None:
        st.write(f"Die empfohlene Dosis für {weight} kg beträgt {dose} mg.")
    else:
        st.write("Ungültiges Medikament ausgewählt.")
else:
    st.write("Bitte geben Sie ein gültiges Gewicht ein.")
