import streamlit as st
import functions

todos = functions.get_todos()
write_todo = functions.write_todos()

st.title('My Todo App')
for todo in write_todo:
    title = todo['title']
    description = todo['description']
    st.text_input(title, value=description)
    todos.append(todo)

st.subheader('Get Task Done Quickly!')

for todo in todos:
    st.checkbox(todo)



