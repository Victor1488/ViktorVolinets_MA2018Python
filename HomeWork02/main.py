#Guess the number


import simplegui
import random
import math


#Global variable

secret_number = 0
num_range = 100
user_guess = 0
num_guess = 7
restart = 5


#automatical restarting of the game
def game_restart():
    global restart
    
    restart=restart-1
    print "New game in", restart
    if restart == 1:
        restart = 5
        new_game()
        timer.stop()
        

#choice number range
def new_game():
    if num_range == 100:
        global num_guess
        num_guess = 7
        print
        print "A new game has started with a range from 0 to 100"
        print "You have", num_guess, "guesses remaining"
        global comp
        comp = random.randint(0,100)
        #for checking random number
        #print comp
        
    if num_range == 1000:
        num_guess
        num_guess = 10
        print
        print "A new game has started with a range from 0 to 1000"
        print "You have", num_guess, "guesses remaining"
        comp = random.randint(0,1000)
        #for checking random number
        #print comp
                    
#all logic of the game
def input(user_input):
    global user_guess
    global num_guess
    user_guess=int(user_input)
    print user_guess
    
    if user_guess < comp:
        print "Higher!"
        num_guess = num_guess - 1
        print "Remaining guesses:",num_guess
        
    if user_guess > comp:
        print "Lower!"
        num_guess = num_guess - 1
        print "Remaining guesses:",num_guess
        
    if user_guess == comp:
        print "You win!"
        timer.start()
        
    if num_guess == 0:
        print "You lose!!!"
        timer.start()
        
   
def range100():
    global num_range
    num_range = 100
    global num_guess
    num_guess = 7
    new_game()
    
def range1000():
    global num_range
    num_range = 1000
    global num_guess
    num_guess = 10
    new_game()
      
timer = simplegui.create_timer(1000,game_restart)    
    
frame = simplegui.create_frame('Testing', 300, 300)
frame.add_button('Range [0, 100]', range100, 200)
frame.add_button('Range [0, 1000]', range1000, 200)
frame.add_input('Enter guess', input, 50)


new_game()
frame.start()
