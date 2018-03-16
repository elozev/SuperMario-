from animators.background import Background
from animators.screen import Screen
from animators.startscreenloader import StartScreenLoader
from constants import Constants
from handlers.keyboard import Keyboard
from handlers.mouse import Mouse
from player.testball import TestBall
from player.vector import Vector


class State:

    def __init__(self, frame):
        self.frame = frame
        ground = Constants.GROUND_FOR_BALL
        self.test_ball = TestBall(Vector(100, ground), 10, 2, 'blue', ground)
        self.kb = Keyboard(self.test_ball)
        self.bg = Background(Constants.BACKGROUND_IMAGE, Constants.WIDTH, Constants.HEIGHT)
        self.sc = Screen(self.bg, self.test_ball)
        self.start_screen = StartScreenLoader(self)
        self.ms = Mouse(self.sc)

    def load_start_screen(self):
        self.frame.set_mouseclick_handler(self.start_screen.click)
        self.frame.set_draw_handler(self.start_screen.draw)
        self.frame.start()

    def draw_handler(self, canvas):
        self.sc.animate(canvas)
        self.sc.update(self.kb.background_movement())

    def load_playground(self):
        self.frame.set_draw_handler(self.draw_handler)
        self.frame.set_keydown_handler(self.kb.key_down_handler)
        self.frame.set_keyup_handler(self.kb.key_up_handler)
        self.frame.set_mouseclick_handler(self.ms.click_handler)
        # self.frame.set_mouseclick_handler(self.sc.ms.click_handler)
        # self.frame.start()

    def game_over(self):
        # TODO: 1.Get results 2. Unload background with obstacles and mario
        # TODO: 3. Display game over screen with presenting results 4. Button for restarting game
        pass
