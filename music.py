import time
import math
import pygame
pygame.mixer.init()

windowSize = [400,300]
screen =pygame.display.set_mode(windowSize)

cat = pygame.image.load('1.png')
tang = pygame.image.load('2.png')
screen.blit(cat,(0,0))
screen.blit(tang,(100,200))
done = False
while not done:
      keys = pygame.key.get_pressed()

      if keys[pygame.K_a]:
            pygame.mixer.music.load('p.mp3')
            pygame.mixer.music.play()
      if keys[pygame.K_b]:
            pygame.mixer.music.load('q.mp3')
            pygame.mixer.music.play()
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  done =True
      pygame.display.flip()
pygame.quit()
