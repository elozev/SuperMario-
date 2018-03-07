try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class ScreenObjects:

    def __init__(self, img_url, scale, base, start_at):
        self.img = simplegui.load_image(img_url)
        self.img_w = self.img.get_width()
        self.img_h = self.img.get_height()
        self.scaled_img_w = self.img_w / scale
        self.scaled_img_h = self.img_h / scale
        self.base = base
        self.animate_at_w = start_at
        self.margin = 150

    def animate(self, canvas):
        canvas.draw_image(self.img,
                          (self.img_w / 2, self.img_h / 2),

                          (self.img_w, self.img_h),
                          (self.animate_at_w / 2, self.base),
                          (self.scaled_img_w, self.scaled_img_h))

    def update(self, offset):
        self.animate_at_w -= offset

    def __str__(self):
        return "Object: \nimage width: " + str(self.img_w) + \
               "\nimage height: " + str(self.img_h) + \
               "\nscaled width: " + str(self.scaled_img_w) + \
               "\nscaled height: " + str(self.scaled_img_h) + \
               "\nbase: " + str(self.base) + \
               "\nanimate at: " + str(self.animate_at_w)

    def get_scaled_img_w(self):
        return self.scaled_img_w + self.margin


class Obstacle(ScreenObjects):

    def __init__(self, img_url, scale, base, start_at):
        super(Obstacle, self).__init__(img_url, scale, base, start_at)

    def update(self, offset):
        self.animate_at_w -= offset

    def is_colliding_with_ball(self, ball, canvas):

        box_pos_x = self.animate_at_w / 2 - self.scaled_img_w / 2
        box_pos_y = self.base - self.scaled_img_h / 2

        canvas.draw_circle((box_pos_x, box_pos_y), 5, 1, 'white', 'white')
        canvas.draw_circle((box_pos_x - self.scaled_img_w, box_pos_y), 5, 1, 'white', 'white')
        canvas.draw_circle((box_pos_x - self.scaled_img_w, box_pos_y - self.scaled_img_h), 5, 1, 'white', 'white')
        canvas.draw_circle((box_pos_x, box_pos_y - self.scaled_img_h), 5, 1, 'white', 'white')

        # canvas.draw_circle((box_x, box_y), 3, 1, 'red', 'red')
        # canvas.draw_circle((box_x, box_y), 3, 1, 'red', 'red')

        canvas.draw_polygon([(box_pos_x, box_pos_y), (box_pos_x + self.scaled_img_w, box_pos_y),
                             (box_pos_x + self.scaled_img_w, box_pos_y + self.scaled_img_h),
                             (box_pos_x, box_pos_y + self.scaled_img_h)], 2, 'Green')

        return ball.pos.x + ball.rad > box_pos_x and \
               ball.pos.y + ball.rad > box_pos_y and \
               ball.pos.x - ball.rad < box_pos_x + self.scaled_img_w and \
               ball.pos.y - ball.rad < box_pos_y + self.scaled_img_h
