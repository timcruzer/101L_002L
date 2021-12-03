import turtle
class Point(object):
	def __init__(self, x, y, color):
        	self.x = x
        	self.y = y
        	self.color = color
	def draw(self):
	    	turtle.penup()
	    	turtle.goto(self.x, self.y)
	    	turtle.color(self.color)
	    	turtle.setheading(0)
	    	self.draw_action()
	def draw_action(self):
        	turtle.dot(50,"red")
class Box(Point):
	def __init__(self, x1, y1, width, height, color):
		self.x = x1
		self.y = y1
		self.width = width
		self.height = height
		self.color = color
		super().__init__(x1, y1, color)
	def draw_action(self):
		turtle.penup()
		turtle.goto(self.x, self.y)
		turtle.pendown()
		turtle.forward(self.width)
		turtle.right(90)
		turtle.forward(self.height)
		turtle.right(90)
		turtle.forward(self.width)
		turtle.right(90)
		turtle.forward(self.height)
class BoxFilled(Box):
	def __init__(self, x1, y1, width, height, color, fillcolor):
		self.x = x1
		self.y = y1
		self.width = width
		self.height = height
		self.color = color
		self.fillcolor = fillcolor
		super().__init__(x1, y1, width, height, color)		
	def draw_action(self):
		turtle.penup()
		turtle.goto(self.x, self.y)
		turtle.fillcolor(self.fillcolor)
		turtle.begin_fill()
		turtle.pendown()
		turtle.forward(self.width)
		turtle.right(90)
		turtle.forward(self.height)
		turtle.right(90)
		turtle.forward(self.width)
		turtle.right(90)
		turtle.forward(self.height)
		turtle.end_fill()	
class Circle(Point):
	def __init__(self, x1, y1, radius, color):
		self.x = x1
		self.y = y1
		self.radius = radius
		self.color = color
		super().__init__(x1, y1, color)

	def draw_action(self):
		turtle.penup()
		turtle.goto(self.x, self.y)
		turtle.pendown()
		turtle.circle(self.radius)		
class CircleFilled(Circle):
	def __init__(self, x1, y1, radius, color, fillcolor):
		self.x = x1
		self.y = y1
		self.radius = radius
		self.color = color
		self.fillcolor = fillcolor
		super().__init__(x1, y1, radius, color)
	def draw_action(self):
		turtle.penup()
		turtle.fillcolor(self.fillcolor)
		turtle.begin_fill()
		turtle.goto(self.x, self.y)
		turtle.pendown()
		turtle.circle(self.radius)		
		turtle.end_fill()