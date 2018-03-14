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
        self.line_x = Constants.WIDTH - 300
        self.going_down = True
        self.ground = ground
        self.falling_into_block = False

    def draw_ball(self, canvas):
        super(Grenade, self).draw_ball(canvas)
        # self.draw_line(canvas)

    def update_grenade(self):
        if not self.falling_into_block:
            if self.going_down:
                self.update_downwards()
            else:
                self.update_upwards()

            if self.is_stanionary():
                pass
                # TODO: explosion
        else:
            self.pos.add(self.vel)

    def update_downwards(self):
        if self.pos.y < Constants.HEIGHT - self.ground:
            self.vel.y += .8
            self.vel.divide(1.005)
            self.pos.add(self.vel)
        else:
            self.going_down = False
            self.vel.x *= -1

    def update_upwards(self):
        if self.vel.y >= 0.5:
            self.vel.y -= .8
            self.vel.divide(1.005)
            self.pos.subtract(self.vel)
        else:
            self.going_down = True
            self.vel.x *= -1

    def update_grenade_pos(self, offset):
        offset /= 2
        if self.pos.x < 0:
            self.pos.x += offset
        else:
            self.pos.x -= offset

    def is_stanionary(self):
        if self.vel.x < 0:
            return self.vel.x * -1 < 0.6
        else:
            return self.vel.x < 0.6

    def set_falling_into_block(self):
        self.falling_into_block = True

    def draw_line(self, canvas):
        canvas.draw_line((self.line_x, 0), (self.line_x, Constants.HEIGHT), 5, 'green')

    def check_collision(self, bounder):
        if self.pos.x + self.rad + self.line_width >= bounder:
            self.vel.x *= -1

    def bounce_off(self, collision_where):
        if collision_where == Constants.RIGHT_COLLISION or collision_where == Constants.LEFT_COLLISION:
            self.vel.x *= -1
        elif collision_where == Constants.TOP_COLLISION:
            self.going_down = True
            self.vel.x *= -1
