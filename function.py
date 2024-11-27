## Intro of the homepage
def show_intro():
    st.title("THIS IS TO DO LIST APP")
    st.subheader("This to do list is created based RWID python crash course")

## Name input function
def name_input():
    name = st.text_input("Please enter your name here", "")
    if name != "":
        st.subheader(f"Hi {name} please use this To Do App for your daily productivity")
    else:
        None

## Table Creation function using Pandas
def create_table():
    table = pd.DataFrame(columns=['To Do', 'Day'])
    activity = st.text_input("Put your to do list")
    day = st.text_input("Put your day")
    table.loc[len(table.index)] = [activity, day]
    st.dataframe(table)

## Table read function using pandas
#def read_table():


## Table Insert function using Pandas
#def update_table():


## Main function
def main():
    choice = st.sidebar.selectbox(
            "To Do List Button",
            ("Create", "Read") # Must Add Update and Delete in the future
        )
    show_intro()
    name_input()
    if choice == "Create":
        create_table()



