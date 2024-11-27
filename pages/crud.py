import streamlit as st
import pandas as pd

col1, col2 = st.columns(2, gap="small")
with col1:
    activity_1 = st.text_input("Put your to do list 1")
    activity_2 = st.text_input("Put your to do list 2")
    activity_3 = st.text_input("Put your to do list 3")
    activity_4 = st.text_input("Put your to do list 4")
    activity = [activity_1,activity_2,activity_3,activity_4]
with col2:
    day_1 = st.text_input("Put your day 1")
    day_2 = st.text_input("Put your day 2")
    day_3 = st.text_input("Put your day 3")
    day_4 = st.text_input("Put your day 4")
    day = [day_1,day_2,day_3,day_4]

table_1 = pd.DataFrame(columns=['To Do'])
table_2 = pd.DataFrame(columns=['Day'])

for i in activity:
    table_1.loc[len(table_1)] = [i]

for y in day:
    table_2.loc[len(table_2)] = [y]
table = pd.concat([table_1,table_2], axis = 1)

st.write("#")
if "table" not in st.session_state:
    st.session_state.table = table
elif "st.session_state.table_2" not in st.session_state:
    st.session_state.table_2 = st.session_state.table
elif "st.session_state.table_3" not in st.session_state:
    st.session_state.table_3 = st.session_state.table_2

left,right = st.columns(2)
if left.button("Create To Do List", use_container_width=True):
    left.markdown("You add all To Do List.")
    st.dataframe(table, use_container_width=True)
if right.button("Reset", icon=":material/mood:", use_container_width=True):
    right.markdown("You reset all To Do List.")
    table = pd.DataFrame(columns=table.columns)
    st.dataframe(table, use_container_width=True)

st.write("#")
left,middle,right = st.columns(3)
if left.button("Delete Index 1", use_container_width=True):
    st.session_state.table = table.drop(index=1)
    st.dataframe(st.session_state.table, use_container_width=True)
if middle.button("Delete Index 2", use_container_width=True):
    st.session_state.table_2 = st.session_state.table.drop(index=2)
    st.dataframe(st.session_state.table_2, use_container_width=True)
if right.button("Delete Index 3", use_container_width=True):
    st.session_state.table_2 = st.session_state.table.drop(index=2)
    st.session_state.table_3 = st.session_state.table_2.drop(index=3)
    st.dataframe(st.session_state.table_3, use_container_width=True)



