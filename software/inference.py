"""
inference.py — KrishiMitra AI
Loads the TFLite model and runs disease prediction on a single leaf image.
"""
import json
import numpy as np
from PIL import Image

try:
    import tflite_runtime.interpreter as tflite
except ImportError:
    import tensorflow.lite as tflite  # fallback for dev machines with full TF installed

MODEL_PATH = "models/krishimitra_model.tflite"
CLASS_INDICES_PATH = "models/class_indices.json"
IMG_SIZE = (224, 224)


def load_class_names(path=CLASS_INDICES_PATH):
    with open(path, "r") as f:
        class_indices = json.load(f)
    return {v: k for k, v in class_indices.items()}


def preprocess_image(image_path):
    img = Image.open(image_path).convert("RGB").resize(IMG_SIZE)
    arr = np.asarray(img, dtype=np.float32) / 255.0
    arr = np.expand_dims(arr, axis=0)
    return arr


def predict(image_path, model_path=MODEL_PATH):
    interpreter = tflite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    index_to_class = load_class_names()
    img_array = preprocess_image(image_path)

    interpreter.set_tensor(input_details[0]["index"], img_array)
    interpreter.invoke()
    predictions = interpreter.get_tensor(output_details[0]["index"])[0]

    top_index = int(np.argmax(predictions))
    confidence = float(predictions[top_index])
    disease_name = index_to_class[top_index]

    return {"disease": disease_name, "confidence": round(confidence, 4)}


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python inference.py <path_to_leaf_image>")
        sys.exit(1)

    result = predict(sys.argv[1])
    print(f"Prediction: {result[\'disease\']} (confidence: {result[\'confidence\']})")
