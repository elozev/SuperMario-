from constants import Constants


class Collision:

    def is_colliding_with_ball(self, obstacle, ball):
        box_pos_x = obstacle.animate_at_w / 2 - obstacle.scaled_img_w / 2
        box_pos_y = obstacle.base - obstacle.scaled_img_h / 2

        # draw polygon around the obstacle
        # canvas.draw_polygon([(box_pos_x, box_pos_y), (box_pos_x + self.scaled_img_w, box_pos_y),
        #                      (box_pos_x + self.scaled_img_w, box_pos_y + self.scaled_img_h),
        #                      (box_pos_x, box_pos_y + self.scaled_img_h)], 2, 'Green')

        return ball.pos.x + ball.rad > box_pos_x and \
               ball.pos.y + ball.rad > box_pos_y and \
               ball.pos.x - ball.rad < box_pos_x + obstacle.scaled_img_w and \
               ball.pos.y - ball.rad < box_pos_y + obstacle.scaled_img_h

    def trigger_action(self, type):
        if type == Constants.TYPE_FALL_BLOCK:
            # TODO end game and mario fall - velocity (0, 5)
            pass
        elif type == Constants.QUESTION_BLOCK:
            # TODO generate moving mushroom from there
            pass
        elif type == Constants.THREE_BLOCK_QUESTION:
            # TODO generate moving mushroom if the hit is in the middle
            pass
