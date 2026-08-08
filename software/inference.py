"""

inference.py — KrishiMitra AI

Loads the trained model and runs disease prediction on a single leaf image.

"""

import json

import numpy as np

from tensorflow.keras.models import load_model

from tensorflow.keras.preprocessing.image import load_img, img_to_array

MODEL_PATH = "models/finetune_best.keras"   # swap to .tflite path once exported

CLASS_INDICES_PATH = "models/class_indices.json"

IMG_SIZE = (224, 224)

def load_class_names(path=CLASS_INDICES_PATH):

    with open(path, "r") as f:

        class_indices = json.load(f)

    # invert: {0: 'Potato___Early_blight', ...}

    return {v: k for k, v in class_indices.items()}

def preprocess_image(image_path):

    img = load_img(image_path, target_size=IMG_SIZE)

    arr = img_to_array(img)

    arr = arr / 255.0                      # match training rescale=1./255

    arr = np.expand_dims(arr, axis=0)      # add batch dimension

    return arr

def predict(image_path, model_path=MODEL_PATH):

    model = load_model(model_path)

    index_to_class = load_class_names()

    img_array = preprocess_image(image_path)

    predictions = model.predict(img_array)[0]   # shape: (28,)

    top_index = int(np.argmax(predictions))

    confidence = float(predictions[top_index])

    disease_name = index_to_class[top_index]

    return {

        "disease": disease_name,

        "confidence": round(confidence, 4)

    }

if __name__ == "__main__":

    import sys

    if len(sys.argv) != 2:

        print("Usage: python inference.py <path_to_leaf_image>")

        sys.exit(1)

    result = predict(sys.argv[1])

    print(f"Prediction: {result['disease']} (confidence: {result['confidence']})")