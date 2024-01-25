try:
    totval = float(input("Enter a total value: "))
    val = float(input("Enter a value: "))

    perc = float(val / totval) * 100
    print(perc, "%")

except ValueError:
    print("You have to enter a number.")
except ZeroDivisionError:
    print("Your total value cannot be zero")