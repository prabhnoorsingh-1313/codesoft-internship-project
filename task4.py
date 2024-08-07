
import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    computer_score = 0
    user_score = 0

    while True:
        user_choice = input("Enter your choice (rock/paper/scissors) or 'q' to quit: ").lower()
        if user_choice == 'q':
            break

        if user_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"\nComputer chose: {computer_choice}")

        if user_choice == computer_choice:
            print(f"Both players selected {user_choice}. It's a tie!")
        elif user_choice == 'rock':
            if computer_choice == 'scissors':
                print("Rock smashes scissors! You win!")
                user_score += 1
            else:
                print("Paper covers rock! You lose.")
                computer_score += 1
        elif user_choice == 'paper':
            if computer_choice == 'rock':
                print("Paper covers rock! You win!")
                user_score += 1
            else:
                print("Scissors cuts paper! You lose.")
                computer_score += 1
        elif user_choice == 'scissors':
            if computer_choice == 'paper':
                print("Scissors cuts paper! You win!")
                user_score += 1
            else:
                print("Rock smashes scissors! You lose.")
                computer_score += 1

        print(f"\nScore - You: {user_score}, Computer: {computer_score}")

if __name__ == "__main__":
    play_game()
