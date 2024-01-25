head = 0
tail = 0
suma = 0

while True:
    coin = input("Throw the coin and enter head or tail here: ")

    match coin:
        case 'head':
            head = head + 1
            suma = suma + 1
            percentaza = (head / suma) * 100
            print("Heads: ", percentaza, '%')

        case 'tail':
            suma = suma + 1
            percentaza = (head / suma) * 100
            print("Heads: ", percentaza, '%')

        #case whatever:
        #    print("You can choose between head and tail only!")

        case 'exit':
            break