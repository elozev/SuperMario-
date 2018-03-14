class Mouse:

    def __init__(self, screen):
        self.screen = screen

    def click_handler(self, pos):
        self.screen.generate_grenade()
