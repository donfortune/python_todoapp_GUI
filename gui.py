import PySimpleGUI as sg
import functions
import time
import os

if not os.path.exists('todos.txt'):   #condition
    with open('todos.txt', 'w') as file:
        pass

all_todos = []
sg.theme('Blue')
label = sg.Text("Enter your todo")
input_box = sg.InputText(key="todo")
add_button = sg.Button('Add', tooltip='Add Todo')
edit_button = sg.Button('Edit', tooltip='Edit Todo')
exit_button = sg.Button('Exit', tooltip='Exit Todo')
completed_button = sg.Button('Completed', tooltip='Completed Todo')
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[50, 5])
clock_label = sg.Text('', key="clock")

window = sg.Window("My Todo App",
                   layout=[[clock_label],
                       [label, input_box, add_button],
                           [list_box, exit_button],
                           [edit_button, completed_button]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read(timeout=200)  #open the window
    window["clock"].update(value=time.strftime("%Y %H:%M:%S"))
    if event == "Add":
        todos = functions.get_todos()
        new_todos = values["todo"]
        todos.append(new_todos)
        functions.write_todos(todos)
        window['todos'].update(values=todos)
        window['todo'].update(value=todos)
    elif event == "Edit":
        try:
            todo_to_edit = values["todos"][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        except IndexError:
            sg.popup("Select an item from the list")
    elif event == "todos":
        window['todo'].update(value=values['todos'])
    elif event == "Exit":
        exit()
    elif event == "Completed":
        try:
            completed_todo = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(completed_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value=todos)
        except IndexError:
            sg.popup("Select an item from the list")

    elif event == sg.WIN_CLOSED:
        break



    print(event)
    print(values)
window.close()  #close the window
















