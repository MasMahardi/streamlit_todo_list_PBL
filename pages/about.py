
import streamlit as st
from PIL import Image

st.title("About Me")

image = Image.open("./file/profpic.jpeg")
st.image(image, width= 400)

st.subheader("*Mahardi Setyoso Pratomo*")
st.write("Linkedin [link](https://www.linkedin.com/in/mahardi-setyoso-pratomo-5ab97432/)")
st.write("Github [link](https://github.com/mahardisetyoso)")
st.write("Email: [mahardisetyoso@gmail.com]")