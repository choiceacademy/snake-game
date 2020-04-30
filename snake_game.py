
#work on scoreboard experience; currently shows old high score until you earn new high score
#how do we allow the next player to start a new game without exiting
#better snake graphic
#check left,right,upper and lower boundaries


import turtle
import time
import random
import winsound

delay = 0.1

#score
score = 0
high_score = 0

turtle.register_shape("apple.gif")

#set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.setup(width=600, height=600)
wn.bgpic("grass-2.gif")
wn.tracer(0) #Turns off the screen updates

name = turtle.textinput("Enter your name" , "What is your name?")

game_over = turtle.Turtle()
game_over.hideturtle()

#functions 
def go_up():
	if head.direction != "down":
		head.direction = "up"
def go_down():
	if head.direction != "up":
		head.direction = "down"
def go_left():
	if head.direction != "right":
		head.direction = "left"
def go_right():
	if head.direction != "left":
		head.direction = "right"
	
	
def move():
	if head.direction == "up":
		y = head.ycor()
		head.sety(y+20)
	if head.direction == "down":
		y = head.ycor()
		head.sety(y-20)
	if head.direction == "left":
		x = head.xcor()
		head.setx(x-20)
	if head.direction == "right":
		x = head.xcor()
		head.setx(x+20)
		

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("apple.gif")
food.penup()
food.goto(0,100)

#make snake grow
segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier",24,"normal"))

#keyboard bindings
wn.listen()
wn.onkey(go_up,"Up")
wn.onkey(go_down,"Down")
wn.onkey(go_left,"Left")
wn.onkey(go_right,"Right")

#main game loop
while True:
	wn.update()
	#check for collision with the food
	if head.distance(food) < 20:
		#move food to random point
		winsound.PlaySound("chomp", winsound.SND_ASYNC | winsound.SND_ALIAS) 
		x = random.randint(-290,290)
		y = random.randint(-290,290)
		food.goto(x,y)
		
		#add a segment
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color("grey")
		new_segment.penup()
		#put things into list "segments"
		segments.append(new_segment)
		
		#shorten the delay
		delay -= 0.001
		
		#increase the score
		score+=10
		
		#check the high score
		if score > high_score:
			high_score = score
			print(name,"set a new high score of", high_score,"!")
		pen.clear()
		pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier",24,"normal"))
			
		
	#move the end segments first in reverse order
	for index in range(len(segments)-1, 0, -1):
		x = segments[index -1].xcor()
		y = segments[index -1].ycor()
		segments[index].goto(x,y)
	#move segment 0 to where the head is
	if len(segments) > 0:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x,y)
	
	move()

	#Check for collision with body segments
	for segment in segments:
		if segment.distance(head) < 20:
			time.sleep(1)
			head.goto(0,0)
			head.direction = "stop"
			for segment in segments:
				segment.goto(1000,1000)
			segments.clear()
			#name = turtle.textinput("Enter your name" , "What is your name?")
			#reset the score
			score = 0
			
			#reset the delay
			delay = 0.1
			
			pen.clear()
			pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier",24,"normal"))	
	time.sleep(delay)
	
	#Check for collision with borders
	if (head.xcor()) > 300 or (head.xcor())< -290 or (head.ycor()) > 300 or (head.ycor())< -300:
		pen.clear()
		pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier",24,"normal"))
		game_over.penup()
		game_over.goto(0,0)
		game_over.pendown()
		game_over.speed("fastest")
		game_over.pencolor("white")
		s1 = ("Game Over")
		
		game_over.write(s1, align="center", font=("Calibri", 60))
		game_over.penup()
		game_over.goto(0,-100)
		game_over.pendown()
		s2 = name+("'s score = ") + str(score)
		game_over.write(s2, align="center", font=("Calibri", 60))
		time.sleep(3)
		game_over.clear()
		time.sleep(1)
		head.goto(0,0)
		head.direction = "stop"
		for segment in segments:
			segment.goto(1000,1000)
		segments.clear()
		#reset the score
		score = 0
		
		#reset the delay
		delay = 0.1
	

	
#keep window open
wn.mainloop()

