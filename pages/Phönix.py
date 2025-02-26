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
    if medikament_name.lower() in ["aspirin", "ibuprofen", "paracetamol", "amoxicillin", "omeprazol",
            "metformin", "simvastatin", "ramipril", "lisinopril", "atorvastatin",
            "pantoprazol", "clopidogrel", "losartan", "bisoprolol", "metoprolol",
            "furosemid", "amlodipin", "levothyroxin", "prednison", "diclofenac",
            "gabapentin", "sertralin", "citalopram", "escitalopram", "venlafaxin",
            "duloxetin", "tramadol", "morphin", "oxycodon", "hydromorphon",
            "insulin", "warfarin", "heparin", "digoxin", "nitroglycerin",
            "fentanyl", "ketamin", "lidocain", "midazolam", "diazepam",
            "alprazolam", "clonazepam", "zolpidem", "eszopiclon", "temazepam",
            "lorazepam", "bupropion", "mirtazapin", "quetiapin", "risperidon",
            "olanzapin", "aripiprazol", "haloperidol", "chlorpromazin", "lithium",
            "valproat", "carbamazepin", "lamotrigin", "topiramat", "levetiracetam",
            "phenytoin", "phenobarbital", "primidon", "gabapentin", "pregabalin",
            "baclofen", "tizanidin", "dantrolen", "cyclobenzaprin", "methocarbamol",
            "azithromycin", "clarithromycin", "doxycyclin", "cefalexin", "ceftriaxon",
            "ciprofloxacin", "levofloxacin", "moxifloxacin", "vancomycin", "linezolid",
            "clindamycin", "metronidazol", "fluconazol", "voriconazol", "amphotericin",
            "acyclovir", "valacyclovir", "oseltamivir", "zanamivir", "ribavirin",
            "sofosbuvir", "ledipasvir", "daclatasvir", "tenofovir", "emtricitabin",
            "efavirenz", "lopinavir", "ritonavir", "darunavir", "raltegravir",
            "dolutegravir", "maraviroc", "enfuvirtid", "abacavir", "lamivudin",
            "zidovudin", "stavudin", "didanosin", "nevirapin", "etravirin",
            "rilpivirin", "atazanavir", "saquinavir", "indinavir", "nelfinavir",
            "tipranavir", "fosamprenavir", "elvitegravir", "cobicistat", "bictegravir"
        ]:  # Beispielhafte Medikamentenliste
        st.success("Das Medikament ist im Compendium enthalten.")
    else:
        st.error("Das Medikament ist nicht im Compendium enthalten.")
    