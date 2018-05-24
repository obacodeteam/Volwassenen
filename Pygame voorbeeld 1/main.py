import pygame, sys

#alle standaard variabelen van pygame importeren
from pygame.locals import *

#pygame opstarten
pygame.init()

#maak het scherm
screen = pygame.display.set_mode((400, 300))

#verander de titel
pygame.display.set_caption("Hello OBA!")

#stel key_repeat in
pygame.key.set_repeat(10,10)

#laad het plaatje in
oba = pygame.image.load("logo oba.jpg")

#de coordinaten voor het plaatje
oba_x = 0
oba_y = 0

#de beweegsnelheid van het plaatje
movespeed = 1

# main game loop
while True: 
	
	#input verwerken
	for event in pygame.event.get(): # pygame.event.get() geeft een lijst terug
									 # met alle input sinds de laatste keer dat je deze functie aangeroepen hebt

		if event.type == QUIT: #als het type van de event QUIT is (kruisje is aangeklikt)
			pygame.quit() #pygame afsluiten
			sys.exit() #scherm afsluiten
		
		elif event.type == KEYDOWN: #als het type van de event KEYDOWN is (er is een knop ingedrukt)
			if event.key == K_UP: #als de knop het pijltje omhoog is
				oba_y -= movespeed
			elif event.key == K_DOWN:
				oba_y += movespeed
			elif event.key == K_LEFT:
				oba_x -= movespeed
			elif event.key == K_RIGHT:
				oba_x += movespeed
	
	#tekenen
	screen.fill((0,0,0)) #vul het scherm met de kleur zwart
	screen.blit(oba, (oba_x, oba_y)) #plak het plaatje op het scherm bij de coordinaten oba_x en oba_y
	pygame.display.update() #laat het nieuwe getekende scherm op de monitor zien
