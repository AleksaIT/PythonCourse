#todos = []
while True:
    user_action  = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a ToDo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show' | 'display':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            #new_todos = []
            #for item in todos:
            #    new_item = item.strip('\n')   #strip uklanja nesto iz elementa
            #    new_todos.append(new_item)
            #new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
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
