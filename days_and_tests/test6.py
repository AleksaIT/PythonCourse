#1
#file = open(f"../files/{'essay.txt'}", 'r')
#essay = file.read()
#file.close()
#print(essay.title())

#2
#file = open(f"../files/{'essay.txt'}", 'r')
#essay = file.read()
#number = len(essay)
#print(number)

#3
#member = input("Add a new member: ")
#file = open(f"../files/{'members.txt'}", 'r')
#existing_members = file.readlines()   #pravimo listu sa memberima
#file.close()
#existing_members.append(member + "\n")     #appendujemo novog
#file = open(f"../files/{'members.txt'}", 'w')
#existing_members = file.writelines(existing_members)    #upisujemo novu listu sa appendovanim
#file.close()

#4
#filenames = ["doc.txt", "report.txt", "presentation.txt"]
#for filename in filenames:
#    file = open(f"../files/{filename}", 'w')
#    file.write("Hello")
#    file.close()

#5
filenames = ['a.txt', 'b.txt', 'c.txt']
for filename in filenames:
    file = open(f"../files/{filename}", 'r')
    iam = file.readline()
    print(iam)