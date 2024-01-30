#1
prompt_country = input("Where are you from?: ")
prompt_country = prompt_country.title()

match prompt_country:
    case 'America':
        print("Yo wassup nigga?")
    case 'Serbia':
        print("Desi tebra!")
    case 'Russia':
        print("VODKAAAAAAAAAAAA")


#2
ingredients = ["john smith", "sen plakay", "dora ngacely"]

for item in ingredients:
    print(item.title())