# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 10
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-120/240, -60/180]
paddle1_pos = [4,20,4,80]
paddle1_vel = [0,0]
paddle2_pos = [596,20,596,80]
ball_vel = [-120/240, -60/180]
score1 = 0
score2 = 0
def spawn_ball():
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel[0] = - ball_vel[1]
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos  # these are numbers
    global score1, score2  # these are ints
    #spawn_ball(LEFT)

    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, direction 
    global LEFT,RIGHT
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_text(str(score1), [250,112], 48, "White")  
    canvas.draw_text(str(score2), [325,112], 48, "White") 
    # update ball
    ball_pos[0] += ball_vel[0]*3
    ball_pos[1] += ball_vel[1]*3
    
   
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Red", "White")
    # update paddle's vertical position, keep paddle on the screen
    
    
    #if ball_pos[0]  <= paddle1_pos[3]:
        #ball_vel[0] = - ball_vel[0]
        
    
    if  ball_pos[0] <= 10:
        ball_vel[0] = - ball_vel[0]
        score1 = score1+1
        spawn_ball()
        
    elif ball_pos[0] >= 572:
        ball_vel[0] = - ball_vel[0]
        score2 = score2+1
        spawn_ball()
        
    elif ball_pos[1]>= 380:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1]<= 20:
        ball_vel[1] = - ball_vel[1] 
    
    # draw paddles       
    canvas.draw_polygon([[paddle1_pos[0],paddle1_pos[1]],[paddle1_pos[2],paddle1_pos[3]]], 10, 'White')
    canvas.draw_polygon([[paddle2_pos[0],paddle2_pos[1]],[paddle2_pos[2],paddle2_pos[3]]], 10, 'White')
    # determine whether paddle and ball collide  

    #ball_vel = ball_pos
    
    # draw score
        
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos
    
    if key == 83:
        paddle1_pos[1] = paddle1_pos[1] + 20
        paddle1_pos[3] = paddle1_pos[3] + 20
    if key == 87:
        paddle1_pos[3] = paddle1_pos[3] - 20
        paddle1_pos[1] = paddle1_pos[1] - 20
    if key == 40:
        paddle2_pos[1] = paddle2_pos[1] + 20
        paddle2_pos[3] = paddle2_pos[3] + 20
    if key == 38:
        paddle2_pos[1] = paddle2_pos[1] - 20
        paddle2_pos[3] = paddle2_pos[3] - 20

        
def keyup(key):
    global paddle1_vel, paddle2_vel



# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
