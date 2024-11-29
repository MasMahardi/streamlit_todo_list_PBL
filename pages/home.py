import json
import streamlit as st
from pathlib import Path
from streamlit_lottie import st_lottie

# function for load lottiefiles
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
lottie_file = load_lottiefile("https://github.com/MasMahardi/streamlit_todo_list_PBL/blob/main/file/animation_1.json")

# intro page
st.title("MY :blue[_TO DO LIST APP_] :sunglasses:")
name = st.text_input("Please input your name here",)

if name != "":
    st.subheader(f"This is {name} 's To Do List Apps")
else:
    None

st_lottie(
    lottie_file,
    speed=0,
    reverse=False,
    loop=True,
    quality="low", # medium ; high # canvas
    key=None,
)

