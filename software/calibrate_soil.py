"""
calibrate_soil.py — KrishiMitra AI
Run this ONLY on the Raspberry Pi to find real DRY_THRESHOLD / WET_THRESHOLD values
for soil_sensor.py. Move the sensor between conditions (dry air, water, dry soil, wet soil)
and log readings for each.
"""
from soil_sensor import read_adc

print("Calibration mode. Move sensor between conditions and press Enter to log a reading.")
print("Try: dry_air, water, dry_soil, wet_soil, moist_soil")
while True:
    label = input("Label this reading (or 'q' to quit): ")
    if label == 'q':
        break
    val = read_adc()
    print(f"  {label}: {val}")
