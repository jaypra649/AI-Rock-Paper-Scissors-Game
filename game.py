import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:

    user = input("Enter rock, paper, or scissors: ").lower()

    if user == "exit":
        break

    if user not in choices:
        print("Invalid input")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("Tie!")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    print("Score:", user_score, "-", computer_score)