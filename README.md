# 🧠 One Pixel Attack on ResNet18 – Web App Interface

This project demonstrates a **One Pixel Adversarial Attack** on a ResNet18 image classifier. A web-based interface allows users to upload an image, apply the attack using Python + PyTorch, and download the altered adversarial image.

## 📌 What is the One Pixel Attack?

The **One Pixel Attack** was introduced by **Jiawei Su, Danilo Vasconcellos Vargas, and Kohichi Sakurai** in their 2017 paper:  
👉 *"One Pixel Attack for Fooling Deep Neural Networks"*  
It shows that even changing **a single pixel** in an image can be enough to fool a deep neural network into making incorrect predictions — raising serious concerns for the robustness and security of AI systems.

## 🛠️ Features

- ✔️ Python script using **PyTorch** to perform the One Pixel Attack on **ResNet18**
- ✔️ **PHP-based web application** for uploading images and viewing results
- ✔️ Saves the adversarial image and shows the original vs. perturbed predictions
- ✔️ Lightweight and easy to run locally

## 📷 Example

| Original Image | Adversarial Image |
|----------------|-------------------|
| ![original](assets/original.jpg) | ![attacked](assets/adversarial.jpg) |

*(Images above are just placeholders — replace with actual results)*

---

## ⚙️ How It Works

1. **User uploads an image** via the web interface.
2. The PHP backend sends the image to a **Python script**.
3. The Python script runs the **One Pixel Attack** on a pretrained **ResNet18 model**.
4. The adversarial image is saved and displayed on the frontend with prediction results.

---

## 🚀 Getting Started

### 🧩 Prerequisites

- PHP (CLI or local server)
- Python 3.8+
- pip packages: `torch`, `torchvision`, `Pillow`, `numpy`, `matplotlib`

### 📦 Installation

```bash
git clone https://github.com/your-username/one-pixel-attack-webapp.git
cd one-pixel-attack-webapp
