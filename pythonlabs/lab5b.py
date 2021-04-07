user_input = int(input("Enter a positive integer (<= 0 to quit): "))

total = 0

while user_input > 0:
    if (user_input % 2) == 0:
        total = total + user_input
        user_input = int(input("Enter a positive integer (<= 0 to quit): "))
    else:
        user_input = int(input("Enter a positive integer (<= 0 to quit): "))
        
print("The sum of the positive even integers entered is {}".format(total))
