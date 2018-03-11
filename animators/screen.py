from animators.screenloader import ScreenLoader
from animators.screenobjects import Obstacle
from constants import Constants
from player.collision import Collision
from player.testball import TestBall
from player.vector import Vector


class Screen:
    def __init__(self, background):
        self.canvas = 0
        self.screen_loader = ScreenLoader()

        self.obstacles = self.generate_new_obstacles(Constants.WIDTH * 2)
        self.screen_objects = self.generate_clouds()
        self.background = background

        self.test_ball = TestBall(Vector(400, 400), 30, 2, 'red')

        self.collision_handler = Collision()

        self.block_background_movement = False
        # TODO: change this to reference from screenloader.py
        self.ball_blocked_by_ob = Obstacle(Constants.GREEN_PIPE, 6, Constants.BASE, 0)
        self.ball_blocked_by_ob.animate_at_w = 0
        self.is_background_moving = True

    def animate(self, canvas):
        # background
        self.background.animate_background(canvas)
        # obstacles, bushes and clouds
        for sb in self.screen_objects:
            sb.animate(canvas)
        for ob in self.obstacles:
            ob.animate(canvas)
        # moving ball
        self.test_ball.animate(canvas)
        self.canvas = canvas

    def update(self, offset):
        # checks is more obstacles are needed and generates if so
        self.check_distance_traveled()
        self.test_ball.update(offset, self.is_background_moving)
        self.move_bg_after_hero_is_middle(offset)

    def move_bg_after_hero_is_middle(self, offset):
        ball_rad_line_w = self.test_ball.rad + self.test_ball.line_width
        move_screen_with = 0

        self.is_background_moving = self.test_ball.pos.x + ball_rad_line_w > Constants.WIDTH / 2 + 50 and not self.block_background_movement
        if self.is_background_moving and offset[1] == Constants.ORIENTATION_RIGHT:
            move_screen_with = 10

        self.update_screen_objects(move_screen_with)

    def update_screen_objects(self, offset):
        self.background.update_bg(offset)
        for sb in self.screen_objects:
            sb.update(offset)
        for ob in self.obstacles:
            ob.update(offset)
            if self.collision_handler.is_colliding_with_ball(ob, self.test_ball, self.canvas):
                collision_where = self.collision_handler.determine_collision_location(ob, self.test_ball)
                self.collision_handler.trigger_action(ob, self.test_ball)

                self.test_ball.set_collision_where(collision_where)
                self.block_background_movement = True
                self.ball_blocked_by_ob = ob
            else:
                if self.ball_blocked_by_ob == ob:
                    self.block_background_movement = False

    def check_distance_traveled(self):
        if self.background.get_progress() >= self.screen_loader.get_obstacles_distance_traveled() - 2.5 * Constants.WIDTH:
            self.obstacles.extend(self.generate_new_obstacles(self.background.get_progress()))

    def check_clouds_enough(self):
        if self.background.get_progress() >= self.screen_loader.clouds_distance_traveled:
            self.screen_objects.extend(self.generate_clouds())

    def generate_new_obstacles(self, start_at):
        return self.screen_loader.load_obstacles(start_at)

    def generate_clouds(self):
        return self.screen_loader.load_clouds()
