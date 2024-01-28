import random

def get_random_number():
    while True:
        try:
            num1 = int(input("Enter the first whole number: "))
            break
        except ValueError:
            print("Please enter a valid whole number.")

    while True:
        try:
            num2 = int(input("Enter the second whole number: "))
            break
        except ValueError:
            print("Please enter a valid whole number.")

    lower = min(num1, num2)
    upper = max(num1, num2)

    return random.randint(lower, upper)

random_number = get_random_number()
print(f"The random number between your chosen numbers is: {random_number}")