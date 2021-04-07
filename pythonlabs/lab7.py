def min2(x, y = 0):
    return min(x, y)

x = int(input("Enter an int: "))
y = int(input("Enter an int: "))
print("The minimum of", x, "and", 0, "is", min2(x))
print("The minimum of", x, "and", y, "is", min2(x, y))

    
