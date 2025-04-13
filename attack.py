import sys
import os
from PIL import Image
import numpy as np
import torch
import torch.nn.functional as F
import torchvision.transforms as transforms
import torchvision.models as models
from scipy.optimize import differential_evolution

# Paths
input_path = sys.argv[1]
output_path = sys.argv[2]

# Resize to 224x224 for ResNet18
img = Image.open(input_path).convert('RGB').resize((224, 224))
image_np = np.asarray(img) / 255.0

# Load ResNet18
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
model.eval()

def predict(img):
    img_tensor = torch.tensor(img.transpose(2, 0, 1)).unsqueeze(0).float()
    output = model(img_tensor)
    probs = F.softmax(output, dim=1)
    return probs.detach().numpy()

def attack(pixel, image, target_label):
    img_copy = image.copy()
    x, y, r, g, b = map(int, pixel)
    img_copy[y, x] = [r / 255.0, g / 255.0, b / 255.0]
    prediction = predict(img_copy)
    return -prediction[0][target_label]

# Original prediction
original_pred = predict(image_np)
true_label = np.argmax(original_pred)

print("Original label:", true_label)

bounds = [(0, 223), (0, 223), (0, 255), (0, 255), (0, 255)]

# Run differential evolution
result = differential_evolution(
    func=attack,
    bounds=bounds,
    args=(image_np.copy(), true_label),
    maxiter=20,
    popsize=5,
    tol=1e-3
)

# Apply best pixel modification
x, y, r, g, b = [int(v) for v in result.x]
perturbed = image_np.copy()
perturbed[y, x] = [r / 255.0, g / 255.0, b / 255.0]

# Save output
os.makedirs(os.path.dirname(output_path), exist_ok=True)
Image.fromarray((perturbed * 255).astype(np.uint8)).save(output_path)
print("✅ Attacked image saved:", output_path)
