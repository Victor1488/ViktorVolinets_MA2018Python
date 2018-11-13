import random

elements = 'rock', 'Spock', 'paper', 'lizard', 'scissors'


def name_to_number(name):

    if name == "rock":
        name = 0
    elif name == "Spock":
        name = 1
    elif name == "paper":
        name = 2
    elif name == "lizard":
        name = 3
    else:
        name = 4
    return (name)


def number_to_name(number): 
    #I do not understand why this function is here.
    #I did without her
    
    if number == 0:
        number = "rock"
    elif number == 1:
        number = "Spock"
    elif number == 2:
        number = "paper"
    elif number == 3:
        number = "lizard"
    else:
        number = "scissors"


def rpsls(player_choice):
    
    comp_choice = random.choice(elements)

    player = name_to_number(player_choice)

    comp = name_to_number(comp_choice)

    print "Player chooses", player_choice
    print "Computer chooses", comp_choice

    win = (player - comp) % 5

    if win == 1:
        print "Player wins!"
    elif win == 2:
        print "Player wins!"
    elif win == 3:
        print "Computer wins!"
    elif win == 4:
        print "Computer wins!"
    else:
        print "Draw"

    print


rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

