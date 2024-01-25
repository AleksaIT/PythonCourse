todos = []

while True:
    user_action  = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a ToDo: ")
            todos.append(todo)
        case 'show' | 'display':
            for index, item in enumerate(todos):
                row = f"{index + 1}.{item}"
                #item = item.title()
                print(row)
        case 'complete':
            number = int(input("Number of the ToDo to complete: "))
            todos.pop(number - 1)
        case 'exit':
            break
        case 'edit':
            number = int(input("Number of the ToDo to edit: "))
            number = number - 1
            new_todo = input("Enter a new ToDo: ")
            todos[number] = new_todo
        case whatever:
            print("You have entered an unknown command!")

print("Bye!")
