import pygame


class Rect:
	def __init__(self, x, y, width, height, colour, gravity, yvel, xvel, grounded):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.colour = colour
		self.gravity = gravity
		self.yvel = yvel
		self.xvel = xvel
		self.grounded = grounded
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


	def draw(self, screen):
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
		pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))
