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
		self.setSize()
		self.clickable = True
		self.rotation = 0 

	def setSize(self):
		self.width = self.sprite.get_width()
		self.height = self.sprite.get_height()

	def setPosition(self,x,y,z):
		self.x=x
		self.y=y
		self.z=z

	def applyRotation(self,angle):
		self.rotation += angle
		self.sprite = pygame.transform.rotate(self.spriteOrigin,self.rotation).convert_alpha()
		self.setSize()

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

class Carte(Image):
	def __init__(self,hauteur,couleur):
		Image.__init__(self,"cartes/"+str(hauteur)+str(couleur)+".jpg")
		self.valeur = hauteur
		self.couleur = couleur

def redraw(images,main,fenetre):
	for img in sorted(images, key=lambda image: image.z,reverse=False):
		img.draw(fenetre)
	displayHand(main,fenetre)
	pygame.display.flip()

def getImage(event,imagesList):
	image_click = None
	for img in sorted(imagesList, key=lambda image: image.z,reverse=False):
		if (img.eventClickInImage(event)):
			image_click = img
	return image_click

def getListeCartes():
	liste_cartes = list()
	for valeur in ("as","deux","trois","quatre","cinq","six","sept","huit","neuf","dix","valet","cavalier","dame","roi"):
		for couleur in ("coeur","pique","carreau","trefle"):
			liste_cartes.append(Carte(valeur,couleur))
	return liste_cartes


def displayHand(jeu,fenetre):
	xStart = 400
	yStart = 600
	zStart = 1
	for cartes in jeu:
		cartes.setPosition(xStart,yStart,xStart)
		cartes.draw(fenetre)
		xStart+=30
		zStart+=1


pygame.init()
list_image = list()

fenetre = pygame.display.set_mode((1280, 915))
background = Image("table.png")
background.clickable = False
list_image.append(background)

#cartes = Image("TONSOFCARDS.jpg")
#list_image.append(cartes)
#cartes2 = Image("TONSOFCARDS.jpg")
#cartes2.x=200
#cartes2.z=1
#cartes2.applyRotation(10)
#list_image.append(cartes2)

cartes = getListeCartes()
main = list()
for i in (1,5,15,47,28,35):
	main.append(cartes[i])




redraw(list_image,main,fenetre)
continuer = True
while continuer:
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = False
		if event.type == MOUSEBUTTONDOWN and event.button == 1:
			imgclic = getImage(event,list_image)
			if (imgclic is not None) :
				imgclic.setOnTop(list_image)
		
		redraw(list_image,main,fenetre)	
		
