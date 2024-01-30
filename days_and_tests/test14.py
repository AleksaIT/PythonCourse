from ../modules import functions

def state(temp):
    if temp <= 0:
        state = 'Solid'
    elif 0 < temp < 100:
        state = 'Liquid'
    elif temp >= 100:
        state = 'Gas'
    return state

temp = int(input("Eter water temperature: "))
print(state(temp))