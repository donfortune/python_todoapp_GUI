import streamlit as st
import functions
todos = functions.get_todos()
def add_todo():
    todo_new = st.session_state['new_todo'] + "\n"
    todos.append(todo_new)
    functions.write_todos(todos)



st.title('My Todo App')
st.subheader('Get Task Done Quickly!')
st.text_input(label='', placeholder='Enter a todo..',
              on_change=add_todo, key='new_todo')
for todo in todos:
    st.checkbox(todo)



