#Simple Dice Rolling Game

import random

roll_count = 0

while True:
    choice = input("Roll the dice (y/n): ").upper()
    if choice == "Y":
        while True:
            try:
                quantity = int(input("How many dice you want to roll: "))
                if quantity <= 0:
                    print('Please enter a number greater than 0')
                    continue
                break
            except ValueError:
                print("Invalid! Please try again!!")

        for i in range(quantity):
            dice_roll = random.randint(1,6)
            print(f"Roll {i + 1}: {dice_roll}")
            roll_count += 1

    elif choice == "N":
        print("Game shut down! Thank you for playing<3")
        print(f'Total roll this time: {roll_count}')
        break
    else:
        print("Invalid choice! Please try again")


