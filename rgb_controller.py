#!/usr/bin/python

import serial
import pygame,sys
from pygame.locals import *

s = serial.Serial("/dev/ttyACM0")

pygame.init()

def main():
	#Set up Window
	screen = pygame.display.set_mode((500,400),0,32)
	pygame.display.set_caption('drawing')
	white = (255,0,0)


	while(True):
		l = s.readline()
		x = l.rstrip().split(",")
		try:
			rgb = [ int(val) for val in x]
			screen.fill(rgb)
			pygame.display.flip()
		except ValueError:
			continue
		print(rgb)
		
	
	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.update()


		

main()

#rgb = []
#print(x)
#for val in x:
#rgb.append(int(val))
#print("Output=",rgb)

