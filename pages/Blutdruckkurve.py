import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.title("Schlaftracker")

# Funktion zum Erfassen der Schlafdaten
def erfasse_schlafdaten():
    st.header("Schlaf-Tagebuch")
    datum = st.date_input("Datum")
    schlafenszeit = st.time_input("Schlafenszeit")
    aufwachzeit = st.time_input("Aufwachzeit")
    schlafqualitaet = st.slider("Schlafqualität (1-10)", 1, 10)
    if st.button("Daten speichern"):
        schlafdauer = (datetime.combine(datum, aufwachzeit) - datetime.combine(datum, schlafenszeit)).seconds / 3600
        neue_daten = {"Datum": datum, "Schlafenszeit": schlafenszeit, "Aufwachzeit": aufwachzeit, "Schlafqualität": schlafqualitaet, "Schlafdauer": schlafdauer}
        if "schlafdaten" not in st.session_state:
            st.session_state.schlafdaten = []
        st.session_state.schlafdaten.append(neue_daten)
        st.success("Daten gespeichert!")

# Funktion zur Analyse der Schlafdaten
def analysiere_schlafdaten():
    st.header("Schlafanalyse")
    if "schlafdaten" in st.session_state and st.session_state.schlafdaten:
        df = pd.DataFrame(st.session_state.schlafdaten)
        st.line_chart(df.set_index("Datum")[["Schlafqualität", "Schlafdauer"]])
        durchschnitt_qualitaet = df["Schlafqualität"].mean()
        durchschnitt_dauer = df["Schlafdauer"].mean()
        st.write(f"Durchschnittliche Schlafqualität: {durchschnitt_qualitaet:.2f}")
        st.write(f"Durchschnittliche Schlafdauer: {durchschnitt_dauer:.2f} Stunden")
        if durchschnitt_qualitaet < 5:
            st.warning("Ihre Schlafqualität ist unterdurchschnittlich. Versuchen Sie, Ihre Schlafumgebung zu verbessern.")
        if durchschnitt_dauer < 7:
            st.warning("Sie schlafen weniger als die empfohlenen 7 Stunden pro Nacht. Versuchen Sie, mehr Schlaf zu bekommen.")
    else:
        st.info("Keine Schlafdaten vorhanden. Bitte erfassen Sie Ihre Schlafdaten.")

# Hauptfunktion
def main():
    erfasse_schlafdaten()
    analysiere_schlafdaten()

main()

