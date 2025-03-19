from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

# ------------------------------------------------------------
# Here starts the actual app, which was developed previously
import streamlit as st
import pandas as pd

st.title('BFI Werte')

data_df = st.session_state.get('data_df', pd.DataFrame())
if data_df.empty:
    st.info('Keine BFI Daten vorhanden. Berechnen Sie Ihren BFI auf der Startseite.')
    st.stop()

# Ensure the 'timestamp' column exists and is of datetime type
if 'timestamp' in data_df.columns:
    data_df['timestamp'] = pd.to_datetime(data_df['timestamp'], errors='coerce')
    data_df = data_df.dropna(subset=['timestamp'])
    data_df = data_df.sort_values('timestamp', ascending=False)
else:
    st.error('Die Spalte "timestamp" fehlt in den Daten.')
    st.stop()

# Display table
st.dataframe(data_df)