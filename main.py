from modules.functions import get_todos, write_todos
import time
#import functions  -> ali moras pozivati funkcije sa functions.get_todos()...

now = time.strftime("%d/%b/%Y  %H:%M:%S")
print(now)

while True:
    user_action  = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]           # samo se upise 'add' sve nakon toga je string za unos

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)     #drugi parametar je default vec sa filepathom

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"

            print(row)

    elif user_action.startswith("complete"):
        try:
            todos = get_todos()
            number = int(user_action[9:])
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is not item with that number.")
            continue

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()
            print('Here are existing todos: ', todos)

            new_todo = input("Enter a new ToDo: ")
            todos[number] = new_todo +'\n'

            write_todos(todos)

            print('Heres after the edit: ', todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command doesn't exist!")
    #if whatever in user_action:
    #    print("You have entered an unknown command!")
print("Bye!")
