"""    Zadatak 1
def age(year_of_birth, current_year):
    ager = current_year - year_of_birth
    return ager

birth = int(input("What is your year of birth?: "))
your_age = age(birth, 2024)

if your_age < 120:
    print(your_age)
else:
    print("Bro, you're not a fossil...")
"""

#Zadatak 2
def userno(names):
    names = names.split(",")
    return len(names)

names = input("Enter the names separated by commas (no spaces): ")
num = userno(names)
print(num)