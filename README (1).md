
# 🔥 Fire Prediction from Images using Deep Learning

This project involves predicting the presence of fire in images using Convolutional Neural Networks (CNNs). The goal is to classify images as **"Fire"** or **"No Fire"**, which can be useful in early detection systems for wildfire management, surveillance systems, and industrial safety.

---

## 📁 Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [Data Preprocessing](#data-preprocessing)
- [Model Architecture](#model-architecture)
- [Evaluation](#evaluation)
- [How to Run](#how-to-run)
- [Future Work](#future-work)
- [Contact](#contact)

---

## 🧠 Overview

The system classifies images into two categories:
- 🔥 Fire
- 🌲 No Fire

The model is trained on a dataset of images and utilizes a Convolutional Neural Network to learn fire-related features such as flame color, shape, and texture.

---

## 🔍 Problem Statement

Traditional fire detection systems are either sensor-based or manually monitored. These methods may delay response time. The aim of this project is to develop an automated, image-based fire detection system that can provide instant alerts.

---

## ⚙️ Tech Stack

- Python
- TensorFlow / Keras
- OpenCV
- NumPy, Matplotlib
- Jupyter Notebook

---

## 📊 Dataset

- **Source**: [Kaggle]
- **Classes**: Fire, No Fire
- **Images**: [Number] images in total
- Images include forests, urban environments, and industrial scenes.

Directory structure:
```
fire-dataset/
│
├── train/
│   ├── fire/
│   └── no_fire/
│
├── test/
│   ├── fire/
│   └── no_fire/
```

---

## 🧹 Data Preprocessing

- Image resizing to 224x224
- Normalization / Rescaling
- Data Augmentation: Rotation, flipping, zoom, etc.
- Train-Test split (80-20)

---

## 🧠 Model Architecture

- Input: 224x224 RGB image
- CNN layers with ReLU activation
- MaxPooling layers
- Flatten layer
- Dense layers with Dropout
- Output:  Softmax for binary classification


## 📈 Evaluation

- Accuracy
- Confusion Matrix
- Precision, Recall, F1-Score
- ROC Curve

Best Model Performance:
- **Accuracy**: XX%
- **Loss**: XX
- **F1 Score**: XX



---

## 🔮 Future Work

- Integrate live camera feed (e.g., CCTV, drone)
- Real-time alert system
- Expand to multi-class detection (smoke, fire intensity, etc.)

---

## 📬 Contact

**Yashwanth P B**  
📧 yashwanthx23@gmail.com 
📱 [LinkedIn](linkedin.com/in/yashwanth-pb-947aab2a9)
