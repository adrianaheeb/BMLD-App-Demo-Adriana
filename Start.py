import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager
 
# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="BMLD_LN 2")  # switch drive
 
# initialize the login manager
login_manager = LoginManager(data_manager)
login_manager.login_register()  # open login/register page
 
# load the data from the persistent storage into the session state
data_manager.load_user_data(
    session_state_key='data_df',
    file_name='data.csv',
    initial_value = pd.DataFrame(),
    parse_dates = ['timestamp']
    )
 
import streamlit as st

# Streamlit UI
st.title("BodyFatIndex-App")
st.write("Diese Streamlit-App bietet eine klare und benutzerfreundliche Oberfläche zur präzisen Berechnung deines Body Fat Index (BFI). Anhand von Eingaben zu Gewicht, Grösse sowie Taillenumfang, Handgelenkumfang, Hüftumfang und Unterarmumfang erhältst du eine detaillierte Auswertung deiner Körperzusammensetzung. Die strukturierte Darstellung der Ergebnisse unterstützt dich dabei, deinen aktuellen Fitnesszustand besser zu verstehen und gezielt an deinen Gesundheitszielen zu arbeiten.")

st.write("🏃💪🍎📊🏋️‍♀️🥗")

st.write("Diese App wurde von Adriana Heeb entwickelt.")
st.write("E-Mail Adresse: heebadr1@students.zhaw.ch")


