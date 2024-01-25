#def get_max():
#    minmax = []
#    grades = [9.6, 9.2, 9.7]
#    maxxer = max(grades)
#    minner = min(grades)
#    minmax = [minner, maxxer]
#    return minmax

# = get_max()
#print("Min: ", prmax[0])
#print("Max: ", prmax[1])


def get_max():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    minimum = min(grades)
    message = f"Max: {maximum}, Min: {minimum}"
    return message

print(get_max())