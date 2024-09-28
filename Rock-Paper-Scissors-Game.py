import random

def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You win!"
    else:
        return "Computer wins!"

user_choice = input("Choose Rock, Paper, or Scissors: ")
computer_choice = get_computer_choice()
print(f"Computer chose: {computer_choice}")
result = determine_winner(user_choice, computer_choice)
print(result)
