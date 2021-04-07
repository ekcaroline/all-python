import random

magic_num = random.randrange(11)

user1 = int(input("User 1, enter a number between 1 and 10: "))
user2 = int(input("User 2, enter a number between 1 and 10: "))

print("Magic Number:", magic_num)

difference1 = abs(user1 - magic_num)
difference2 = abs(user2 - magic_num)

if difference1 < difference2:
    print("User 1 guessed", user1, "which is closer to", magic_num, "than", user2)
elif difference1 > difference2:
    print("User 2 guessed", user2, "which is closer to", magic_num, "than", user1)
elif difference1 == difference2:
    print("There are no winners.")
else:
    print()




