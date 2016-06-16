# Rock, Paper, Scissors
# June 16th 2016
# Patrick Mogianesi
# Definitly room for imporvement, it's kinda messy.
# But it's totally functional, which is nice.

import random

#the actions the player and computer have access to
game_actions = ["rock", "paper", "scissors"]

#stores the scores of the player and computer
#if the player wins, 1 score is added, same for comp if comp wins
player_wins = 0
computer_wins = 0

#called function that prints the scores stored in the variables
def score(player_wins, computer_wins):
	print "The player has %r wins, and the computer has %r wins" % (player_wins, computer_wins)

#function that is called which allows the game to be replayed
def play_again(player_wins, computer_wins):
	print "Do you want to play again"
	print "y for yes, n for no"
	replay = raw_input("> ")
	if replay == "y":
		game(player_wins, computer_wins)
	elif replay == "n":
		print "Ok, thanks for playing. :)"
	else:
		print "That input doesn't work, please input either y or n."
		play_again(player_wins, computer_wins)
		
#Main function which holds the game mechanics		
def game(player_wins, computer_wins):
	
	#this is the code that randomly chooses the action for the computer choice
	computer_choice = random.choice(game_actions)
	print "Choose either rock, paper, or scissors."
	
	#the player choice, input by user
	player_choice = raw_input("> ")
	
	#Code here is based on what the computer & users are equal to
	
	#player picked rock situations
	if player_choice == "rock" and computer_choice == "rock":
		print "It's a tie, you both threw rock."
		score(player_wins, computer_wins)
		play_again(player_wins, computer_wins)
		
	elif player_choice == "rock" and computer_choice == "scissors":
		print "You win, you chose rock, and computer picked scissors."
		player_wins = player_wins + 1
		score(player_wins, computer_wins)
		play_again(player_wins, computer_wins)
		
	elif player_choice == "rock" and computer_choice == "paper":
		print "You lost, computer picked paper and you picked rock."
		computer_wins = computer_wins + 1
		score(player_wins, computer_wins)
		play_again(player_wins, computer_wins)
	
	#player picked paper situations
	elif player_choice == "paper" and computer_choice == "rock":
	
		print "You win, computer picked rock and you picked paper."
		player_wins = player_wins + 1
		score(player_wins, computer_wins)
		play_again(player_wins, computer_wins)
		
	elif player_choice == "paper" and computer_choice == "paper":
		print "It's a tie, you both picked paper."
		score(player_wins, computer_wins)
		play_again(player_wins, computer_wins)
		
	elif player_choice == "paper" and computer_choice == "scissors":
		print "You lost, you picked paper and computer picked scissors."
		computer_wins = computer_wins + 1
		score(player_wins, computer_wins)
		play_again(player_wins, computer_wins)
	
	#player picked scissors situations
	elif player_choice == "scissors" and computer_choice == "rock":
		print "You lost, you chose scissors and computer chose rock."
		score(player_wins, computer_wins)
		computer_wins = computer_wins + 1
		play_again(player_wins, computer_wins)
		
	elif player_choice == "scissors" and computer_choice == "scissors":
		print "It's a tie, you both picked scissors."
		score(player_wins, computer_wins)
		play_again(player_wins, computer_wins)
		
	elif player_choice == "scissors" and computer_choice == "paper":
		print "You win, you picked scissors and the computer picked paper."
		player_wins = player_wins + 1
		score(player_wins, computer_wins)
		play_again(player_wins, computer_wins)
	
	#reset back	
	else:
		print "That's not a valid command"
		game(player_wins, computer_wins)
		
game(player_wins, computer_wins)
