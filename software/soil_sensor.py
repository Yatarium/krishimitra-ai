"""
soil_sensor.py — KrishiMitra AI
Real MCP3008 ADC reading. Run this ONLY on the Raspberry Pi (needs spidev + wired MCP3008).
Install: sudo apt install -y python3-spidev && pip install spidev
"""
import spidev

spi = spidev.SpiDev()
spi.open(0, 0)  # bus 0, device 0 — adjust if wired differently
spi.max_speed_hz = 1350000

# Calibrate these using calibrate_soil.py before relying on real readings
DRY_THRESHOLD = 700
WET_THRESHOLD = 400

def read_adc(channel=0):
    if not 0 <= channel <= 7:
        raise ValueError("MCP3008 channel must be 0-7")
    cmd = 0b11 << 6 | channel << 3
    adc = spi.xfer2([1, cmd, 0])
    value = ((adc[1] & 0x0F) << 8) | adc[2]
    return value  # 0-1023

def classify_moisture(raw_value, dry_threshold=DRY_THRESHOLD, wet_threshold=WET_THRESHOLD):
    if raw_value > dry_threshold:
        return "Dry"
    elif raw_value > wet_threshold:
        return "Moderate"
    else:
        return "Wet"

def read_moisture():
    raw = read_adc()
    return raw, classify_moisture(raw)

if __name__ == "__main__":
    raw, level = read_moisture()
    print(f"Raw ADC value: {raw} -> {level}")
