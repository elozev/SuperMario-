from screenloader import ScreenLoader


class Screen:
    def __init__(self, distance_between):
        self.screen_loader = ScreenLoader()
        self.distance_between = distance_between
        self.obstacles = self.screen_loader.load_first_set()
        self.screen_objects = self.screen_loader.load_screen_objects()

    def animate(self, canvas):
        for sb in self.screen_objects:
            sb.animate(canvas)

        for ob in self.obstacles:
            ob.animate(canvas)

    def update(self, offset):
        for sb in self.screen_objects:
            sb.update(offset)

        for ob in self.obstacles:
            ob.update(offset)
