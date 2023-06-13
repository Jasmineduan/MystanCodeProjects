"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    count = 0
    # Add the animation loop here!
    while count < NUM_LIVES:
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        graphics.ball.move(dx, dy)
        # ball touch the floor
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            print('c')
            graphics.reset_the_ball()
            graphics.start = False
            count += 1
        # ball touch ceiling and paddle
        if graphics.ball.y <= 0:
            # print('f')
            graphics.set_dy(-dy)
        # ball touch left and right walls
        if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
            graphics.set_dx(-dx)
        hit_once = False
        for i in range(0, graphics.ball.width + 1, graphics.ball.width):
            for j in range(0, graphics.ball.height + 1, graphics.ball.height):
                obj = graphics.window.get_object_at(graphics.ball.x+i, graphics.ball.y+j)
                if obj is not None:
                    if obj == graphics.paddle:
                        if dy > 0:
                            graphics.set_dy(-dy)
                    else:
                        if not hit_once:
                            # ball touch brick
                            graphics.window.remove(obj)
                            graphics.set_dy(-dy)
                            hit_once = True
                            # graphics.set_dx(-dx)
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
