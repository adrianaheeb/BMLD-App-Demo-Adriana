import streamlit as st

st.title("Phönix")

st.header("Verordnungsplattform für Medikamente")

# Eingabeformular für Medikamentenverordnung
with st.form(key='medikamenten_form'):
    patient_name = st.text_input("Patientenname")
    medikament_name = st.text_input("Medikamentenname")
    dosis = st.text_input("Dosis")
    anweisungen = st.text_area("Anweisungen")
    submit_button = st.form_submit_button(label='Verordnen')

# Anzeige der Verordnung
if submit_button:
    st.subheader("Verordnung")
    st.write(f"Patientenname: {patient_name}")
    st.write(f"Medikamentenname: {medikament_name}")
    st.write(f"Dosis: {dosis}")
    st.write(f"Anweisungen: {anweisungen}")

    # Compendium Kontrolle
    st.subheader("Compendium Kontrolle")
    if medikament_name.lower() in ["aspirin", "ibuprofen", "paracetamol"]:  # Beispielhafte Medikamentenliste
        st.success("Das Medikament ist im Compendium enthalten.")
    else:
        st.error("Das Medikament ist nicht im Compendium enthalten.")