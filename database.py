import sqlite3

DB_NAME = "iot_faults.db"


def create_database():
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperature REAL,
            vibration REAL,
            current REAL,
            rpm REAL,
            fault TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_data(temperature, vibration, current, rpm, fault):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO sensor_data
        (temperature, vibration, current, rpm, fault)
        VALUES (?, ?, ?, ?, ?)
    """, (temperature, vibration, current, rpm, fault))

    conn.commit()
    conn.close()


def get_data():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM sensor_data
        ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data