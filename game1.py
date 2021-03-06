import pygame
pygame.init()

# Window setup
size = [400,300]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# player position
x = size[0]//2
y  = size[1]//2

#colors
red = pygame.color.Color('#FF8080')
blue = pygame.color.Color('#8080FF')
white = pygame.color.Color('#FFFFFF')
black = pygame.color.Color('#000000')

# game loop
done = False
while not done:
	screen.fill(black)
	keys = pygame.key.get_pressed()
	
	# player movement
	if keys[pygame.K_w]:
		y -= 1
        if keys[pygame.K_s]:
		y += 1
	#draw player
	pygame.draw.circle(screen,red,[x,y],6)
	pygame.display.flip()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	clock.tick(72)
pygame.quit()
