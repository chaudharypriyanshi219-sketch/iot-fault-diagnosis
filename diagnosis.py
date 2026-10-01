def diagnose(temperature, vibration, current, rpm):

    if temperature > 80 and vibration > 4:
        return "Critical Motor/Bearing Fault"

    elif temperature > 80:
        return "Overheating"

    elif vibration > 4:
        return "Excessive Vibration"

    elif current > 8:
        return "Motor Overload"

    elif rpm < 1200:
        return "Low RPM"

    else:
        return "Normal"