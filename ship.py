from random import randint

class Ship :
	def __init__(self, Game) :
		self.config = Game.config
		self.window = Game.window
		self.setup_Location()

	def setup_Location(self) :
		x = randint(0, self.config.row-1) #0-4
		y = randint(0, self.config.column-1)
		self.location  = (x,y)
