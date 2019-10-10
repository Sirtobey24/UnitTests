class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Circle(Point):
	def __init__(self, x, y, r):
		self.x = x
		self.y = y
		self.r = r
