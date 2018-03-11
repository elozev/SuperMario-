from constants import Constants

try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Keyboard:

    def __init__(self):
        self.current_key = ''

    def keydown_handler(self, key):
        self.current_key = key

    def keyup_handler(self, key):
        self.current_key = ''

    def background_movement(self):
        if self.current_key == simplegui.KEY_MAP["left"]:
            return -10, Constants.ORIENTATION_LEFT
        elif self.current_key == simplegui.KEY_MAP["right"]:
            return 10, Constants.ORIENTATION_RIGHT
        elif self.current_key == simplegui.KEY_MAP["up"]:
            return -10, Constants.ORIENTATION_UP
        elif self.current_key == simplegui.KEY_MAP["down"]:
            return 10, Constants.ORIENTATION_DOWN
        else:
            return 0, Constants.ORIENTATION_NONE
