try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import math

from constants import Constants
from player.vector import Vector


class TestBall:
    def __init__(self, pos, rad, line_width, col, ground, vel=Vector(0, 0)):
        self.is_in_left_collision = False
        self.is_in_right_collision = False
        self.pos = pos
        self.rad = rad
        self.line_width = line_width
        self.col = col
        self.vel = vel
        self.desired_size = rad
        self.collision_where = Constants.NONE_COLLISION

        self.ground = ground
        self.jumping = False
        self.acc = 4
        self.block_right_movement = False

    def draw_ball(self, canvas):
        canvas.draw_circle(self.pos.getP(), self.rad, self.line_width, self.col, self.col)

    def update(self, offset, block_right_movement):
        orientation = offset[1]
        self.block_right_movement = block_right_movement
        self.ground = Constants.GROUND_FOR_BALL
        self.is_in_right_collision = False
        self.is_in_left_collision = False

        if self.collision_where == Constants.BOTTOM_COLLISION:
            if orientation == Constants.ORIENTATION_UP:
                self.vel.y += 5
        elif self.collision_where == Constants.TOP_COLLISION:
            self.ground = self.pos.y
        elif self.collision_where == Constants.RIGHT_COLLISION:
            self.is_in_left_collision = True
            self.vel.x = 0
            self.pos.x += 1

        elif self.collision_where == Constants.LEFT_COLLISION:

            self.is_in_right_collision = True
            self.vel.x = 0
            # this resolves the sticky problem
            self.pos.x -= 1

        if self.check_mario_going_far_left():
            self.pos.x += 1
            self.vel.x = 0
        elif self.check_mario_going_far_right():
            self.pos.x -= 1
            self.vel.x = 0
        # if self.block_right_movement:
        #     self.pos.x -= 1

        self.collision_where = Constants.NONE_COLLISION
        self.update_pos()

    def update_pos(self):
        self.pos.add(self.vel)
        # if self.jumping:
        self.vel.y += Constants.GRAVITY
        if self.pos.y >= self.ground:
            self.jumping = False
            self.vel.y = 0
            self.pos.y = self.ground

    def update_on_key_down(self, key):
        if key == simplegui.KEY_MAP["up"]:
            self.jumping = True
            self.vel.y = -5
        elif key == simplegui.KEY_MAP["left"] and not self.is_in_left_collision:
            self.vel.x -= self.acc
        elif key == simplegui.KEY_MAP["right"] and not self.is_in_right_collision:
            self.vel.x += self.acc

    def update_on_key_up(self, key):
        if key == simplegui.KEY_MAP["up"]:
            self.vel.y = 0
        elif key == simplegui.KEY_MAP["left"]:
            self.vel.x = 0
        elif key == simplegui.KEY_MAP["right"]:
            self.vel.x = 0

    def set_collision_where(self, collision_where):
        self.collision_where = collision_where

    def animate(self, canvas):
        self.draw_ball(canvas)

    def check_mario_going_far_left(self):
        return self.pos.x - (self.rad + self.line_width) <= 0

    def check_mario_going_far_right(self):
        return self.pos.x + (self.rad + self.line_width) >= Constants.WIDTH

    def is_stanionary(self):
        return self.vel.x == 0 and self.vel.y == 0

    def distance_to(self, first, second):
        return math.sqrt(math.pow(second.pos.x - first.pos.x, 2) + math.pow(second.pos.y - first.pos.y, 2))


class Grenade(TestBall):

    def __init__(self, pos, rad, line_width, col, ground, vel=Vector(0, 0)):
        super(Grenade, self).__init__(pos, rad, line_width, col, ground, vel)
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
