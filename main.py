import streamlit as st
import streamlit_lottie
from pathlib import Path

from streamlit import title

# PATH Setting
current_dir = Path(__file__).parent if "_file_" in locals() else Path.cwd()
home_page = current_dir/"pages"/"home.py"
about_me = current_dir/"pages"/"about.py"


# page setup
pages ={
    "To Do List Activity":[
        st.Page(home_page, title="Home"),
    ],
    "About me":[
        st.Page(about_me, title="About me")
    ]
}

if __name__ == "__main__":
    pg = st.navigation(pages)
    pg.run()
