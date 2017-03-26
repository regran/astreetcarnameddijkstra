import pygame
import numpy as np
from pygame.locals import *
from random import randint
from numpy.random import choice
from time import sleep

"""
types:
	blank = 0	lightgreen
	house = 1	brown
	store = 2	pink
	park = 3	green
	forest = 4	lime
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
gray = (96, 125, 139)


class Square(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def draw(cls, surface, x, y):
		s = pygame.Surface((squareWidth, squareWidth))
		s.fill(cls.color)
		surface.blit(s, (x, y))
	
	def getAdjacent(cls):
		x = cls.x
		y = cls.y
		return [squarelist[i-1][y+1], squarelist[x][y+1], squarelist[x+1][y+1], squarelist[x+1][y], 0, squarelist[x+1][y-1], squarelist[x][y+1], squarelist[x-1][y-1], squarelist[i][j]]
	
	 
class Border(Square):
	color = (0, 0, 0)
	type = -1
	cost = 100000
	isDestination = False
	
	def getAdjacent(cls):
		return [] 
	 
class Blank(Square):
	color = lightgreen
	type = 0
	cost = 2
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
	cost = 4
	isDestination = False

class Water(Square):
	color = blue
	type = 5
	cost = 4
	isDestination = False
	
class Road(Square):
	color = gray
	type = 6
	cost = 1
	isDestination = False
	
	roadgrid = [0 for r in range(8)]
	indices = [i for i, x in enumerate(roadgrid) if x==1]	#locations of road branch
	
	def draw (cls, surface, x, y):
		super(Road, cls).draw(surface, x, y)
		
		for index in cls.indices:
			pygame.draw.line(surface, gray, [x*squareWidth + .5*squareWidth, y*squareWidth + .5*squareWidth], [x*squareWidth + index % 3 * squareWidth/2, y*squareWidth + index/3 * height/2])

	
	

# class Person (pygame.sprite.sprite):
		# def __init__(self):
			# pygame.sprite.Sprite.__init__(self)
			# self.image.fill(0, 255, 0)
			# self.rect = self.image.get_rect()	



#randomly generates square types
#squarelist = [[randint(0,5) for x in xrange(squaresPerRow)] for y in xrange(squaresPerRow)]
#squarelist = [[randint(0,5) for i in range (squaresPerRow)] for j in range (squaresPerRow)]

#order: blank, house, store, park, forest, water
elements = [0, 1, 2, 3, 4, 5]		#square types
probblank = .9
probhouse = .01
probstore = .01
probpark = .01
probforest = .05
probwater = .02	
weights = [probblank, probhouse, probstore, probpark, probforest, probwater]	#probabilities of each square type
squarelist = [[choice(elements, p=weights) for i in range(squaresPerRow)] for j in range(squaresPerRow)]	#generate 2d array of square types
#print (squarelist)
for row in squarelist:
	print (row)

#Add border to map
squarelist = [[-1 for i in range(len(squarelist))]] + squarelist + [[-1 for i in range (len(squarelist))]]

for i in range (len(squarelist)):
	squarelist[i] = [-1] + squarelist[i] + [-1]

print (squarelist)


#replaces numerical types with actual type objects
for i in range(len(squarelist)):
	for j in range(len(squarelist[i])):
		if squarelist[i][j] == 0:
			squarelist[i][j]=(Blank(i, j))
		elif squarelist[i][j] == 1:
			squarelist[i][j]=(House(i, j))
		elif squarelist[i][j] == 2:
			squarelist[i][j]=(Store(i, j))
		elif squarelist[i][j] == 3:
			squarelist[i][j]=(Park(i, j))
		elif squarelist[i][j] == 4:
			squarelist[i][j]=(Forest(i, j))
		elif squarelist[i][j] == 5:
			squarelist[i][j]=(Water(i, j))
		elif squarelist[i][j] == 6:
			squarelist[i][j]=(Road(i, j))
		elif squarelist[i][j] == -1:
			squarelist[i][j]=(Border(i, j))
#print (squarelist)

#initialize screen
pygame.init()
screen = pygame.display.set_mode((bglength, bgwidth))
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
for i in range (1,len(squarelist)-1):
	for j in range (1, len(squarelist[i])-1):
		x = (j-1) * squareWidth
		y = (i-1) * squareWidth
	#	print (squarelist[i][j])
		squarelist[i][j].draw(background, x, y)
		#print(squarelist[i][j].adjacent)
		print (squarelist[i][j].getAdjacent())
		
	#Blit everything to the screen
screen.blit(background, (0, 0))
pygame.display.flip()

sleep(2)
	
def main():	

	#Event loop
	while 1:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
		screen.blit(background, (0, 0))
		for i in range (1,len(squarelist)-1):
			for j in range (1, len(squarelist[i])-1):
				x = (j-1) * squareWidth
				y= (i-1) * squareWidth
		#	print (squarelist[i][j])
				squarelist[i][j].draw(background, x, y)
		pygame.display.flip()

if __name__ == '__main__': main()

