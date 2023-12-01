from game.window import window
from objects.rect import Rect
import pygame


red_cube = Rect(x=100, y=250, width=50, height=50, colour=(255, 0, 0), gravity=0.5, xvel=0, yvel=0, grounded=False)
blue_cube = Rect(x=400, y=250, width=50, height=50, colour=(0, 0, 255), gravity=0.5, xvel=0, yvel=0, grounded=False)
floor = Rect(x=0, y=450, width=500, height=50, colour=(100, 150, 0), gravity=0, xvel=0, yvel=0, grounded=True)


class Main:
	def __init__(self):
		pass


running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	window.screen.fill(window.colour)

	floor.draw(screen=window.screen)
	red_cube.draw(screen=window.screen)

	pygame.display.flip()
