import pandas as pd
import streamlit as st
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

# Initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="BMLD_LN 2")

# Initialize the login manager
login_manager = LoginManager(data_manager)
login_manager.login_register()  # Open login/register page

# Define file name
file_name = 'data.csv'

# Check if the file exists using data_manager's file system
try:
    existing_files = data_manager.list_files()  # Get list of available files
    if file_name in existing_files:
        data_manager.load_user_data(
            session_state_key='data_df', 
            file_name=file_name, 
            initial_value=pd.DataFrame(), 
            parse_dates=['timestamp']
        )
    else:
        st.warning("Die Datei 'data.csv' wurde nicht gefunden. Eine neue Datei wird erstellt.")
        empty_df = pd.DataFrame(columns=['timestamp'])
        data_manager.save_user_data(empty_df, file_name)
        data_manager.load_user_data(
            session_state_key='data_df',
            file_name=file_name,
            initial_value=empty_df
        )
except Exception as e:
    st.error(f"Fehler beim Zugriff auf die Datei: {e}")

# Streamlit UI
st.title("BFI-App")
st.write("Diese Streamlit-App bietet eine einfache Möglichkeit, den Körperfettanteil zu berechnen, basierend auf grundlegenden persönlichen Angaben wie Grösse, Gewicht, Alter, Geschlecht sowie Aktivitätslevel. Die benutzerfreundliche Oberfläche ermöglicht es, eine erste Einschätzung der Körperzusammensetzung schnell zu erhalten.")
st.write("🏃")

st.write("Diese App wurde von Adriana Heeb entwickelt.")
st.write("E-Mail Adresse: heebadr1@students.zhaw.ch")


