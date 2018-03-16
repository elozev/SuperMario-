from constants import Constants
from player.vector import Vector

try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Keyboard:

    def __init__(self, ball):
        self.current_key = ''
        # <Sophie code>
        self.jumping = False
        self.vel = Vector(0, 0)
        self.acc = 1
        self.last_key_up = ''
        self.ball = ball

    def key_down_handler(self, key):
        self.current_key = key
        self.ball.update_on_key_down(key)

    def key_up_handler(self, key):
        self.current_key = ''
        self.ball.update_on_key_up(key)

    def background_movement(self):
        if self.current_key == simplegui.KEY_MAP["left"]:
            return -Constants.SCREEN_MOVEMENT_SPEED, Constants.ORIENTATION_LEFT
        elif self.current_key == simplegui.KEY_MAP["right"]:
            return Constants.SCREEN_MOVEMENT_SPEED, Constants.ORIENTATION_RIGHT
        elif self.current_key == simplegui.KEY_MAP["up"]:
            return -Constants.SCREEN_MOVEMENT_SPEED, Constants.ORIENTATION_UP
        # elif self.current_key == simplegui.KEY_MAP["down"]:
        #     return Constants.SCREEN_MOVEMENT_SPEED, Constants.ORIENTATION_DOWN
        else:
            return 0, Constants.ORIENTATION_NONE, self.last_key_up
