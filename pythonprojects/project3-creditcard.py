def is_valid_CC(creditnum): 
    if not creditnum.isdecimal():
        return False
    if len(creditnum) < 12 or len(creditnum) > 17:
        return False
    if creditnum[0] == 4 or creditnum[0] == 5 or creditnum[0] == 37:
        return False
    
    #luhns algorithm
    
    totalone = 0
    for digit in creditnum[::-2]:
        totalone += int(digit)
        
    totaltwo = 0
    for digit in creditnum[-2::-2]:
        doubled = int(digit) * 2
        if doubled < 10:
            totaltwo += doubled
        else:
            tens = doubled // 10
            ones = doubled % 10
            single = tens + ones
            totaltwo += single
    return (totalone + totaltwo) % 10 == 0

def is_valid_RN(routenum):
    if not routenum.isdecimal():
        return False
    if len(routenum) != 9:
        return False

    totalone = 0
    for digit in routenum[::-3]:
        totalone += int(digit)

    totaltwo = 0
    for digit in routenum[-2::-3]:
        totaltwo += int(digit)
    totaltwo *=  7

    totalthree = 0
    for digit in routenum[-3::-3]:
        totalthree += int(digit)
    totalthree *= 3

    return (totalone + totaltwo + totalthree) % 10 == 0

print("Credit Card Entry")
print("--------------------------------------------------------------")
print("------------------")
card = input("Enter credit card number: ")

while card != 'q':
    if is_valid_CC(card) == True:
        print(card, "is valid.")
    else:
        print(card, "is invalid.")
    card = input("Enter credit card number: ")

print()

print("Routing Number Entry")
print("--------------------------------------------------------------")
print("------------------")
route = input("Enter routing number: ")
while route != 'q':
    if is_valid_RN(route) == True:
        print(route, "is valid.")
    else:
        print(route, "is invalid.")
    route = input("Enter routing number: ")




