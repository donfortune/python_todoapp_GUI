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
for index, todo in enumerate(todos):
    check_box = st.checkbox(todo, key=todo)
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()






