'''
This is the final project for Day 4 of 100 Days of Python

In this project, we are going to create the classic Rock-Paper-Scissor game using Python

We are going to learn about randomising and if else conditions through this project
'''

import random  # Since we have to randomise computer's choice, therefore we have to use the random module

'''
The play() function initialises the variables required for calculating the scores for both the player and the computer
We are giving 10 chances to the player to play either rock, paper or scissor and depending on the computer's choice we are calculating the score

The variables are as follows:-

restart - Variable for the user to choose whether or not to play again
comp_choices - List of values which the computer might play
num_chances - Number of chances for each round
player_score - Total score of the player
computer_score - Total score of the computer
player_choice - Player's choice, either rock, paper or scissor
computer - Random choice for computer from the list of choices comp_choices
'''


def play():
    restart = 'yes'
    comp_choices = ['rock', 'paper', 'scissor']

    while restart == 'yes':
        num_chances = 10  # Total number of chances a particular player gets
        player_score = 0
        computer_score = 0
        while num_chances > 0:
            player_choice = input(
                "Type \'rock\', \'paper\' or \'scissor\': ").lower()

            computer = random.choice(comp_choices)

            if computer == 'rock':
                if player_choice == 'scissor':
                    computer_score += 1
                elif player_choice == 'paper':
                    player_score += 1
            elif computer == 'paper':
                if player_choice == 'rock':
                    computer_score += 1
                elif player_choice == 'scissor':
                    player_score += 1
            else:
                if player_choice == 'paper':
                    computer_score += 1
                elif player_choice == 'rock':
                    player_score += 1
            print("Your choice: " + player_choice +
                  "                      Computer Choice: " + computer)
            num_chances -= 1

        if player_score > computer_score:
            print(
                f"Your score is {player_score} and computer\'s score {computer_score}. You have won!")
        elif player_score == computer_score:
            print(
                f"Your score is {player_score} and computer\'s score {computer_score}. It is a draw!")
        else:
            print(
                f"Your score is {player_score} and computer\'s score {computer_score}. You have lost this round :( Better luck next time!")

        restart = input(
            "Do you want to play again? Type \'yes\' to continue or \'no\' to exit: ").lower()


if __name__ == '__main__':
    play()
