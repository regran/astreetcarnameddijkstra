import pygame
import numpy as np
from pygame.locals import *
from random import randint

"""
types:
	blank = 0	lightgreen
	house = 1	brown
	store = 2	pink
	park = 3	green
	forest = 4	lightgreen
	water = 5	blue

"""


squaresPerRow = 12
bglength = squaresPerRow * 50
bgwidth = squaresPerRow * 50
squareWidth = bglength / squaresPerRow

white=(255, 255, 255)
brown=(121, 85, 72)
blue = (33, 150, 243)
green = (76, 175, 80)
lightgreen=(139, 195, 74)
lime = (205, 220, 57)
pink = (233, 30, 99)
#itemcolors=[white, brown, blue, green, lightgreen]


class Square(object):
	
	@classmethod
	def draw(cls, surface, x, y):
		s = pygame.Surface((squareWidth, squareWidth))
		s.fill(cls.color)
		surface.blit(s, (x, y))
	
	 
class Blank(Square):
	color = lightgreen
	type = 0
	cost = 1
	isDestination = False
		

class House(Square):
	color = brown
	type = 1
	cost = 10000
	isDestination = True

class Store(Square):
	color = pink
	type = 2
	cost = 10000
	isDestination = True
		

class Park(Square):
	color = green
	type = 3
	cost = 10000
	isDestination = True

class Forest(Square):
	color = lime
	type = 4
	cost = 3
	isDestination = False

class Water(Square):
	color = blue
	type = 5
	cost = 3
	isDestination = False



#randomly generates square types
#squarelist = [[randint(0,5) for x in xrange(squaresPerRow)] for y in xrange(squaresPerRow)]
squarelist = [[randint(0,5) for i in range (squaresPerRow)] for j in range (squaresPerRow)]
print (squarelist)

#replaces numerical types with actual type objects
for i in range(len(squarelist)):
	for j in range(len(squarelist[i])):
		if squarelist[i][j] == 0:
			squarelist[i][j]=(Blank())
		elif squarelist[i][j] == 1:
			squarelist[i][j]=(House())
		elif squarelist[i][j] == 2:
			squarelist[i][j]=(Store())
		elif squarelist[i][j] == 3:
			squarelist[i][j]=(Park())
		elif squarelist[i][j] == 4:
			squarelist[i][j]=(Forest())
		elif squarelist[i][j] == 5:
			squarelist[i][j]=(Water())
print (squarelist)


def main():
	#initialize screen
	pygame.init()
	screen = pygame.display.set_mode((500, 500))
	pygame.display.set_caption('Roads!')
	
	#Fill background
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((250, 250, 250))
	
	#Display some text
	font = pygame.font.Font(None, 36)
	text = font.render("There will be roads", 1, (10, 10, 10))
	textpos = text.get_rect()
	textpos.centerx = background.get_rect().centerx
	background.blit(text, textpos)
	
	#Display all the squares
	for i in range (len(squarelist)):
		for j in range (len(squarelist[i])):
			x = j * squareWidth
			y = i * squareWidth
			print (squarelist[i][j])
			squarelist[i][j].draw(background, x, y)

	#Blit everything to the screen
	screen.blit(background, (0, 0))
	pygame.display.flip()
	
	#Event loop
	while 1:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
		screen.blit(background, (0, 0))
		pygame.display.flip()

if __name__ == '__main__': main()

