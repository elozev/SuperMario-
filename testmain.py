import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from animators.coin import Coin
from constants import Constants


def handler(canvas):
    coin.animate(canvas)
    coin.update()


coin = Coin()

frame = simplegui.create_frame("TEST", Constants.WIDTH, Constants.HEIGHT)
frame.set_draw_handler(handler)
frame.start()
