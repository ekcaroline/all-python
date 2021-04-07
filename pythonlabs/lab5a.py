num = int(input("Enter a positive integer: "))
total = 0

for number in range(1, num + 1):
    print(number, end=" ")
    total = total + number
print("\nThe sum is {}.".format(total))



