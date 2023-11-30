import pygame


class Window:
	def __init__(self):
		self.width = 500
		self.height = 500
		self.colour = 255, 255, 255
		self.screen = pygame.display.set_mode((self.width, self.height))


window = Window()
