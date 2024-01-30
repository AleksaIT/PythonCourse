todos = []

while True:
    user_action  = input("Type add or show or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a ToDo: ")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        case whatever:
            print("You have entered an unknown command!")

print("Bye!")
