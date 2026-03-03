import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    todo_text = st.session_state["new_todo"].strip()
    if not todo_text:
        return
    todos.append(todo_text + "\n")
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""  # очистити інпут

st.title('My Todo App')
st.subheader("This is to increase your productivity")
st.text("This is my first app")

indexes_to_remove = []

for i, todo in enumerate(todos):
    todo_clean = todo.strip()
    checked = st.checkbox(todo_clean, key=f"todo_{i}")
    if checked:
        indexes_to_remove.append(i)

if indexes_to_remove:
    for i in sorted(indexes_to_remove, reverse=True):
        todos.pop(i)
    functions.write_todos(todos)
    st.rerun()

st.text_input(label="Enter your todo: ",
              placeholder="Add new todo...",
              on_change=add_todo,
              key="new_todo")