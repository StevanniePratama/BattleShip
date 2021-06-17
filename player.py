class Player :
	def __init__(self, name = "Sallini") :
		self.name = name
	
	def current_location(self, x, y) :
		self.location = (x,y)
