"""
test_real_accuracy.py — KrishiMitra AI
Run this ONLY on the Raspberry Pi (or any machine with inference.py's dependencies).
Organize test photos as: test_photos/<true_label>/<image>.jpg
where <true_label> matches a key in class_indices.json.
"""
import os
from inference import predict

TEST_DIR = "test_photos"

correct = 0
total = 0

for true_label in os.listdir(TEST_DIR):
    label_dir = os.path.join(TEST_DIR, true_label)
    if not os.path.isdir(label_dir):
        continue
    for img_file in os.listdir(label_dir):
        img_path = os.path.join(label_dir, img_file)
        result = predict(img_path)
        is_correct = result["disease"] == true_label
        correct += is_correct
        total += 1
        print(f"{img_file}: predicted={result[\'disease\']} ({result[\'confidence\']*100:.1f}%) "
              f"true={true_label} {chr(0x2713) if is_correct else chr(0x2717)}")

if total > 0:
    print(f"\nAccuracy: {correct}/{total} ({100*correct/total:.1f}%)")
else:
    print("No test images found. Check TEST_DIR structure.")
