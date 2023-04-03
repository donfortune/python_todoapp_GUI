import PySimpleGUI as sg
print("WELCOME TO YOUR TODO LIST")
import time

all_todos = []

# GUI Code
label = sg.Text("Enter your todo")
input_box = sg.InputText(key="todo")
add_button = sg.Button('Add')

window = sg.Window("My Todo App",
                   layout=[[label, input_box, add_button]],
                   font=('Helvetica', 15))

while True:
    time = time.strftime("%d-%m-%Y  %H:%M:%S")
    print(f"Today's date is {time}")
    initialize = input("TYPE ADD, SHOW, EDIT, DELETE  AND EXIT TO BEGIN \n")

    if initialize.startswith("add") or initialize.startswith("new"):
        todos = initialize[4:]
        all_todos.append(todos)
        with open('todos.txt', 'a') as file:
            file.write(todos + '\n')

    elif initialize == "show":
        for index, i in enumerate(all_todos):
            print(f"{index + 1}.{i}")

    elif initialize == "edit":
        number = int(input('enter the number of todo you wish to edit'))
        number = number - 1
        new_todo = input('enter the new todo')
        all_todos[number] = new_todo
        with open('todos.txt', 'w') as file:
            file.write('\n'.join(all_todos))

    elif initialize == "delete":
        deleted = int(input('enter the number you wish to delete'))
        remove_todo = all_todos[deleted - 1]
        all_todos.pop(deleted - 1)
        with open('todos.txt', 'w') as file:
            file.writelines('\n'.join(all_todos))
            message = f"your todo {remove_todo } was removed from the list "
            print(message)

    elif initialize == 'exit':
        break
    else:
        print('YOU ENTERED AN INVALID OPTION')

    # Add todo from GUI
    event, values = window.read()
    if event == "Add":
        todos = values["todo"]
        all_todos.append(todos)
        with open('todos.txt', 'a') as file:
            file.write(todos + '\n')

window.close()
print("GOODBYE")
