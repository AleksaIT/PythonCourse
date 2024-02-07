import streamlit as st
from PIL import Image

with st.expander("Start camera"):
    #Start a camera
    camera_image = st.camera_input("Camera")

if camera_image:
    #Create a pillow image instance
    img = Image.open(camera_image)

    #Convert the pillow image into grey scale
    gray_img = img.convert("L")

    #Render the greyscale image on webpage
    st.image(gray_img)