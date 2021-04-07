import sys
sys.setrecursionlimit(8000)

def give_sum(n):
    if n <= 1:                          #if n is equal to 1, print 1
        return n
    else:                               #else, add the integer with next integer
       return n + give_sum(n-1)         #for example, if n=3, then goes to else 3 + 2. Stores 5, then runs again with 3-1 = 2. Goes to else and .


num = 123
print("The sum from 1 to {} is {}.".format(num, give_sum(num)))
