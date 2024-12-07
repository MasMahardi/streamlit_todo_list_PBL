from pathlib import Path
import streamlit as st
from PIL import Image

st.title("About Me")

current_dir = Path(__file__).parent if "_file_" in locals() else Path.cwd()
profile_pic = current_dir / "file" / "profpic.jpeg"

image = Image.open(profile_pic)
st.image(image, width= 400)

st.subheader("*Mahardi Setyoso Pratomo*")
st.write("Linkedin [link](https://www.linkedin.com/in/mahardi-setyoso-pratomo-5ab97432/)")
st.write("Github [link](https://github.com/mahardisetyoso)")
st.write("Email: [mahardisetyoso@gmail.com]")