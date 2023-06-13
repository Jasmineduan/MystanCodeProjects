"""
File: bouncing_ball.py
Name: Jasmine Duan
-------------------------
This file shows how to use campy
mouse event to make a ball jumping animation
on GWindow
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, x=START_X, y=START_Y)
    t = 0
    onmouseclicked(ball_remove)


def ball_remove(event):
    window.get_object_at(ball.x, ball.y)
    white_ball = GOval(0, 0)
    white_ball.filled = True
    white_ball.fill_color = 'white'
    white_ball.color = 'white'
    window.add(white_ball, event.x, event.y)
    if ball.x == START_X and ball.y == START_Y:
        vy = 5
        while True:
            ball.move(VX, vy)
            vy += GRAVITY
            if ball.y + ball.height >= window.height:
                vy = -vy * REDUCE
            elif ball.x >= window.width:
                window.add(ball, x=START_X, y=START_Y)
                break
            pause(DELAY)


if __name__ == "__main__":
    main()
