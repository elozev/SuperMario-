import random

from constants import Constants
from screenobjects import Obstacle
from screenobjects import ScreenObjects


class ScreenLoader:

    def __init__(self):
        self.clouds_distance_traveled = Constants.WIDTH
        self.bush_distance_traveled = Constants.WIDTH * random.randrange(4, 10)
        self.obstacles_distance_between = Constants.WIDTH

    def load_first_set(self):
        res = []
        for i in range(8):
            ob = self.get_random_object()
            res.append(ob)
            self.obstacles_distance_between += (ob.get_scaled_img_w() + 200)
            print("scaled img w: " + str(ob.get_scaled_img_w()))
        return res

    def get_random_object(self):
        r = random.randrange(0, 8)
        if r == 0:
            return ScreenObjects(Constants.BUSH, 7, Constants.BASE, self.bush_distance_traveled)
        elif r == 1:
            return Obstacle(Constants.GREEN_PIPE, 6, Constants.BASE, self.obstacles_distance_between)
        elif r == 2:
            return Obstacle(Constants.QUESTION_BLOCK, 30, Constants.BLOCKS_POSITION,
                            self.obstacles_distance_between)
        elif r == 3:
            return Obstacle(Constants.THREE_BLOCK_QUESTION, 3, Constants.BLOCKS_POSITION,
                            self.obstacles_distance_between)
        elif r == 4:
            return Obstacle(Constants.THREE_BLOCK, 3, Constants.BLOCKS_POSITION,
                            self.obstacles_distance_between)
        elif r == 5:
            return Obstacle(Constants.SIX_BLOCK, 3, Constants.BLOCKS_POSITION,
                            self.obstacles_distance_between)
        elif r == 6:
            return Obstacle(Constants.EIGHT_BLOCK, 3, Constants.BLOCKS_POSITION,
                            self.obstacles_distance_between)
        elif r == 7:
            return Obstacle(Constants.FALL_BLOCK, 1, Constants.FALL_BLOCK_OFFSET,
                            self.obstacles_distance_between)

    def load_screen_objects(self):
        sb = []
        for i in range(5):
            sb.append(ScreenObjects(Constants.CLOUD, 7, random.randrange(50, 400), self.clouds_distance_traveled))
            self.clouds_distance_traveled += random.randrange(300, 800)
        return sb
