try:
	import simplegui
except:
	import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from background import Background
from keyboard import Keyboard

WIDTH = 800
HEIGHT = 800

print("Hello")


def draw_handler(canvas):
	global counter
	counter += 1
	bg.animate(canvas)
	bg.update(kb.background_movement())



counter = 0
img = "https://i.imgur.com/uYaDwBC.jpg"

bg = Background(img, WIDTH, HEIGHT)
kb = Keyboard()


frame = simplegui.create_frame("SuperMario-", WIDTH, HEIGHT)
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(kb.keydown_handler)
frame.set_keyup_handler(kb.keyup_handler)
frame.start()