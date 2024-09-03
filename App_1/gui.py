#desktop graphical user interface
import functions
import PySimpleGUI as sg#third party libraries or modules
import time


sg.theme("DarkPurple4")

clock=sg.Text("",key="clock")
label=sg.Text("Type in a todo:")
input_box=sg.InputText(tooltip="Enter todo:", key="Todo")
add_button=sg.Button("Add")


list_box=sg.Listbox(values=functions.open_todo(), key="todos", enable_events=True,
                    size=[45,10])
edit_button=sg.Button("Edit")

cut_button=sg.Button("Cut")

exit_button=sg.Button("Exit")

window=sg.Window('My Todo App',
                 layout=[[clock],[label], [input_box,add_button],[list_box,edit_button],[cut_button,exit_button]],
                 font=('Helvetica',20))#widgets

while True:
    event,values=window.read(timeout=200)#display window on screen using read method.Creates a tuple
    window["clock"].update(value=time.strftime("%b %d,%Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "Add":
            todos=functions.open_todo()
            new_todo=values["Todo"]+"\n"
            todos.append(new_todo)
            functions.write_todo(todos)
            window["todos"].update(values=todos)
            window["Todo"].update(value="")

        case "Edit":
            try:
                todo_to_edit=values["todos"][0]
                new_todo=values["Todo"]+"\n"
                todos=functions.open_todo()
                index=todos.index(todo_to_edit)
                todos[index]=new_todo
                functions.write_todo(todos)
                window["todos"].update(values=todos)#values for list
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica",20))


        case "Cut":
            try:
                todo_to_cut=values["todos"][0]
                todos=functions.open_todo()
                todos.remove(todo_to_cut)
                functions.write_todo(todos)
                window["todos"].update(values=todos)
                window["Todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))



        case "todos":
            window["Todo"].update(value=values["todos"][0])#value for a string

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

window.close()
