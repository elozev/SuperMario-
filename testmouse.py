from vector import Vector


class Mouse:

    # ball
    def __init__(self, ball):
        self.mouse_click = Vector(0, 0)
        self.ball = ball

    def click_handler(self, p):
        self.mouse_click = Vector(p[0], p[1])
        new_velocity = self.mouse_click.substract(self.ball.pos)
        self.ball.vel = new_velocity.normalize().multiply(3).divide(self.ball.rad / 40)
