from constants import Constants
from player.testball import TestBall
from player.vector import Vector


class Collision:

    def is_colliding_with_ball(self, obstacle, ball, canvas):
        box_pos_x = obstacle.animate_at_w / 2 - obstacle.scaled_img_w / 2
        box_pos_y = obstacle.base - obstacle.scaled_img_h / 2

        # draw polygon around the obstacle
        canvas.draw_polygon([(box_pos_x, box_pos_y), (box_pos_x + obstacle.scaled_img_w, box_pos_y),
                             (box_pos_x + obstacle.scaled_img_w, box_pos_y + obstacle.scaled_img_h),
                             (box_pos_x, box_pos_y + obstacle.scaled_img_h)], 2, 'Green')

        return ball.pos.x + ball.rad > box_pos_x and \
               ball.pos.y + ball.rad > box_pos_y and \
               ball.pos.x - ball.rad < box_pos_x + obstacle.scaled_img_w and \
               ball.pos.y - ball.rad < box_pos_y + obstacle.scaled_img_h

    def two_ball_collision(self, ball_1, ball_2):
        return TestBall.distance_to(ball_1, ball_2) - (
                ball_1.rad + ball_1.line_width + ball_2.rad + ball_2.line_width) <= 0

    def determine_collision_location(self, obstacle, ball):
        box_pos_x = obstacle.animate_at_w / 2 - obstacle.scaled_img_w / 2
        box_pos_y = obstacle.base - obstacle.scaled_img_h / 2

        ball_bottom = ball.pos.y + ball.rad + ball.line_width
        box_bottom = box_pos_y + obstacle.scaled_img_h
        ball_right = ball.pos.x + ball.rad + ball.line_width
        box_right = box_pos_x + obstacle.scaled_img_w

        bottom_c = box_bottom - ball.pos.y
        top_c = ball_bottom - box_pos_y
        left_c = ball_right - box_pos_x
        right_c = box_right - ball.pos.x

        if top_c < bottom_c and top_c < left_c and top_c < right_c:
            return Constants.TOP_COLLISION
        elif bottom_c < top_c and bottom_c < left_c and bottom_c < right_c:
            return Constants.BOTTOM_COLLISION
        elif left_c < top_c and left_c < right_c and left_c < bottom_c:
            return Constants.LEFT_COLLISION
        elif right_c < top_c and right_c < bottom_c and right_c < left_c:
            return Constants.RIGHT_COLLISION

    def trigger_action(self, ob, ball, screen):
        if ob.type == Constants.FALL_BLOCK:
            if self.determine_collision_location(ob, ball) == Constants.TOP_COLLISION:
                print(10 * "GAME OVER ")

        # TODO trigger game over
        elif ob.type == Constants.QUESTION_BLOCK:
            if self.determine_collision_location(ob,
                                                 ball) == Constants.BOTTOM_COLLISION and not ob.get_power_up_activated():
                ob.set_power_up_activated()
                screen.generate_coin(ob.get_pos())
                print(10 * "POWER UP ")
        # TODO generate moving mushroom from there or coin
        elif ob.type == Constants.THREE_BLOCK_QUESTION:
            if self.determine_collision_location(ob,
                                                 ball) == Constants.BOTTOM_COLLISION and not ob.get_power_up_activated():
                print(10 * "POWER UP 3")
                ob.set_power_up_activated()
                screen.generate_coin(ob.get_pos())
        # TODO generate moving mushroom if the hit is in the middle or coin

    def grenade_collision_handler(self, ob, ball):
        if ob.type == Constants.FALL_BLOCK:
            if self.determine_collision_location(ob, ball) == Constants.TOP_COLLISION:
                ball.set_falling_into_block()
                ball.vel = Vector(ball.vel.x, 20)

    def enemy_collision_handler(self, ob, en):
        if ob.type == Constants.FALL_BLOCK:
            if self.determine_collision_location(ob, en.ball) == Constants.TOP_COLLISION:
                en.ball.vel = Vector(en.ball.vel.x, 20)
                en.vel = en.ball.vel
