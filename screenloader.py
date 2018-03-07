import random

from constants import Constants
from screenobjects import Obstacle
from screenobjects import ScreenObjects


class ScreenLoader:

    def __init__(self):
        self.clouds_distance_traveled = Constants.WIDTH
        self.bush_distance_traveled = Constants.WIDTH * random.randrange(4, 10)
        self.obstacles_distance_between = Constants.WIDTH

        # objects
        self.CLOUD = ScreenObjects(Constants.CLOUD, 7, random.randrange(50, 400), self.clouds_distance_traveled)
        # ground objects
        self.BUSH = ScreenObjects(Constants.BUSH, 7, Constants.BASE, self.bush_distance_traveled)
        self.PIPE = Obstacle(Constants.GREEN_PIPE, 6, Constants.BASE, self.obstacles_distance_between)
        self.QUESTION_BLOCK = Obstacle(Constants.QUESTION_BLOCK, 25, Constants.BLOCKS_POSITION,
                                       self.obstacles_distance_between)
        self.THREE_BLOCK_QUESTION = Obstacle(Constants.THREE_BLOCK_QUESTION, 3, Constants.BLOCKS_POSITION,
                                             self.obstacles_distance_between)
        self.THREE_BLOCK = Obstacle(Constants.THREE_BLOCK, 3, Constants.BLOCKS_POSITION,
                                    self.obstacles_distance_between)
        self.SIX_BLOCK = Obstacle(Constants.SIX_BLOCK, 3, Constants.BLOCKS_POSITION,
                                  self.obstacles_distance_between)
        self.EIGHT_BLOCK = Obstacle(Constants.EIGHT_BLOCK, 3, Constants.BLOCKS_POSITION,
                                    self.obstacles_distance_between)
        self.FALL_BLOCK = Obstacle(Constants.FALL_BLOCK, 1, Constants.FALL_BLOCK_OFFSET,
                                   self.obstacles_distance_between)
        self.obstacles = [self.PIPE, self.QUESTION_BLOCK, self.THREE_BLOCK_QUESTION, self.THREE_BLOCK, self.SIX_BLOCK,
                          self.EIGHT_BLOCK, self.FALL_BLOCK]

    def load_first_set(self):
        res = []
        for i in range(7):
            ob = self.obstacles[i]
            # ob = self.obstacles[0]
            ob.set_animate_at_w(self.obstacles_distance_between)
            res.append(ob)
            self.obstacles_distance_between += (ob.get_scaled_img_w() + 100)
            print("Scaled image width = " + str(ob.get_scaled_img_w()))
            print("Obstacles distance = " + str(self.obstacles_distance_between))
        return res

    def load_screen_objects(self):
        sb = []

        for i in range(5):
            sb.append(ScreenObjects(Constants.CLOUD, 7, random.randrange(50, 400), self.clouds_distance_traveled))
            sb.append(ScreenObjects(Constants.BUSH, 7, Constants.BASE, self.bush_distance_traveled))
            self.clouds_distance_traveled += random.randrange(300, 800)
            self.bush_distance_traveled += random.randrange(800, 1700)

        return sb
