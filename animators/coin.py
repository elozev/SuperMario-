import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from constants import Constants
from player.vector import Vector


class Coin:
    COLUMNS = 4
    ROWS = 1
    URL = "https://i.imgur.com/K6pxBXz.png"

    def __init__(self):
        self.image = simplegui.load_image(Coin.URL)
        self.image_w = self.image.get_width()
        self.image_h = self.image.get_height()
        self.pos = Vector(Constants.WIDTH, Constants.HEIGHT)
        self.max_upwards_position = self.pos.y - 150
        self.original_downwards_position = self.pos.y
        self.is_going_up = True

        # url = https://i.imgur.com/s2IT6no.png

    def animate(self, canvas):
        # canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest)
        canvas.draw_image(self.image,
                          (self.image_w / 2, self.image_h / 2),
                          (self.image_w, self.image_h),
                          (self.pos.x / 2, self.pos.y / 2),
                          (50, 50))

    def update(self):
        if self.is_going_up:
            if self.pos.y <= self.max_upwards_position:
                self.is_going_up = False
            self.pos.y -= 5
        else:
            if self.pos.y <= self.original_downwards_position:
                self.pos.y += 5
