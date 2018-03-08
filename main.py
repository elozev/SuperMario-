try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from constants import Constants
from state import State

frame = simplegui.create_frame("SuperMario-", Constants.WIDTH, Constants.HEIGHT)

state = State(frame)
state.load_start_screen()
