import PySimpleGUI as sg

label = sg.Text("Enter your todo")
input_box = sg.InputText("")
add_button = sg.Button('ADD')

window = sg.Window("MY TODO APP", layout=[[label, input_box, add_button]])
window.read()  #open the window
window.close()  #close the window