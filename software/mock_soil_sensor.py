"""
mock_soil_sensor.py — KrishiMitra AI
Simulates soil moisture readings for development without real MCP3008/sensor hardware.
Once hardware arrives, replace read_moisture() with real SPI/MCP3008 ADC reads.
"""
import random


def read_moisture():
    """
    Mock reading: returns a simulated raw ADC value (0-1023, matching MCP3008's 10-bit range)
    and a classified moisture level.
    """
    raw_value = random.randint(0, 1023)
    return raw_value, classify_moisture(raw_value)


def classify_moisture(raw_value):
    """
    Classifies a raw ADC reading into Dry / Moderate / Wet.
    Thresholds are placeholders — calibrate against the real sensor once hardware arrives,
    since capacitive sensor output varies by soil type and sensor unit.
    """
    if raw_value > 700:
        return "Dry"
    elif raw_value > 400:
        return "Moderate"
    else:
        return "Wet"


if __name__ == "__main__":
    raw, level = read_moisture()
    print(f"[MOCK SENSOR] Raw ADC value: {raw} -> {level}")
