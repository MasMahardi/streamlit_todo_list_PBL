import streamlit as st
from pathlib import Path

# PATH Setting
current_dir = Path(__file__).parent if "_file_" in locals() else Path.cwd()
home_page = current_dir/"pages"/"home.py"
create_page = current_dir/"pages"/"crud.py"
test_page = current_dir/"pages"/"logic_test.py"

# page setup
pages ={
    "Home":[
        st.Page(home_page, title="Home"),
    ],
    "To Do List Activity":[
        st.Page(create_page, title="Create Read Update Delete Feature")
    ]

}


pg = st.navigation(pages)
pg.run()
