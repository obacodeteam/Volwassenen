import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400, 300))

pygame.display.set_caption("Hello OBA!")

pygame.key.set_repeat(10,10)

oba = pygame.image.load("logo oba.jpg")

oba_x = 0
oba_y = 0

movespeed = 1

while True: # main game loop
	#input handling
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_UP:
				oba_y -= movespeed
			elif event.key == K_DOWN:
				oba_y += movespeed
			elif event.key == K_LEFT:
				oba_x -= movespeed
			elif event.key == K_RIGHT:
				oba_x += movespeed
	
	#drawing
	screen.fill((0,0,0))
	screen.blit(oba, (oba_x, oba_y))
	pygame.display.update()
