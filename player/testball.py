import math

from player.vector import Vector


class TestBall:
    def __init__(self, pos, rad, line_width, col, vel=Vector(0, 0)):
        self.pos = pos
        self.rad = rad
        self.line_width = line_width
        self.col = col
        self.vel = vel
        self.desired_size = rad

    def draw_ball(self, canvas):
        # if self.is_hitting_wall():
        #     self.normal_vector()

        canvas.draw_circle(self.pos.getP(), self.rad, self.line_width, self.col, self.col)

    def update(self):
        self.pos.add(self.vel)
        if self.rad < self.desired_size:
            self.rad += 0.1

    def animate(self, canvas):
        self.update()
        self.draw_ball(canvas)

    def is_stanionary(self):
        return self.vel.x == 0 and self.vel.y == 0

    # def is_hitting_wall(self):
    #     return ((self.pos.x >= (WIDTH - BORDER_WIDTH)) or
    #             (self.pos.x <= BORDER_WIDTH) or
    #             (self.pos.y >= (HEIGHT - BORDER_WIDTH)) or
    #             (self.pos.y <= BORDER_WIDTH))

    # def normal_vector(self):
    #     if (self.pos.x <= 0 or self.pos.x >= WIDTH):
    #         self.vel = Vector(self.vel.x * -1, self.vel.y)
    #     elif (self.pos.y <= 0 or self.pos.y >= HEIGHT):
    #         self.vel = Vector(self.vel.x, self.vel.y * -1)
    #
    # def enlarge(self, size):
    #     self.desired_size += size
    # pass

    def distance_to(self, first, second):
        return math.sqrt(math.pow(second.pos.x - first.pos.x, 2) + math.pow(second.pos.y - first.pos.y, 2))

    # def is_colliding(self, other):
    #     return self.distance_to(self, other) <= self.rad + other.rad + self.line_width + other.line_width

    def split(self):
        self.rad /= 2
        self.vel = self.vel.normalize().multiply(3).divide(self.rad / 40)
        return TestBall(self.pos.add(Vector(self.rad + 50, self.rad + 50)), self.rad, self.line_width, self.col, self.vel)

    def attach_to(self, other):
        pass

    def bounce_of(self, other):
        pass

    def get_pos_x_with_rad(self):
        return self.pos.x + self.rad + self.line_width

    def get_pos_y_with_rad(self):
        return self.pos.y + self.rad + self.line_width
