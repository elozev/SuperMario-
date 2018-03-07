try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random

from background import Background
from constants import Constants
from keyboard import Keyboard
from screen import Screen

WIDTH = Constants.WIDTH
HEIGHT = Constants.HEIGHT


def draw_handler(canvas):
    global counter
    counter += 1

    bg.animate_background(canvas)
    sc.animate(canvas)

    bg.update_bg(kb.background_movement())
    sc.update(kb.background_movement())


counter = 0
img = "https://i.imgur.com/uYaDwBC.jpg"

bg = Background(img, WIDTH, HEIGHT)
sc = Screen(100)
kb = Keyboard()

frame = simplegui.create_frame("SuperMario-", WIDTH, HEIGHT)
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(kb.keydown_handler)
frame.set_keyup_handler(kb.keyup_handler)
frame.start()
