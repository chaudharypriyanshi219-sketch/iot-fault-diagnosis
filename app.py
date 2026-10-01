import streamlit as st
import sqlite3
import pandas as pd
import time

st.set_page_config(
    page_title="IoT Fault Diagnosis",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Knowledge-Driven IoT Fault Diagnosis")

st.write(
    "Real-Time Monitoring and Fault Diagnosis Dashboard"
)


# Database connection
conn = sqlite3.connect("iot_faults.db")

query = """
SELECT
    id,
    temperature,
    vibration,
    current,
    rpm,
    fault
FROM sensor_data
ORDER BY id DESC
LIMIT 50
"""

df = pd.read_sql_query(query, conn)

conn.close()


# Dashboard
if len(df) > 0:

    latest = df.iloc[0]

    st.subheader("Current Machine Status")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Temperature",
        f"{latest['temperature']:.2f} °C"
    )

    col2.metric(
        "Vibration",
        f"{latest['vibration']:.2f}"
    )

    col3.metric(
        "Current",
        f"{latest['current']:.2f} A"
    )

    col4.metric(
        "RPM",
        f"{latest['rpm']:.0f}"
    )


    st.divider()

    st.subheader("🔍 Fault Diagnosis")

    fault = latest["fault"]

    if fault == "Normal":

        st.success("Machine Status: NORMAL")

    elif "Critical" in fault:

        st.error(
            f"Machine Status: {fault}"
        )

    else:

        st.warning(
            f"Machine Status: {fault}"
        )


    st.divider()

    st.subheader("📊 Sensor Data")

    st.dataframe(
        df,
        use_container_width=True
    )


    st.subheader("🌡️ Temperature")

    st.line_chart(
        df.set_index("id")["temperature"]
    )


    st.subheader("📳 Vibration")

    st.line_chart(
        df.set_index("id")["vibration"]
    )


    st.subheader("⚡ Motor Current")

    st.line_chart(
        df.set_index("id")["current"]
    )


else:

    st.info(
        "Waiting for IoT sensor data..."
    )