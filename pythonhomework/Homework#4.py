import random

#randomly picks an integer between 0 and 99
rand_num = (random.randrange(100))
print(rand_num)
rand_tens = rand_num // 10
rand_ones = rand_num % 10


user_num = int(input("Enter a number from 0-99: "))
user_tens = user_num // 10
user_ones = user_num % 10

if rand_tens == user_tens and rand_ones == user_ones:
    print("You won $10000.")
elif rand_tens == user_ones and rand_ones == user_tens:
    print("You won $3000.")
elif rand_tens == user_tens or rand_ones == user_ones or rand_tens == user_ones or rand_ones == user_tens:
    print("You won $1000.")
else:
    print()
