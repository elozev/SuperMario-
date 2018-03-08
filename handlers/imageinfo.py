class ImageInfo:

    def __init__(self, center, size, radius=0, life=None, animated=False):
        self.center = center
        self.size = size
        self.radius = radius
        if life:
            self.life = life
        else:
            self.life = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_life(self):
        return self.life

    def get_animated(self):
        return self.animated