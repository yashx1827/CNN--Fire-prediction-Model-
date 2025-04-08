import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import base64
import io

st.set_page_config(page_title="Fire Detection AI", page_icon="🔥", layout="wide")

def set_background(image_path):
    with open(image_path, "rb") as img_file:
        encoded_img = base64.b64encode(img_file.read()).decode()
    bg_image = f"""
    <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_img}");
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
            background-position: center;
        }}
        .title {{
            text-align: center;
            font-size: 50px;
            font-weight: bold;
            color: white;
            text-shadow: 3px 3px 12px red;
            margin-top: 20px;
        }}
        .slogan {{
            text-align: center;
            font-size: 24px;
            font-style: italic;
            color: white;
            text-shadow: 2px 2px 8px orange;
            margin-top: 10px;
        }}
    </style>
    """
    st.markdown(bg_image, unsafe_allow_html=True)
    st.markdown(bg_image, unsafe_allow_html=True)

set_background(r"C:\data\landscape-smoke-forest-wallpaper.jpg")

@st.cache_resource
def load_model():
    model_path = r"C:\python\fire_prediction_model.h5"  
    model = tf.keras.models.load_model(model_path)
    return model

model = load_model()

class_names = ["Fire", "Non-Fire"]  

def preprocess_image(image, img_shape=224):
    """Prepares an image for model prediction."""
    image = image.convert("RGB")  
    image = image.resize((img_shape, img_shape))  
    image = np.array(image, dtype=np.float32) / 255.0  
    image = np.expand_dims(image, axis=0)  
    return image

st.markdown('<h1 class="title">Fire Detection AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="slogan">"Only You Can Prevent Forest Fires!"</p>', unsafe_allow_html=True)
st.markdown('<p class="slogan">"Act Before It Turns to Ashes!"</p>', unsafe_allow_html=True)

st.write("### Upload an image to check if it contains **Fire or Non-Fire.**")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)

    img_width, img_height = image.size
    max_display_width = 500  
    if img_width > max_display_width:
        scale_ratio = max_display_width / img_width
        new_height = int(img_height * scale_ratio)
        image_resized = image.resize((max_display_width, new_height))
    else:
        image_resized = image

    st.image(image_resized, caption="Uploaded Image (Resized for display)", use_column_width=False)

    processed_img = preprocess_image(image)
    prediction = model.predict(processed_img)
    pred_index = np.argmax(prediction)  
    pred_class = class_names[pred_index]
    confidence = np.max(prediction) * 100  


    if pred_class == "Fire":
        st.error(f"🔥 **Fire Detected!**\n🚨 Take necessary precautions!\n🔥 Confidence: {confidence:.2f}%")
    else:
        st.success(f"✅ **No Fire Detected. Stay Safe!**\n🌿 Confidence: {confidence:.2f}%")
