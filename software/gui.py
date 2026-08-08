"""
gui.py — KrishiMitra AI
Farmer-facing interface: capture -> predict -> translate -> speak, plus soil moisture display.
Simple Tkinter GUI, designed for a small Pi-connected touchscreen/display.
NOTE: Rishabh may take over/extend this file for the real hardware-facing GUI.
"""
import tkinter as tk
from tkinter import messagebox

from inference import predict
from translate import translate_disease
from tts import speak
from mock_camera import capture_image
from mock_soil_sensor import read_moisture


def run_diagnosis():
    try:
        image_path = capture_image()
        result = predict(image_path)
        hindi_name = translate_disease(result["disease"])

        result_label.config(
            text=f"{hindi_name}\n(Confidence: {result['confidence']*100:.1f}%)"
        )
        speak(hindi_name)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def check_soil():
    raw, level = read_moisture()
    soil_label.config(text=f"Soil Moisture: {level} (raw: {raw})")
    speak(f"मिट्टी की नमी: {level}")


root = tk.Tk()
root.title("KrishiMitra AI")
root.geometry("480x320")  # rough size for a small Pi touchscreen

title = tk.Label(root, text="कृषिमित्र AI", font=("Arial", 20, "bold"))
title.pack(pady=10)

diagnose_btn = tk.Button(root, text="पत्ता जांचें (Check Leaf)", font=("Arial", 14), command=run_diagnosis)
diagnose_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400)
result_label.pack(pady=10)

soil_btn = tk.Button(root, text="मिट्टी जांचें (Check Soil)", font=("Arial", 14), command=check_soil)
soil_btn.pack(pady=10)

soil_label = tk.Label(root, text="", font=("Arial", 14))
soil_label.pack(pady=10)

if __name__ == "__main__":
    root.mainloop()
