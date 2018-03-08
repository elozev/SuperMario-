from constants import Constants
from handlers.imageinfo import ImageInfo

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


# <Leila code>
class StartScreenLoader:

    def __init__(self):
        self.background = ImageInfo([320, 240], [640, 480])
        self.backgroundImage = simplegui.load_image("https://i.imgur.com/fY8di.jpg")

        # image
        self.bkinfo = ImageInfo([200, 150], [400, 300])
        self.bkimg = simplegui.load_image(
            "https://png.pngtree.com/thumb_back/fw800/back_pic/00/06/34/7956298ae43266e.jpg")

        self.logo_info = ImageInfo([124, 12], [248, 23])
        self.logo = simplegui.load_image("https://fontmeme.com/permalink/180307/3d9848417b5eb71c112dcb18cf23b2d0.png")
        self.time = 0

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
        canvas.draw_text("Lives", [50, 50], 22, "White", "sans-serif")
        canvas.draw_text("Score", [680, 50], 22, "White", "sans-serif")
        # TODO draw lives and score
        canvas.draw_text(str(0), [50, 80], 22, "White", "sans-serif")
        canvas.draw_text(str(0), [680, 80], 22, "White", "sans-serif")

    def click(self, pos):
        center = [Constants.WIDTH / 2, Constants.HEIGHT / 2]
        size = self.bkinfo.get_size()
        inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
        inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
        # if (not started) and inwidth and inheight:
        #     started = True
        #     lives = 10
        #     score = 0
