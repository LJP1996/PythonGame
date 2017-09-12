import random
import pygame
pygame.mixer.init()
pygame.mixer.music.load('p.mp3')
pygame.mixer.music.play(1)
# Window setup
size = [400,300]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# player position
x = size[0]//2
y  = size[1]//2
# ball position
ballX = random.randrange(0,size[0])
ballY = random.randrange(0,size[1])

# Goal position
goalX = size[0] //2 -10
goalY = size[1] //2 -10
goalW = 20
goalH = 20

#points
points =0

#colors
red = pygame.color.Color('#FF8080')
blue = pygame.color.Color('#8080FF')
white = pygame.color.Color('#FFFFFF')
black = pygame.color.Color('#000000')

def checkoffScreenX(x):
	if x>size[0]:
		x =0
	elif x<0:
		x=size[0]
	return x
def checkoffScreenY(y):
	if y>size[1]:
		y =0
	elif y<0:
		y=size[1]
	return y
def checkoffching():
	global x
	global y
	global ballX
	global ballY
	
	if -10< y - ballY<10 and -10< x - ballX< 10:
		pygame.draw.circle(screen,white,[x,y],15)
		
		xDiff = x-ballX
		yDiff = y-ballY
		#check if ball is on edge of screen
		if ballX ==0:
			xDiff -=5
		elif ballX == size[0]:
			xDiff += 5
		if ballY ==0:
			yDiff -=5
		elif ballY == size[1]:
			yDiff += 5
		
		#move ball and player
		x +=xDiff *3
		ballX -= xDiff*3
		
		y +=yDiff *3
		ballY -= yDiff*3
		
		
# game loop
done = False
#get time 
timeStart = pygame.time.get_ticks()

while not done:
	screen.fill(black)
	# draw goal 
	pygame.draw.rect(screen,white,(goalX,goalY,goalW,goalH))
	#Check ball in the goal
	if goalX<=ballX<=goalX+goalH and	goalY<=ballY<=goalY+goalH:
		points +=1
		ballX = random.randrange(0,size[0])
		ballY = random.randrange(0,size[1])
	keys = pygame.key.get_pressed()
	
	# player movement
	if keys[pygame.K_w]:
		y -= 1
	if keys[pygame.K_s]:
		y += 1	
	if keys[pygame.K_a]:
		x -= 1
	if keys[pygame.K_d]:
		x += 1	
	# Check off screen
	x = checkoffScreenX(x)
	y = checkoffScreenY(y)
	ballX = checkoffScreenX(ballX)
	ballY = checkoffScreenY(ballY)
	
	#Check ball touchinng player
	checkoffching()
	#Draw points
	for point in range(points):
		pointX = 0 +point*5
		pygame.draw.rect(screen,white,(pointX,3,4,7))
	#draw player
	pygame.draw.circle(screen,red,[x,y],6)
	#draw ball
	pygame.draw.circle(screen,blue,[ballX,ballY],6)
	pygame.display.flip()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	clock.tick(200)
	# check elapased time
	timeNow = pygame.time.get_ticks()
	if timeNow -timeStart  >=60000:
		done = True
pygame.quit()
print("Toal points:"+str(points))
