'''
This is the final project for day 3.

We are building a text based adventure game which features some choices for the user.

Depending on what choices the user provides, we are going to develop the game further.
'''

'''
The display_message() function simply prints the welcome message to the player at the start of the game
'''


def display_message():
    diagram = '''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/______/_
    *******************************************************************************
    '''

    message = ''' Welcome to Treasure Island! \n Your mission is to find the treasure. Let\'s begin!
    '''

    print(diagram, message, sep='\n')


'''
The play() function is the main working function of this game
After displaying the welcome message to the user, the play() function is called to start the game
A series of questions are asked to the player and the answers are stored in different variables

direction = whether the player wants to go right or left
swim_or_wait = whether the player wants to swim across the lake or wait for a boat
door_color = the color of the door the player chooses

Depending on the answers provided by the player for these questions, we have to develop the adventure.
'''


def play():
    direction = input(
        "You are at a cross road. Where do you want to go? Type \"left\" or \"right\" ").lower()

    if direction == 'right':
        print(" There is a huge troll with a club who just smashed you like a fly. Bas! Khatam! Tata! Bye bye ! Goodbye! Gaya!")
        return
    swim_or_wait = input(
        " You come to a lake.  There is an island at the middle of the lake. Type \"wait\" to wait for a boat or \"swim\" to swim across the lake. ").lower()

    if swim_or_wait == 'swim':
        print(" You have been eaten by a giant crocodile. Bas! Khatam! Tata! Bye bye ! Goodbye! Gaya!")
        return

    door_color = input(
        " You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? ").lower()

    if door_color == 'red':
        print(
            " You entered a room full of fire. Bas! Khatam! Tata! Bye bye ! Goodbye! Gaya!")
        return
    elif door_color == 'blue':
        print(" You entered a ice cold room. You froze to death. Bas! Khatam! Tata! Bye bye ! Goodbye! Gaya!")
        return
    else:
        print(" Congratulations! You have found the treasure!")
        return


if __name__ == "__main__":
    display_message()
    play()
