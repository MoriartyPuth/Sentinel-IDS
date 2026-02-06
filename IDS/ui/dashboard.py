import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import time

st.set_page_config(page_title="Sentinel SOC", layout="wide", page_icon="🛡️")

# --- SETTINGS ---
REFRESH_INTERVAL = 5 

def load_data():
    try:
        conn = sqlite3.connect('data/ids_logs.db')
        df = pd.read_sql("SELECT * FROM alerts", conn)
        conn.close()
        
        if not df.empty:
            # Fix: Ensure column names match your DB and convert to datetime
            df['timestamp'] = pd.to_datetime(df['timestamp'])
        return df
    except Exception as e:
        st.error(f"Database Error: {e}")
        return pd.DataFrame()

# --- HEADER ---
st.title("🛡️ Sentinel Real-Time SOC Dashboard")
st.markdown(f"Last updated: `{time.strftime('%H:%M:%S')}` (Auto-refreshes every {REFRESH_INTERVAL}s)")

# --- LOAD DATA ---
df = load_data()

if not df.empty:
    # 1. METRICS ROW
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Threats", len(df))
    
    with col2:
        # Corrected time comparison
        one_hour_ago = pd.Timestamp.now() - pd.Timedelta(hours=1)
        recent_count = len(df[df['timestamp'] > one_hour_ago])
        st.metric("Alerts (Last Hour)", recent_count)
    
    with col3:
        st.metric("Unique Attackers", df['ip'].nunique())

    # 2. MAP VISUALIZATION
    st.subheader("🌍 Global Threat Map")
    # Note: Ensure your DB has lat/lon columns or this will error!
    fig = px.scatter_mapbox(df, 
                            lat="lat", lon="lon", 
                            color="attack_type", 
                            size_max=15, zoom=1,
                            mapbox_style="carto-darkmatter",
                            hover_name="ip",
                            template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

    # 3. DATA TABLE
    st.subheader("📑 Recent Events Log")
    st.dataframe(df.sort_values(by="timestamp", ascending=False), use_container_width=True)

else:
    st.info("🛰️ Scanning network... No threats detected in database yet.")

# --- AUTO-REFRESH ---
time.sleep(REFRESH_INTERVAL)
st.rerun()