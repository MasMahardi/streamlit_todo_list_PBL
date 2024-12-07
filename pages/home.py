import json
import streamlit as st
from pathlib import Path
from streamlit_lottie import st_lottie


# Function to load Lottie animation files
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


# Load Lottie animation
lottie_file = load_lottiefile("./file/animation_1.json")

# Intro section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.title("MY :blue[_COOL TO DO LIST APP_] :sunglasses:")
with col2:
    st_lottie(
        lottie_file,
        speed=1,
        reverse=False,
        loop=True,
        quality="low",  # medium ; high # canvas
        key=None,
        height=175,
        width=350,
    )

# Input user's name
name = st.text_input("Please input your name here")
if name:
    st.subheader(f"This is {name}'s To-Do List App")
else:
    st.write("Welcome! Please enter your name to get started.")

st.write("----------------------------------------------------")

# Initialize session state variables for each day
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for day in DAYS:
    if f"todolist_{day}" not in st.session_state:
        st.session_state[f"todolist_{day}"] = []
    if f"checkbox_states_{day}" not in st.session_state:
        st.session_state[f"checkbox_states_{day}"] = {}

# Function to add a to-do item
def add_todo_to_list(day):
    todo = st.session_state[f"new_todo_input_{day}"].strip()
    if todo:  # Don't add empty todos
        st.session_state[f"todolist_{day}"].append(todo)
        st.session_state[f"checkbox_states_{day}"][todo] = False


# Function to reset the to-do list for a specific day
def reset_todo_list(day):
    st.session_state[f"todolist_{day}"] = []
    st.session_state[f"checkbox_states_{day}"] = {}


# Divide days into two rows of columns
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

# Map columns to days
columns = [col1, col2, col3, col4, col5]
for col, day in zip(columns, DAYS):
    with col:
        st.subheader(f"{day}'s To-Do List")
        with st.form(f"To Do List {day}"):
            st.text_input(
                label=f"Enter a to-do for {day}:",
                placeholder="What is your next task?",
                key=f"new_todo_input_{day}",
            )
            if st.form_submit_button("Submit"):
                add_todo_to_list(day)

        # Display the to-do list with checkboxes
        for todo in st.session_state[f"todolist_{day}"]:
            is_checked = st.checkbox(
                label=f"{todo}" if not st.session_state[f"checkbox_states_{day}"][todo] else f"~~{todo}~~",
                value=st.session_state[f"checkbox_states_{day}"][todo],
                key=f"checkbox_{day}_{todo}",
            )
            st.session_state[f"checkbox_states_{day}"][todo] = is_checked

        # Add a "Start Over" button to reset the day's list
        st.button(f"Start Over {day}", on_click=reset_todo_list, args=(day,))
