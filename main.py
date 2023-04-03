import PySimpleGUI as sg
import time
all_todos = []
label = sg.Text("Enter your todo")
input_box = sg.InputText(key="todo")
add_button = sg.Button('Add')
edit_button = sg.Button('Edit')

window = sg.Window("My Todo App",
                   layout=[[label, input_box, add_button],
                           [edit_button]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read()  #open the window
    if event == "Add":
        todos = values["todo"]
        all_todos.append(todos)
        with open('todos.txt', 'a') as file:
            file.write(todos + '\n')
    if event == sg.WIN_CLOSED:
        break
    print(event)
    print(values)
window.close()  #close the window

print("WELCOME TO YOUR TODO LIST")

#new_todos = [item.strip('\n') for item in todos] -- list comprehension


while True:
    time = time.strftime("%d-%m-%Y  %H:%M:%S")
    print(f"Today's date is {time}")
    initialize = input("TYPE ADD, SHOW, EDIT, DELETE  AND EXIT TO BEGIN \n")

    if initialize.startswith("add") or initialize.startswith("new"):
        todos = initialize[4:]

        all_todos.append(todos)
        with open('todos.txt', 'a') as file:
            file.write(todos + '\n')  # Write tasks to file in a new lines

    elif initialize == "show":
        for index, i in enumerate(all_todos):

            print(f"{index + 1}.{i}")

    elif initialize == "edit":
        number = int(input('enter the number of todo you wish to edit'))
        number = number - 1
        new_todo = input('enter the new todo')

        all_todos[number] = new_todo
        with open('todos.txt', 'w') as file:
            file.write('\n'.join(all_todos))  # Write tasks to file in a new list






        '''edited_todos = input("enter the todo you wish to edit \n")
        for i in range(len(all_todos)):
            if all_todos[i] == edited_todos:
                new_todo = input("enter new todo \n")
                all_todos[i] = new_todo
                break
        else:
                print(f"{edited_todos} is not in the list")'''


    elif initialize == "delete":
        deleted = int(input('enter the number you wish to delete'))
        remove_todo = all_todos[deleted - 1]

        all_todos.pop(deleted - 1)

        with open('todos.txt', 'w') as file:
            file.writelines('\n'.join(all_todos))  # Write tasks to file in a new list
            message = f"your todo {remove_todo } was removed from the list "
            print(message)


        #with open('todos.txt', 'w') as file:
           # file.writelines('\n'.join(all_todos))  # Write tasks to file in a new list


        '''finished_todo = input('enter the todo you wish to delete \n')
        if finished_todo in all_todos:
            all_todos.remove(finished_todo)
            print(f"{finished_todo} has been removed from the list.")
        else:
            print(f"{finished_todo} is not in the list.")'''
    elif initialize == 'exit':
        break
    else:
        print('YOU ENTERED AN INVALID OPTION')

print("GOODBYE")















