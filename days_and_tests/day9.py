#todos = []
while True:
    user_action  = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:]           # samo se upise add i task

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"

            print(row)

    elif 'complete' in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        number = int(user_action[9:])
        idnex = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list."
        print(message)

    elif 'edit' in user_action:
        number = int(user_action[5:])
        number = number - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        print('Here are existing todos: ', todos)

        new_todo = input("Enter a new ToDo: ")
        todos[number] = new_todo +'\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        print('Heres after the edit: ', todos)

    elif 'exit' in user_action:
        break
    else:
        print("Command doesn't exist!")
    #if whatever in user_action:
    #    print("You have entered an unknown command!")
print("Bye!")
