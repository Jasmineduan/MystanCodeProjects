"""
File: my_drawing.py
Name: Jasmine Duan
----------------------
This file shows how to use campy to paint
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GArc, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Wishing all mothers a wonderful Mother's Day ever.
    """
    window = GWindow(800, 500, title="Happy Mother's Day")
    background = GRect(800, 500)
    background.filled = True
    background.fill_color = 'lavenderblush'
    window.add(background)
    face = GOval(160, 130)
    face.filled = True
    face.fill_color = 'sienna'
    face.color = 'sienna'
    window.add(face, x=(window.width-face.width)/2, y=(window.height-face.height)/2)
    ear_l = GOval(50, 50)
    ear_l.filled = True
    ear_l.fill_color = 'sienna'
    ear_l.color = 'sienna'
    window.add(ear_l, x=340, y=175)
    ear_r = GOval(50, 50)
    ear_r.filled = True
    ear_r.fill_color = 'sienna'
    ear_r.color = 'sienna'
    window.add(ear_r, x=410, y=175)
    eye_l = GOval(11, 11)
    eye_l.filled = True
    eye_l.fill_color ='black'
    window.add(eye_l, x=385, y=240)
    eye_r = GOval(11, 11)
    eye_r.filled = True
    eye_r.fill_color = 'black'
    window.add(eye_r, x=410, y=240)
    nose_b = GOval(30, 40)
    nose_b.filled = True
    nose_b.fill_color = 'peachpuff'
    nose_b.color = 'peachpuff'
    window.add(nose_b, x=388, y=254)
    nose = GOval(9, 9)
    nose.filled = True
    nose.fill_color = 'black'
    window.add(nose, x=399, y=257)
    mouse1 = GLine(404, 259, 404, 277)
    window.add(mouse1)
    mouse2 = GLine(404, 277, 395, 285)
    window.add(mouse2)
    mouse3 = GLine(404, 277, 413, 285)
    window.add(mouse3)
    eari_l = GArc(30, 30, 15, 195)
    eari_l.filled = True
    eari_l.fill_color = 'darkred'
    eari_l.color = 'darkred'
    window.add(eari_l, x=349, y=180)
    eari_r = GArc(30, 30, 330, 180)
    eari_r.filled = True
    eari_r.fill_color = 'darkred'
    eari_r.color = 'darkred'
    window.add(eari_r, x=426, y=182)
    body1 = GRect(80, 100)
    body1.filled = True
    body1.fill_color = 'sienna'
    body1.color = 'sienna'
    window.add(body1, x=360, y=300)
    leg_l = GOval(50, 40)
    leg_l.filled = True
    leg_l.fill_color = 'sienna'
    leg_l.color = 'sienna'
    window.add(leg_l, x=350, y=380)
    leg_r = GOval(50, 40)
    leg_r.filled = True
    leg_r.fill_color = 'sienna'
    leg_r.color = 'sienna'
    window.add(leg_r, x=400, y=380)
    hand_r = GOval(85, 30)
    hand_r.filled = True
    hand_r.fill_color = 'sienna'
    hand_r.color = 'sienna'
    window.add(hand_r, x=400, y=300)
    hand_l = GOval(85, 28)
    hand_l.filled = True
    hand_l.fill_color = 'sienna'
    hand_l.color = 'sienna'
    window.add(hand_l, x=380, y=323)
    leaf = GRect(9, 153)
    leaf.filled = True
    leaf.fill_color = 'green'
    leaf.color = 'green'
    window.add(leaf, x=460, y=150)
    leaf1 = GRect(9, 153)
    leaf1.filled = True
    leaf1.fill_color = 'green'
    leaf1.color = 'green'
    window.add(leaf1, x=460, y=150)
    flower1 = GOval(15, 40)
    flower1.filled = True
    flower1.fill_color = 'hotpink'
    flower1.color = 'hotpink'
    window.add(flower1, x=440, y=95)
    flower2 = GOval(15, 40)
    flower2.filled = True
    flower2.fill_color = 'hotpink'
    flower2.color = 'hotpink'
    window.add(flower2, x=450, y=95)
    flower3 = GOval(15, 40)
    flower3.filled = True
    flower3.fill_color = 'hotpink'
    flower3.color = 'hotpink'
    window.add(flower3, x=460, y=95)
    flower4 = GOval(15, 40)
    flower4.filled = True
    flower4.fill_color = 'hotpink'
    flower4.color = 'hotpink'
    window.add(flower4, x=470, y=95)
    leaf_head = GPolygon()
    leaf_head.add_vertex((465, 160))
    leaf_head.add_vertex((440, 130))
    leaf_head.add_vertex((485, 130))
    leaf_head.filled = True
    leaf_head.fill_color = 'green'
    leaf_head.color = 'green'
    window.add(leaf_head)
    label = GLabel("Happy Mother's Day")
    label.font = '-40'
    label.color = 'red'
    window.add(label, x=200, y=70)
    heart = GLine(157, 324, 102, 259)
    heart.color = 'red'
    window.add(heart)
    heart1 = GLine(157, 324, 203, 259)
    heart1.color = 'red'
    window.add(heart1)
    heart_h = GArc(50, 100, 0, 180)
    heart_h.color = 'red'
    window.add(heart_h, x=103, y=239)
    heart_h1 = GArc(50, 100, 0, 180)
    heart_h1.color = 'red'
    window.add(heart_h1, x=153, y=239)
    heart2 = GLine(263, 433, 222, 382)
    heart2.color = 'red'
    window.add(heart2)
    heart3 = GLine(263, 433, 300, 384)
    heart3.color = 'red'
    window.add(heart3)
    heart_h2 = GArc(40, 100, 0, 180)
    heart_h2.color = 'red'
    window.add(heart_h2, x=220, y=360)
    heart_h3 = GArc(40, 100, 0, 180)
    heart_h3.color = 'red'
    window.add(heart_h3, x=260, y=360)
    heart_h4 = GArc(80, 180, 0, 180)
    heart_h4.color = 'red'
    window.add(heart_h4, x=510, y=300)
    heart_h5 = GArc(80, 180, 0, 180)
    heart_h5.color = 'red'
    window.add(heart_h5, x=590, y=300)
    heart4 = GLine(589, 424, 509, 341)
    heart4.color = 'red'
    window.add(heart4)
    heart5 = GLine(589, 424, 670, 344)
    heart5.color = 'red'
    window.add(heart5)
    heart_h6 = GArc(30, 60, 0, 180)
    heart_h6.color = 'red'
    window.add(heart_h6, x=650, y=150)
    heart_h7 = GArc(30, 60, 0, 180)
    heart_h7.color = 'red'
    window.add(heart_h7, x=680, y=150)
    heart6 = GLine(650, 164, 681, 200)
    heart6.color = 'red'
    window.add(heart6)
    heart7 = GLine(710, 165, 681, 200)
    heart7.color = 'red'
    window.add(heart7)


if __name__ == '__main__':
    main()
