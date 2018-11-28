# Stop: The Game

import simplegui

# Global var

A = 0
B = 0
C = 0
D = 0

game = 0
shot = 0

stoper = 0


# Handler for mouse click

def start():
    global message
    timer.start()
    global D, C, B, A, stoper
    stoper = 0
    f()


def f():
    global D, C, B, A, game
    D = D + 1
    if D == 10:
        D = 0
        C = C + 1
        if C == 10:
            C = 0
            B = B + 1
            if B == 6:
                B = 0
                A = A + 1


# timer on canvas

def convert():
    result = str(A) + ':' + str(B) + str(C) + ':' + str(D)
    return result


def stop():
    timer.stop()
    global D, shot, game, stoper
    if D > 0 and stoper == 0:
        shot = shot + 1
        stoper = 1
    if D == 0 and C > 0 and stoper == 0:
        game = game + 1
        shot = shot + 1
        stoper = 1


def reset():
    timer.stop()
    global A, B, C, D, shot, game
    D = 0
    C = 0
    B = 0
    A = 0
    shot = 0
    game = 0


def score():
    global shot, game
    res = str(game) + '/' + str(shot)
    return res


# Handler to draw on canvas

def draw(canvas):
    canvas.draw_text(convert(), [100, 112], 48, 'Red')
    canvas.draw_text(score(), [200, 50], 30, 'Blue')


# Create a frame and assign callbacks to event handlers

frame = simplegui.create_frame('Home', 300, 200)
frame.set_canvas_background('White')
frame.add_button('Start', start)
frame.add_button('Stop', stop)
frame.add_button('Reset', reset)
frame.set_draw_handler(draw)

# Timer

timer = simplegui.create_timer(100, start)

# Start the frame animation

frame.start()    