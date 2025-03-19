# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

# ------------------------------------------------------------
# === BFI Grafik ===
import streamlit as st
import pandas as pd  # Pandas importieren

st.title('BFI Verlauf')

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

# Check if required columns exist
required_columns = ['weight', 'height', 'bmi']
missing_columns = [col for col in required_columns if col not in data_df.columns]

if missing_columns:
    st.error(f'Die folgenden Spalten fehlen in den Daten: {", ".join(missing_columns)}')
    st.stop()

# Weight over time
st.line_chart(data=data_df.set_index('timestamp')['weight'], 
                use_container_width=True)
st.caption('Gewicht über Zeit (kg)')

# Height over time 
st.line_chart(data=data_df.set_index('timestamp')['height'],
                use_container_width=True)
st.caption('Größe über Zeit (m)')

# BMI over time
st.line_chart(data=data_df.set_index('timestamp')['bmi'],
                use_container_width=True)
st.caption('BMI über Zeit')