try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Background:

    def __init__(self, img_url, canvas_width, canvas_height):
        self.image = simplegui.load_image(img_url)

        self.img_width = self.image.get_width()
        self.img_height = self.image.get_height()

        self.canvas_w = canvas_width
        self.canvas_h = canvas_height

        self.bg_animate_at_w = self.canvas_w
        self.progress = self.bg_animate_at_w

    def animate_background(self, canvas):
        canvas.draw_image(self.image,
                          (self.bg_animate_at_w / 2, self.img_height / 2),

                          (self.canvas_w, self.img_height),
                          (self.canvas_w / 2, self.canvas_h / 2),
                          (self.canvas_w, self.canvas_h))

    def update_bg(self, offset):
        if self.bg_animate_at_w >= self.img_width:
            self.bg_animate_at_w = self.canvas_w
        elif self.bg_animate_at_w <= self.canvas_w:
            self.bg_animate_at_w = self.img_width
        self.bg_animate_at_w += offset
        self.progress += offset

    def get_progress(self):
        return self.progress
