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
st.title("BFI-App")
st.write("Diese Streamlit-App bietet eine einfache Möglichkeit, den Körperfettanteil zu berechnen, basierend auf grundlegenden persönlichen Angaben wie Grösse, Gewicht, Alter, Geschlecht sowie Aktivitätslevel. Die benutzerfreundliche Oberfläche ermöglicht es, eine erste Einschätzung der Körperzusammensetzung schnell zu erhalten.")
st.write("🏃")

st.write("Diese App wurde von Adriana Heeb entwickelt.")
st.write("E-Mail Adresse: heebadr1@students.zhaw.ch")


