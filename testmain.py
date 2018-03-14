import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from constants import Constants
from player.testball import Grenade
from player.vector import Vector


def handler(canvas):
    grenade.draw_ball(canvas)
    grenade.update_grenade()


pos = Vector(50, Constants.HEIGHT / 2)
grenade = Grenade(pos, 10, 2, 'RED', 100, Vector(3, 10))

frame = simplegui.create_frame("TEST", Constants.WIDTH, Constants.HEIGHT)
frame.set_draw_handler(handler)
frame.start()
