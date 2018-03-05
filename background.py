try:
	import simplegui
except:
	import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
class Background:

	def __init__(self, img_url, canvas_width, canvas_height):
		self.image = simplegui.load_image(img_url)

		self.img_width = self.image.get_width()
		self.img_height = self.image.get_height()
		self.canvas_w = canvas_width
		self.canvas_h = canvas_height
		self.img_help = self.canvas_w


	def animate(self, canvas):
		#canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest)
		canvas.draw_image(self.image, 
			(self.img_help / 2, self.img_height / 2),
			
			(self.canvas_w, self.img_height),
			(self.canvas_w / 2, self.canvas_h / 2),
			(self.canvas_w, self.canvas_h))
		self.update(2)



	def update(self, offset):
		if(self.img_help >= self.img_width):
			self.img_help = self.canvas_w
		elif(self.img_help <= 0):
			self.img_help = self.img_width
		self.img_help += offset 