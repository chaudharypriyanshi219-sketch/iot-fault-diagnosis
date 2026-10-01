import random
import time
from database import create_database, insert_data
from diagnosis import diagnose

create_database()

print("IoT Sensor Started...")

while True:

    temperature = round(random.uniform(40, 95), 2)
    vibration = round(random.uniform(0.1, 5.5), 2)
    current = round(random.uniform(2, 10), 2)
    rpm = random.randint(1000, 3000)

    fault = diagnose(
        temperature,
        vibration,
        current,
        rpm
    )

    insert_data(
        temperature,
        vibration,
        current,
        rpm,
        fault
    )

    print("--------------------------------")
    print("Temperature:", temperature)
    print("Vibration:", vibration)
    print("Current:", current)
    print("RPM:", rpm)
    print("Diagnosis:", fault)

    time.sleep(3)