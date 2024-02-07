from modules import functions
import PySimpleGUI as SG
import time

SG.theme("DarkPurple4")
clock = SG.Text('', key="clock")
label = SG.Text("Type in a to-do")
input_box = SG.InputText(tooltip="Enter todo", key="todo")
add_button = SG.Button("Add")
list_box = SG.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = SG.Button("Edit")
complete_button = SG.Button("Complete")
exit_button = SG.Button("Exit")

window = SG.Window('My To-Do App',
                   layout=[[clock],
                       [label], [input_box, add_button], [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 12))

while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%d/%b/%Y  %H:%M:%S"))
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                SG.popup("Please select an item first!", font=("Helvetica", 20))
        case "Complete":
            try:
                 todo_to_complete = values['todos'][0]
                 todos = functions.get_todos()
                 todos.remove(todo_to_complete)
                 functions.write_todos(todos)
                 window['todos'].update(values=todos)
                 window['todo'].update(value='')
            except IndexError:
                SG.popup("Please select an item first!", font=("Helvetica", 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case SG.WINDOW_CLOSED:
            break

window.close()