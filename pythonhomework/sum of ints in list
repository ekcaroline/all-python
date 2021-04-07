def make_list():
    list1 = []
    while True:
        num = int(input("Enter a nonnegative number or -999 to quit: "))
        if num == -999:
            break
        list1.append(num)
    return list1

def sum_list(numbers):
    
    total = 0
    
    if numbers == 0:
        return 0
    else:
        for i in range(len(numbers)):
            total = total + numbers[i]
        return total
    
totalamount = make_list()
print("List:",totalamount)
print("Sum of list:", sum_list(totalamount))


