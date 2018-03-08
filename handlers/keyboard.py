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
            return -10
        elif self.current_key == simplegui.KEY_MAP["right"]:
            return 10
        elif self.current_key == '':
            return 0
