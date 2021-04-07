import random

choice1 = input("Enter choice 1: ")
choice2 = input("Enter choice 2: ")

choice_chooser = random.randint(1,2)

if choice_chooser == 1:
    print("Random Selection Engine chooses:", choice1)
else:
    print("Random Selection Engine chooses:", choice2)

