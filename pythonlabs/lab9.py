list1 = []
list1.append(1)
list1.append(2)
list1.append(3)

print(list1)

total = 0
for i in range(0, len(list1)):
    total = total + list1[i]

average = total / len(list1)
print("The total is:",total)
print("The average is: {:.1f}".format(average))

