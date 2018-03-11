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
        # if self.is_hitting_wall():
        #     self.normal_vector()

        canvas.draw_circle(self.pos.getP(), self.rad, self.line_width, self.col, self.col)

    def update(self, offset, block_right_movement):
        self.vel = Vector(0, 0)
        offset_movement = offset[0]
        orientation = offset[1]

        print(self.collision_where)

        if orientation == Constants.ORIENTATION_UP:
            if not self.collision_where == Constants.BOTTOM_COLLISION:
                self.vel = Vector(0, offset_movement)
        elif orientation == Constants.ORIENTATION_DOWN:
            if not self.collision_where == Constants.TOP_COLLISION:
                self.vel = Vector(0, offset_movement)
        elif orientation == Constants.ORIENTATION_LEFT:
            if not self.collision_where == Constants.RIGHT_COLLISION:
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

    def is_stanionary(self):
        return self.vel.x == 0 and self.vel.y == 0

    def distance_to(self, first, second):
        return math.sqrt(math.pow(second.pos.x - first.pos.x, 2) + math.pow(second.pos.y - first.pos.y, 2))
