"""
mock_camera.py — KrishiMitra AI
Simulates leaf image capture for development without real Pi Camera hardware.
Once hardware arrives, replace capture_image() with real picamera2 calls.
"""
import os
import random


MOCK_IMAGE_DIR = "data/sample_leaves"  # place a few sample leaf images here for testing


def capture_image(save_path="captured_leaf.jpg"):
    """
    Mock capture: picks a random sample image instead of using a real camera.
    Returns the path to the 'captured' image.
    """
    if not os.path.isdir(MOCK_IMAGE_DIR):
        raise FileNotFoundError(
            f"{MOCK_IMAGE_DIR} not found. Add a few sample leaf images there for mock testing."
        )

    samples = [f for f in os.listdir(MOCK_IMAGE_DIR) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    if not samples:
        raise FileNotFoundError(f"No sample images found in {MOCK_IMAGE_DIR}.")

    chosen = random.choice(samples)
    src_path = os.path.join(MOCK_IMAGE_DIR, chosen)

    # In real deployment this would come from the camera; here we just return the sample path
    print(f"[MOCK CAMERA] Simulated capture: {chosen}")
    return src_path


if __name__ == "__main__":
    path = capture_image()
    print(f"Captured image path: {path}")
