import streamlit as st
import warnings
warnings.filterwarnings("ignore")
import tensorflow as tf

import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
# Load your saved model
model = tf.keras.models.load_model("/mnt/c/Users/abhis/Downloads/best_model.h5")
  # change path if needed
class_names = ["Cassava Bacterial Blight (CBB)" , "Cassava Brown Streak Disease (CBSD)" , "Cassava Green Mottle (CGM)", "Cassava Mosaic Disease (CMD)", "Healthy"]  # your labels here

st.title("🌿 Plant disease detection")

uploaded_file = st.file_uploader("Upload an image for prediction", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Preprocess the image
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # Make prediction
    prediction = model.predict(img_array)
    pred_idx = int(np.argmax(prediction))

    if pred_idx < len(class_names):
        predicted_class = class_names[pred_idx]
    else:
        predicted_class = f"Unknown (index {pred_idx})"

    st.success(f"Prediction: {predicted_class}")

    

