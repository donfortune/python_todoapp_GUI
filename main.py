import PySimpleGUI as sg
import functions

all_todos = []
label = sg.Text("Enter your todo")
input_box = sg.InputText(key="todo")
add_button = sg.Button('Add')
edit_button = sg.Button('Edit')
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[20, 5])

window = sg.Window("My Todo App",
                   layout=[[label, input_box, add_button],
                           [list_box],
                           [edit_button]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read()  #open the window
    if event == "Add":
        todos = functions.get_todos()
        new_todos = values["todo"]
        todos.append(new_todos)
        functions.write_todos(todos)
        window['todos'].update(values=todos)
    elif event == "Edit":
        todo_to_edit = values["todos"][0]
        new_todo = values['todo']

        todos = functions.get_todos()
        index = todos.index(todo_to_edit)
        todos[index] = new_todo
        functions.write_todos(todos)
        window['todos'].update(values=todos)
    elif event == "todos":
        window['todo'].update(value=values['todos'])
    elif event == sg.WIN_CLOSED:
        break



    print(event)
    print(values)
window.close()  #close the window
















