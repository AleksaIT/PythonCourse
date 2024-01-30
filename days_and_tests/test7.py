#1
#names = ["john smith", "jay santi", "eva kuki"]
#names = [name.title() for name in names]
#print(names)

#2
#usernames = ["john 1990", "alberta1970", "magnola2000"]
#userlen = []
#for name in usernames:
#    usern = len(name)
#    userlen.append(usern)
#print(userlen)

#3
#user_entries = ['10', '19.1', '20']
#float_entry = []
#for entry in user_entries:
#    entry = float(entry)
#    float_entry.append(entry)
#print(float_entry)

#4
user_entries = ['10', '19.1', '20']
user_numbers = [float(item) for item in user_entries]
print(sum(user_numbers))