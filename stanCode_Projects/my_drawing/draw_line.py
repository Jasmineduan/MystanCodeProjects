"""
File: draw_line.py
Name: Jasmine Duan
-------------------------
The file shows how to use campy
mouse event to punch holes (GOval)
on GWindow
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 5


#Global Variable
window = GWindow()
mouse_x = 0
mouse_y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    global mouse_x, mouse_y
    if mouse_x == 0 and mouse_y == 0:
        circle = GOval(SIZE, SIZE)
        circle.filled = True
        circle.fill_color = 'white'
        window.add(circle, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
        mouse_x = mouse.x
        mouse_y = mouse.y
    else:
        circle = window.get_object_at(mouse_x, mouse_y)
        window.remove(circle)
        line = GLine(mouse_x, mouse_y, mouse.x, mouse.y)
        window.add(line)
        mouse_x = 0
        mouse_y = 0


if __name__ == "__main__":
    main()
