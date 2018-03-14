import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from player.vector import Vector


class Coin:
    COLUMNS = 4
    ROWS = 1
    URL = "https://i.imgur.com/K6pxBXz.png"

    def __init__(self, pos):
        self.pos = pos
        self.image = simplegui.load_image(Coin.URL)
        self.image_w = self.image.get_width()
        self.image_h = self.image.get_height()
        self.vel = Vector(0, 5)
        self.max_upwards_position = self.pos.y - 150
        self.original_downwards_position = self.pos.y
        self.is_going_up = True
        self.hide_image = False

    def animate(self, canvas):
        if not self.hide_image:
            canvas.draw_image(self.image,
                              (self.image_w / 2, self.image_h / 2),
                              (self.image_w, self.image_h),
                              (self.pos.x / 2, self.pos.y - 50),
                              (50, 50))

    def update(self):
        if self.is_going_up:
            if self.pos.y <= self.max_upwards_position:
                self.is_going_up = False
            self.pos.subtract(self.vel)
        else:
            if self.pos.y <= self.original_downwards_position:
                self.pos.add(self.vel)
            else:
                self.hide_image = True

    def update_pos(self, offset):
        self.pos.x -= offset

    def get_hide_image(self):
        return self.hide_image
