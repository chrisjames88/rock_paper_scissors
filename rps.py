# Rock, Paper, Scissors
# Patrick Mogianesi
# Definitly room for imporvement, it's kinda messy.
# But it's totally functional, which is nice.

import random

# The actions the player and computer can choose from
game_actions = ["rock", "paper", "scissors"]

# Initialize scores
player_wins = 0
computer_wins = 0

def print_scores(player_wins, computer_wins):
    """Prints the current scores."""
    print(f"The player has {player_wins} wins, and the computer has {computer_wins} wins")

def play_again():
    """Asks the player if they want to play again."""
    while True:
        replay = input("Do you want to play again? (y/n): ").strip().lower()
        if replay == "y":
            return True
        elif replay == "n":
            print("Thanks for playing! :)")
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def reset_game():
    """Resets the game scores and asks if the player wants to start over."""
    while True:
        reset_choice = input("Would you like to reset the game? (y/n): ").strip().lower()
        if reset_choice == "y":
            global player_wins, computer_wins
            player_wins = 0
            computer_wins = 0
            print("Game reset. Let's start over!")
            return True
        elif reset_choice == "n":
            print("Thank you for playing! :)")
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def game():
    """Main game function."""
    global player_wins, computer_wins

    while player_wins < 5 and computer_wins < 5:
        print("Choose either rock, paper, or scissors:")
        player_choice = input("> ").strip().lower()
        
        if player_choice not in game_actions:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(game_actions)
        print(f"The computer chose {computer_choice}.")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            player_wins += 1
        else:
            print("You lost this round!")
            computer_wins += 1

        print_scores(player_wins, computer_wins)

    if player_wins == 5:
        print("Congratulations! You won the game!")
    else:
        print("The computer won the game!")

    if play_again():
        game()
    elif reset_game():
        game()

if __name__ == "__main__":
    game()
