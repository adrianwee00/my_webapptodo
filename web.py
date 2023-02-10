import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.file_write(todos)
    st.session_state["new_todo"] = ""


st.title("My todo App")
st.subheader("This is my todo app.")
st.write("I am learning to write a new web app.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.file_write(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo:", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")
