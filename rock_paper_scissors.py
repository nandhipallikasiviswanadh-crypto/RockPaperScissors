import random

print("=" * 45)
print("     ROCK PAPER SCISSORS GAME")
print("=" * 45)
print("Instructions:")
print("1. Enter rock, paper, or scissors.")
print("2. Play as many rounds as you want.")
print("3. Type 'no' when asked to stop.\n")

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    if user_choice not in choices:
        print("❌ Invalid choice! Please enter rock, paper, or scissors.\n")
        continue

    computer_choice = random.choice(choices)

    print(f"\nYou chose      : {user_choice}")
    print(f"Computer chose : {computer_choice}")

    if user_choice == computer_choice:
        print("🤝 It's a Tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("🎉 You Win!")
        user_score += 1
    else:
        print("💻 Computer Wins!")
        computer_score += 1

    print("\nCurrent Score")
    print("------------------------")
    print("You      :", user_score)
    print("Computer :", computer_score)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("\n========== GAME OVER ==========")
print("Final Score")
print("------------------------")
print("You      :", user_score)
print("Computer :", computer_score)

if user_score > computer_score:
    print("\n🏆 Congratulations! You won the game!")
elif computer_score > user_score:
    print("\n💻 Computer won the game!")
else:
    print("\n🤝 The game ended in a tie!")

print("\nThank you for playing!")