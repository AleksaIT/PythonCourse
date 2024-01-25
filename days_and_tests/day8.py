#todos = []
while True:
    user_action  = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a ToDo: ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}.{item}"
                #item = item.title()
                print(row)

        case 'complete':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            number = int(input("Number of the ToDo to complete: "))
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        case 'exit':
            break

        case 'edit':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            print('Here are existing todos: ', todos)
            number = int(input("Number of the ToDo to edit: "))
            number = number - 1

            new_todo = input("Enter a new ToDo: ")
            todos[number] = new_todo +'\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            print('Heres after the edit: ', todos)

        case whatever:
            print("You have entered an unknown command!")

print("Bye!")
