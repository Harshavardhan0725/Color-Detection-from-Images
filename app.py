# Color-Detection-from-Images
# app.py
import cv2
import pandas as pd
import streamlit as st
import numpy as np

# Load color dataset
@st.cache_data
def load_colors():
    return pd.read_csv('colors.csv')

colors_df = load_colors()

# Find the closest color name
def get_closest_color(R, G, B):
    minimum = float('inf')
    cname = ""
    for i in range(len(colors_df)):
        d = abs(R - int(colors_df.loc[i, "R"])) + abs(G - int(colors_df.loc[i, "G"])) + abs(B - int(colors_df.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = colors_df.loc[i, "Color Name"]
    return cname

# App title
st.title("🎨 Color Detection App")
st.write("Upload an image and click on any part to detect the color.")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    st.write("Click on the image below to detect color:")
    clicked = st.image(img, use_column_width=True)

    st.write("Due to limitations in Streamlit, click-based pixel detection is simplified in this prototype. "
             "Consider using OpenCV UI locally for precise coordinates.")
