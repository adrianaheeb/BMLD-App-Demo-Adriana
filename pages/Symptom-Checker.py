import streamlit as st
import random

st.title("Symptom-Checker")

def diagnose(symptoms):
    possible_diagnoses = {
        "Erkältung": ["Husten", "Schnupfen", "Halsschmerzen", "laufende Nase"],
        "Grippe": ["Fieber", "Kopfschmerzen", "Gliederschmerzen", "Schüttelfrost"],
        "COVID-19": ["Fieber", "Husten", "Atemnot", "kein Geruchssinn"],
        "Allergie": ["Niesen", "Juckreiz", "Augentränen", "Hautausschlag"],
        "Magen-Darm-Infekt": ["Durchfall", "Übelkeit", "Erbrechen", "Bauchschmerzen"],
        "Mittelohrentzündung": ["Ohrenschmerzen", "Fieber", "Hörprobleme", "Schwindel"],
        "Angina": ["Halsschmerzen", "Schluckbeschwerden", "geschwollene Lymphknoten", "Fieber", "geschwollene Mandeln"],
        "Migräne": ["Kopfschmerzen", "Lichtempfindlichkeit", "Übelkeit", "Sehstörungen"],
        "Blasenentzündung": ["Brennen beim Wasserlassen", "häufiger Harndrang", "trüber Urin", "Bauchschmerzen"],
        "Rückenschmerzen": ["Schmerzen im unteren Rücken", "Bewegungseinschränkung", "Muskelverspannungen", "Schmerzen beim Sitzen"],
        "Mumps": ["geschwollene Ohrspeicheldrüsen", "Fieber", "Kopfschmerzen", "Müdigkeit"],
        "Neurodermitis": ["trockene Haut", "Juckreiz", "Ekzeme", "Rötungen"],
        "Schilddrüsenüberfunktion": ["Gewichtsverlust", "Nervosität", "Herzrasen", "Schlaflosigkeit"],
        "Schilddrüsenunterfunktion": ["Gewichtszunahme", "Müdigkeit", "Kälteempfindlichkeit", "Verstopfung"],
        "Diabetes": ["häufiges Wasserlassen", "Durstgefühl", "Müdigkeit", "Juckreiz"],
        "Bluthochdruck": ["Kopfschmerzen", "Schwindel", "Ohrensausen", "Nasenbluten"],
        "Herzinfarkt": ["Brustschmerzen", "Atemnot", "Schweißausbruch", "Übelkeit"],
        "Bandscheibenprobleme": ["Rückenschmerzen", "Ischiasschmerzen", "Taubheitsgefühl", "Bewegungseinschränkung"],
        "Bakterielle Lungenentzündung": ["Fieber", "Husten mit Auswurf", "Atemnot", "Brustschmerzen"],
        "Asthma": ["Atemnot", "Husten", "pfeifender Atem", "Engegefühl in der Brust"],
        "Zöliakie": ["Durchfall", "Bauchschmerzen", "Blähungen", "Gewichtsverlust"],
        "Zahnfleischentzündung": ["Zahnfleischbluten", "Zahnschmerzen", "geschwollenes Zahnfleisch", "Mundgeruch"],
        "Periode": ["Bauchschmerzen", "Rückenschmerzen", "Stimmungsschwankungen", "Kopfschmerzen"],
        "Schwangerschaft": ["Übelkeit", "Müdigkeit", "Brustspannen", "Ausbleiben der Periode"],
        "Wechseljahre": ["Hitzewallungen", "Schlafstörungen", "Stimmungsschwankungen", "Gewichtszunahme"],
        "Schlafapnoe": ["Schnarchen", "Atemaussetzer im Schlaf", "Tagesmüdigkeit", "Konzentrationsprobleme"],
        "Einschlafstörungen": ["Schlaflosigkeit", "Unruhe", "Gedankenkreisen", "Müdigkeit am Tag"],
        "Durchschlafstörungen": ["Nächtliches Erwachen", "Schlaflosigkeit", "Müdigkeit am Tag", "Gereiztheit"],
        "Restless-Legs-Syndrom": ["Kribbeln in den Beinen", "Bewegungsdrang", "Unruhe", "Schlafstörungen"],
        "Schlafwandeln": ["Nächtliches Aufstehen", "Verwirrung", "Gedächtnislücken", "Müdigkeit am Tag"],
        "Zahnabszess": ["Zahnschmerzen", "Schwellung im Mund", "Fieber", "geschwollene Lymphknoten"],
        "Zahnkaries": ["Zahnschmerzen", "Empfindlichkeit gegenüber Süßem", "Loch im Zahn", "Schwellung im Mund"],
        "Zahnfleischrückgang": ["Zahnfleischrückgang", "Zahnhalsfreilegung", "Zahnlockerung", "Zahn" "empfindlichkeit"],
        "Zahnwurzelentzündung": ["Zahnschmerzen", "Schwellung im Mund", "Fieber", "geschwollene Lymphknoten"],
        "Innere Blutung": ["Blut im Urin", "Blut im Stuhl", "Blut im Erbrochenen", "Blutergüsse"],
         }

    
    diagnosis_probabilities = {}
    
    for diagnosis, diagnosis_symptoms in possible_diagnoses.items():
        match_count = len(set(symptoms) & set(diagnosis_symptoms))
        probability = match_count / len(diagnosis_symptoms)
        diagnosis_probabilities[diagnosis] = round(probability * 100, 2)
    
    return diagnosis_probabilities

symptoms = st.text_input("Geben Sie Ihre Symptome ein (kommagetrennt):")

if symptoms:
    symptoms_list = [symptom.strip() for symptom in symptoms.split(",")]
    probabilities = diagnose(symptoms_list)
    
    st.subheader("Mögliche Diagnosen mit Wahrscheinlichkeiten:")
    for diagnosis, probability in probabilities.items():
        st.write(f"{diagnosis}: {probability}%")