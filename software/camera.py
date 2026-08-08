"""
camera.py — KrishiMitra AI
Real Pi Camera capture. Run this ONLY on the Raspberry Pi (needs picamera2 + physical camera).
Install: sudo apt install -y python3-picamera2
"""
from picamera2 import Picamera2
import time

def capture_image(save_path="captured_leaf.jpg"):
    picam2 = Picamera2()
    config = picam2.create_still_configuration(main={"size": (1024, 768)})
    picam2.configure(config)
    picam2.start()
    time.sleep(2)  # let auto-exposure/focus settle
    picam2.capture_file(save_path)
    picam2.stop()
    print(f"Captured: {save_path}")
    return save_path

if __name__ == "__main__":
    capture_image()
