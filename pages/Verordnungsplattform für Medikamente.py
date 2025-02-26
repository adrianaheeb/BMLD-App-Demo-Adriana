import streamlit as st

st.title("Verordnungsplattform für Medikamente")

with st.form(key='erweiterte_medikamenten_form'):
    patient_name = st.text_input("Patientenname")
    medikament_name = st.text_input("Medikamentenname")
    tage = st.number_input("Anzahl der Tage", min_value=1, max_value=30, step=1)
    morgen_dosis = st.text_input("Morgendosis")
    mittag_dosis = st.text_input("Mittagdosis")
    abend_dosis = st.text_input("Abenddosis")
    nacht_dosis = st.text_input("Nachtdosis")
    einnahmeart = st.selectbox("Einnahmeart", ["Oral", "Parenteral", "Reservemedikament"])
    zeitlich_begrenzt = st.checkbox("Zeitlich begrenzt verordnen")
    if zeitlich_begrenzt:
        startdatum = st.date_input("Startdatum")
        enddatum = st.date_input("Enddatum")
    anweisungen = st.text_area("Anweisungen")
    erweiterte_submit_button = st.form_submit_button(label='Erweiterte Verordnung')

if erweiterte_submit_button:
    st.subheader("Erweiterte Verordnung")
    st.write(f"Patientenname: {patient_name}")
    st.write(f"Medikamentenname: {medikament_name}")
    medikamenten_auswahl = st.selectbox("Wählen Sie ein Medikament aus der Liste", medikament_name)
    st.write(f"Ausgewähltes Medikament: {medikamenten_auswahl}")
    st.write(f"Anzahl der Tage: {tage}")
    st.write(f"Morgendosis: {morgen_dosis}")
    st.write(f"Mittagdosis: {mittag_dosis}")
    st.write(f"Abenddosis: {abend_dosis}")
    st.write(f"Nachtdosis: {nacht_dosis}")
    st.write(f"Einnahmeart: {einnahmeart}")
    if zeitlich_begrenzt:
        st.subheader("Zeitlich begrenzte Verordnungen")
        verordnungen = []
        for i in range(1, 6):
            with st.expander(f"Verordnung {i}"):
                startdatum = st.date_input(f"Startdatum {i}")
                enddatum = st.date_input(f"Enddatum {i}")
                verordnungen.append((startdatum, enddatum))
        for idx, (start, end) in enumerate(verordnungen):
            st.write(f"Verordnung {idx + 1}: Startdatum: {start}, Enddatum: {end}")
    st.write(f"Anweisungen: {anweisungen}")

st.subheader("Medikamentenliste")
medikamenten_liste = [
    "Aspirin", "Ibuprofen", "Paracetamol", "Amoxicillin", "Omeprazol",
    "Metformin", "Simvastatin", "Ramipril", "Lisinopril", "Atorvastatin",
    "Pantoprazol", "Clopidogrel", "Losartan", "Bisoprolol", "Metoprolol",
    "Furosemid", "Amlodipin", "Levothyroxin", "Prednison", "Diclofenac",
    "Gabapentin", "Sertralin", "Citalopram", "Escitalopram", "Venlafaxin",
    "Duloxetin", "Tramadol", "Morphin", "Oxycodon", "Hydromorphon",
    "Insulin", "Warfarin", "Heparin", "Digoxin", "Nitroglycerin",
    "Fentanyl", "Ketamin", "Lidocain", "Midazolam", "Diazepam",
    "Alprazolam", "Clonazepam", "Zolpidem", "Eszopiclon", "Temazepam",
    "Lorazepam", "Bupropion", "Mirtazapin", "Quetiapin", "Risperidon",
    "Olanzapin", "Aripiprazol", "Haloperidol", "Chlorpromazin", "Lithium",
    "Valproat", "Carbamazepin", "Lamotrigin", "Topiramat", "Levetiracetam",
    "Phenytoin", "Phenobarbital", "Primidon", "Gabapentin", "Pregabalin",
    "Baclofen", "Tizanidin", "Dantrolen", "Cyclobenzaprin", "Methocarbamol",
    "Azithromycin", "Clarithromycin", "Doxycyclin", "Cefalexin", "Ceftriaxon",
    "Ciprofloxacin", "Levofloxacin", "Moxifloxacin", "Vancomycin", "Linezolid",
    "Clindamycin", "Metronidazol", "Fluconazol", "Voriconazol", "Amphotericin",
    "Acyclovir", "Valacyclovir", "Oseltamivir", "Zanamivir", "Ribavirin",
    "Sofosbuvir", "Ledipasvir", "Daclatasvir", "Tenofovir", "Emtricitabin",
    "Efavirenz", "Lopinavir", "Ritonavir", "Darunavir", "Raltegravir",
    "Dolutegravir", "Maraviroc", "Enfuvirtid", "Abacavir", "Lamivudin",
    "Zidovudin", "Stavudin", "Didanosin", "Nevirapin", "Etravirin",
    "Rilpivirin", "Atazanavir", "Saquinavir", "Indinavir", "Nelfinavir",
    "Tipranavir", "Fosamprenavir", "Elvitegravir", "Cobicistat", "Bictegravir"
    ]
