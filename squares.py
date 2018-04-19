import turtle, random

screen = turtle.Screen()
screen.colormode(255)
screen.bgcolor((0,0,0))
steve = turtle.Turtle()
steve.shape("turtle")

square_size = 20
size = 10
spacing = 1.5

while True:
	steve.penup()
	steve.setpos((-spacing*square_size*size/2.,-spacing*square_size*size/2.))
	for layers in range(2):
		for y in range(size):
			for x in range(size):
				r = random.randrange(0,255)
				g = random.randrange(0,255)
				b = random.randrange(0,255)
				steve.pencolor((r,g,b))
				steve.pendown()
				for sides in range(4):
					steve.forward(square_size)
					steve.left(90)
				steve.penup()
				steve.forward(spacing*square_size)
			steve.left(180)
			steve.forward(spacing*square_size*size)
			steve.right(90)
			steve.forward(spacing*square_size)
			steve.right(90)
		steve.setpos((-spacing*square_size*size/2.+square_size*spacing*.5,-spacing*square_size*size/2.+square_size*spacing*.5))
		size-=1
	steve.clear()
	size+=2
	
	
		

screen.exitonclick()
