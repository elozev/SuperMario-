from constants import Constants
from player.testball import TestBall
from player.vector import Vector

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


# <Arash code>
class Enemy:
    Row = 0
    column = 2
    Image_number = [Row, column]
    time = 0
    BACK_WIDTH = Constants.WIDTH
    BACK_HEIGHT = Constants.HEIGHT
    Goomba_image = simplegui.load_image("https://i.imgur.com/3aCYk4g.png?dl=1")
    Image_width = 37.6666666667
    Image_height = 43
    Image_size = ((Image_width, Image_height))
    Image_center = ((Image_width / 2, Image_height / 2))

    x = 60
    Tx = 0.5
    y = 3 * 391 / 4

    def __init__(self, row, column, Goomba_image, scale, pos):
        self.column = column
        self.row = row
        self.Goomba_image = Goomba_image
        self.Image_height = self.Goomba_image.get_height()
        self.scale = scale
        self.pos = pos
        self.vel = Vector(1, 0)
        self.counter = 0
        self.ball = TestBall(self.pos, self.Goomba_image.get_height() / 2, 1, 'rgba(0, 0, 0, 0)', self.pos.x, self.vel)

    # define draw handeler
    def draw(self, canvas):
        global x, time, Image_center, Image_number

        self.counter += 1
        if self.counter % 20 == 0:
            time = (time + 1) % (Enemy.Image_number[0] + Enemy.Image_number[1])

        curr_goomba_index = [time % Enemy.Image_number[1], time // Enemy.Image_number[1]]

        scaled_image = (Enemy.Image_size[0] * self.scale, Enemy.Image_size[1] * self.scale)
        canvas.draw_image(Enemy.Goomba_image, [Enemy.Image_center[0] + curr_goomba_index[0] * Enemy.Image_size[0],
                                               Enemy.Image_center[1] + curr_goomba_index[1] * Enemy.Image_size[1]],
                          Enemy.Image_size, self.pos.getP(), scaled_image)

        self.ball.draw_ball(canvas)
        self.update()

    def update(self):
        self.pos.add(self.vel)
        self.ball.vel = self.vel
        self.ball.update_mario()


en = Enemy(Enemy.Row, Enemy.column, Enemy.Goomba_image, 2, Vector(50, Constants.HEIGHT / 2))

# define frame +reg draw handler
screen = simplegui.create_frame("goomba sprite spice!!!!!!!!", Enemy.BACK_WIDTH, Enemy.BACK_HEIGHT)
screen.set_draw_handler(en.draw)
screen.set_canvas_background("Blue")
time = 0
# generate a goomba

# timercount = simplegui.create_timer(200, en.timercount_handler)
# timercount.start()

screen.start()

# </Arash code>
