from game.window import window
import pygame


class Main:
	def __init__(self):
		pass


running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	window.screen.fill(window.colour)

	pygame.display.flip()
