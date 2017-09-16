import pygame
pygame.init()

def move(image1,image2):
	global count
	if count<5:
		image = image1
	elif count >=5:
		image = image2
	
	if count >=10:
		count = 0
	else:
		count+=1
	return image

windowSize = [400,300]
screen = pygame.display.set_mode(windowSize)
clock = pygame.time.Clock()

standing = pygame.image.load('7.png')

down1 = pygame.image.load('8.png')
down2 = pygame.image.load('9.png')

up1 = pygame.image.load('9.png')
up2 = pygame.image.load('8.png')

white = pygame.color.Color('#FFFFFF')

count = 0
x= 0
y =0

done = False
while not done:
	screen.fill(white)
	keys = pygame.key.get_pressed()
	
	#player movement
	if keys[pygame.K_s]:
		image = move(down1,down2)
		y+=1
	elif keys[pygame.K_w]:
		image = move(up2,up1)
		y-=1
	else:
		image = standing

	screen.blit(image,(x,y))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	pygame.display.flip()
	clock.tick(32)
pygame.quit()
