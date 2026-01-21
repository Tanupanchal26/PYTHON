import random

choices = {"s": 1, "w": -1, "g": 0}
names = {1: "Snake", -1: "Water", 0: "Gun"}

while True:
    computer = random.choice([1, -1, 0])   # NEW random choice each round
    user = input("\nEnter s (Snake), w (Water), g (Gun) or q to quit: ").lower()

    if user == "q":
        print("Game over!")
        break

    if user not in choices:
        print("Invalid input! Try again.")
        continue

    you = choices[user]

    print(f"You chose {names[you]}")
    print(f"Computer chose {names[computer]}")

    result = you - computer

    if result == 0:
        print("It's a draw!")
    elif result in (1, -2):
        print("You win!")
    else:
        print("You lose!")
