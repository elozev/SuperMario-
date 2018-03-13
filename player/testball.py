import math

from constants import Constants
from player.vector import Vector


class TestBall:
    def __init__(self, pos, rad, line_width, col, vel=Vector(0, 0)):
        self.pos = pos
        self.rad = rad
        self.line_width = line_width
        self.col = col
        self.vel = vel
        self.desired_size = rad
        self.collision_where = Constants.NONE_COLLISION

    def draw_ball(self, canvas):
        canvas.draw_circle(self.pos.getP(), self.rad, self.line_width, self.col, self.col)

    def update(self, offset, block_right_movement):
        self.vel = Vector(0, 0)
        offset_movement = offset[0]
        orientation = offset[1]

        if orientation == Constants.ORIENTATION_UP:
            if not self.collision_where == Constants.BOTTOM_COLLISION:
                self.vel = Vector(0, offset_movement)
        elif orientation == Constants.ORIENTATION_DOWN:
            if not self.collision_where == Constants.TOP_COLLISION:
                self.vel = Vector(0, offset_movement)
        elif orientation == Constants.ORIENTATION_LEFT:
            if not self.collision_where == Constants.RIGHT_COLLISION and not self.check_mario_going_far_left():
                self.vel = Vector(offset_movement, 0)
        elif orientation == Constants.ORIENTATION_RIGHT:
            if not self.collision_where == Constants.LEFT_COLLISION:
                if not block_right_movement:
                    self.vel = Vector(offset_movement, 0)
        self.collision_where = Constants.NONE_COLLISION
        self.update_pos()

    def update_pos(self):
        self.pos.add(self.vel)

    def set_collision_where(self, collision_where):
        self.collision_where = collision_where

    def animate(self, canvas):
        self.draw_ball(canvas)

    def check_mario_going_far_left(self):
        return self.pos.x - (self.rad + self.line_width) <= 0

    def is_stanionary(self):
        return self.vel.x == 0 and self.vel.y == 0

    def distance_to(self, first, second):
        return math.sqrt(math.pow(second.pos.x - first.pos.x, 2) + math.pow(second.pos.y - first.pos.y, 2))


class Grenade(TestBall):

    def __init__(self, pos, rad, line_width, col, ground, vel=Vector(0, 0)):
        super(Grenade, self).__init__(pos, rad, line_width, col, vel)
        self.going_down = True
        self.ground = ground
        self.gravity = 0.98
        self.vel.x = 4

    def update_grenade(self):
        if self.going_down:
            self.update_downwards()
        else:
            self.update_upwards()
        print(self.vel.x)

    def update_downwards(self):
        if self.pos.y < Constants.HEIGHT - self.ground:
            self.vel.y += .8
            self.vel.divide(1.005)
            self.pos.add(self.vel)
        else:
            self.going_down = False
            self.vel.x *= -1

    def update_upwards(self):
        if self.vel.y >= 0.01:
            self.vel.y -= .8
            self.vel.divide(1.005)
            self.pos.substract(self.vel)
        else:
            self.going_down = True
            self.vel.x *= -1
