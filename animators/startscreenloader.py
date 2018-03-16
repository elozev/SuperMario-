from constants import Constants
from handlers.imageinfo import ImageInfo

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


# <Leila code>
class StartScreenLoader:

    def __init__(self, state, is_gameover, progress, score):

        self.background = ImageInfo([320, 240], [640, 480])
        self.backgroundImage = simplegui.load_image("https://i.imgur.com/fY8di.jpg")

        self.game_over_logo = "http://www.powerpointhintergrund.com/uploads/red-text-game-over-png-transparent-4.png"
        # image
        self.bkinfo = ImageInfo([200, 150], [400, 300])
        self.bkimg = simplegui.load_image(
            "https://png.pngtree.com/thumb_back/fw800/back_pic/00/06/34/7956298ae43266e.jpg")

        if not is_gameover:
            self.logo = simplegui.load_image(
                "https://fontmeme.com/permalink/180307/3d9848417b5eb71c112dcb18cf23b2d0.png")
        else:
            self.logo = simplegui.load_image(
                "http://www.powerpointhintergrund.com/uploads/red-text-game-over-png-transparent-4.png")
        self.logo_info = ImageInfo([self.logo.get_width() / 2, self.logo.get_height() / 2],
                                   [self.logo.get_width(), self.logo.get_height()])
        self.time = 0
        self.state = state
        self.progress = progress
        self.score = score

    def draw(self, canvas):
        center = self.background.get_center()
        size = self.background.get_size()
        self.time += 1
        wtime = (self.time / 2) % Constants.WIDTH
        # two images which create a seemless looping background
        canvas.draw_image(self.backgroundImage, center, size, [(Constants.WIDTH / 2) + wtime, Constants.HEIGHT / 2],
                          [Constants.WIDTH, Constants.HEIGHT])
        canvas.draw_image(self.backgroundImage, center, size, [(-Constants.WIDTH / 2) + wtime, Constants.HEIGHT / 2],
                          [Constants.WIDTH, Constants.HEIGHT])

        # draw the lives and score to the screen
        canvas.draw_text("Score", [50, 50], 22, "White", "sans-serif")
        canvas.draw_text("Progress", [680, 50], 22, "White", "sans-serif")
        # TODO draw lives and score
        canvas.draw_text(str(self.score), [50, 80], 22, "White", "sans-serif")
        canvas.draw_text(str(self.progress), [680, 80], 22, "White", "sans-serif")

        canvas.draw_image(self.logo, self.logo_info.get_center(), self.logo_info.get_size(),
                          [Constants.WIDTH / 2, Constants.HEIGHT / 2], self.logo_info.get_size())

    # </Leila code>
    # <Emil code>
    def click(self, pos):
        self.state.load_playground()
