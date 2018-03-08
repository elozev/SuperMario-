from player.collision import Collision
from constants import Constants
from animators.screenloader import ScreenLoader
from player.testball import TestBall
from handlers.testmouse import Mouse
from player.vector import Vector


class Screen:
    def __init__(self, background):
        self.screen_loader = ScreenLoader()

        self.obstacles = self.generate_new_obstacles(500)
        self.screen_objects = self.generate_clouds()
        self.background = background

        self.test_ball = TestBall(Vector(400, 400), 30, 2, 'red')
        self.ms = Mouse(self.test_ball)
        self.collision_handler = Collision()

    def animate(self, canvas):
        for sb in self.screen_objects:
            sb.animate(canvas)

        self.test_ball.animate(canvas)
        for ob in self.obstacles:
            ob.animate(canvas)

    def update(self, offset, canvas):
        self.check_distance_traveled()

        for sb in self.screen_objects:
            sb.update(offset)

        for ob in self.obstacles:
            ob.update(offset)
            if self.collision_handler.is_colliding_with_ball(ob, self.test_ball):
                # TODO trigger action
                self.collision_handler.trigger_action(ob.type)
                self.test_ball.vel = Vector(0, 0)

    def check_distance_traveled(self):
        if self.background.get_progress() >= self.screen_loader.get_obstacles_distance_traveled() - Constants.WIDTH:
            self.obstacles.extend(self.generate_new_obstacles(self.background.get_progress()))

    def check_clouds_enough(self):
        if self.background.get_progress() >= self.screen_loader.clouds_distance_traveled:
            self.screen_objects.extend(self.generate_clouds())

    def generate_new_obstacles(self, start_at):
        return self.screen_loader.load_obstacles(start_at)

    def generate_clouds(self):
        return self.screen_loader.load_clouds()
