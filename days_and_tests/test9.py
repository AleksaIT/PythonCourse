#1
#password = input("Enter the password: ")
#if len(password) > 7:
#    print("Great password there!")
#else:
#    print("Your password is weak!")

#2
password = input("Enter the password: ")
if len(password) > 7:
    print("Great password there!")
elif len(password) == 7:
    print("Password is OK, but not too strong!")
else:
    print("Your password is weak!")