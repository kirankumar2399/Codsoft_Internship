import random

choices = ["rock", "paper", "scissors"]


def game_logic(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "It's a tie!"
  elif user_choice == "rock":
    if computer_choice == "paper":
      return "You lose! Paper covers rock."
    else:
      return "You win! Rock smashes scissors."
  elif user_choice == "paper":
    if computer_choice == "scissors":
      return "You lose! Scissors cut paper."
    else:
      return "You win! Paper covers rock."
  elif user_choice == "scissors":
    if computer_choice == "rock":
      return "You lose! Rock smashes scissors."
    else:
      return "You win! Scissors cut paper."

# Initialize the user's and computer's scores
user_score = 0
computer_score = 0

# Start the game loop
while True:
  user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

  if user_choice not in choices:
    print("Invalid choice. Please try again.")
    continue

  computer_choice = random.choice(choices)

  print("You chose:", user_choice)
  print("The computer chose:", computer_choice)

  result = game_logic(user_choice, computer_choice)
  print(result)

  if result.startswith("You win"):
    user_score += 1
  elif result.startswith("You lose"):
    computer_score += 1

  print("Your score:", user_score)
  print("Computer's score:", computer_score)

  play_again = input("Do you want to play another round? (yes/no): ").lower()

  if play_again not in ["yes", "no"]:
    print("Invalid input. Try again.")
    continue

  if play_again == "no":
    break

print("Thank you for playing. Goodbye!")

