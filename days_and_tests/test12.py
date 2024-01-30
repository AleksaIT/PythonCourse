#1. Create a function that converts liters to cubic meters knowing that 1000 liters make 1 cubic meter.
#def convert(liters):
#   cublit = float(liters / 1000)
#    return cublit
#liter = float(input("How many liters you wanna convert?: "))
#print(convert(liter))

#2. Create a script that asks the user to enter a password. Then create a function that checks the strength of the user password. The function should return Strong Password if all of the following conditions are true:
#Eight or more characters
#At least one uppercase letter.
#At least one digit.

user_password = input("Enter new password: ")
def strength(password):

    result = {}

    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    uppercase = False

    for i in password:
        if i.isdigit():
            digit = True
        if i.isupper():
            uppercase = True

    result["digits"] = digit
    result["upper-case"] = uppercase

    if all(result.values()):
        return "Strong Password"
    else:
        return "Weak Password"

print(strength(user_password))