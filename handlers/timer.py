#Kieran's code for implementing a timer once the player has died.
try:
  import simplegui
except:
  import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
  
from animators.screenloader import 
 
class Timer:
  
  def __init__(self):
      self.current_time = 0
      
  def timer_handler():
      current_time = current_time + 1
      if #Need to implement conditional statement for when the user's lives have reached 0.
          timer.stop()
          print("Your run lasted "+current_time+" seconds.")
     
      
timer = simplegui.create_timer(1000, timer_handler)
timer.start()
          
