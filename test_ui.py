import pygame
from pygame.locals import *

class Image:
	def __init__(self,fichier):
		self.spriteOrigin = pygame.image.load(fichier).convert_alpha() # au cas ou on a besoin de rechargr l'image
		self.sprite = pygame.image.load(fichier).convert_alpha()		
		self.x = 0
		self.y = 0
		self.z = 0
		self.width = 0
		self.height = 0
		self.setPositions()
		self.clickable = True
		self.rotation = 0 

	def setPositions(self):
		self.width = self.sprite.get_width()
		self.height = self.sprite.get_height()

	def applyRotation(self,angle):
		self.rotation += angle
		self.sprite = pygame.transform.rotate(self.spriteOrigin,self.rotation).convert_alpha()
		self.setPositions()

	def eventClickInImage(self,event):
		if (not self.clickable):
			return False
		if (self.x < event.pos[0] and self.x + self.width > event.pos[0] and self.y < event.pos[1] 
			and self.y + self.height > event.pos[1]): ## Si c'est dans le rectangle correspondant a l'image
			if (self.sprite.get_at((event.pos[0]-self.x,event.pos[1]-self.y))[3] != 0): # attention a la transparence !!
				return True
		return False

	def setOnTop(self,listImages):
		prof=0
		for img in sorted(listImages, key=lambda image: image.z,reverse=False):
			img.z=prof
			prof = prof + 1
		self.z=prof

	def draw(self,fenetre):
		fenetre.blit(self.sprite,(self.x,self.y))



def redraw(images,fenetre):
	for img in sorted(images, key=lambda image: image.z,reverse=False):
		img.draw(fenetre)
	pygame.display.flip()

def getImage(event,imagesList):
	image_click = None
	for img in sorted(imagesList, key=lambda image: image.z,reverse=False):
		if (img.eventClickInImage(event)):
			image_click = img
	return image_click

pygame.init()
list_image = list()

fenetre = pygame.display.set_mode((1280, 915))
background = Image("table.png")
background.clickable = False
list_image.append(background)

cartes = Image("TONSOFCARDS.jpg")
list_image.append(cartes)
cartes2 = Image("TONSOFCARDS.jpg")
cartes2.x=200
cartes2.z=1
cartes2.applyRotation(10)
list_image.append(cartes2)

redraw(list_image,fenetre)
continuer = True
while continuer:
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = False
		if event.type == MOUSEBUTTONDOWN and event.button == 1:
			imgclic = getImage(event,list_image)
			if (imgclic is not None) :
				imgclic.setOnTop(list_image)
		

		redraw(list_image,fenetre)	
		
