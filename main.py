# -*- coding: iso-8859-15 -*-

class Main:
    
    def __init__(self,player):
        self.player=player
        self.cartes=[]
        
    def __str__(self):
        ret=''
        for c in self.cartes:
            ret+=str(c)+', '
        return ret

    def get_cartes(self):
        return self.cartes
    
    def ajouter_carte(self,carte):
        self.cartes.append(carte)
        
    def discard(self,pile,carte):
        pile.add_defausse(carte)
        self.cartes.remove(carte)
        
    def vider(self):
        self.cartes=[]
        
    def play(self,pile,liste_carte):
        #Jouer une ou plusieur cartes
        #Chaque carte de la liste est ajoutée dans l'ordre au tour
        for c in liste_carte:
            pile.add_tour(c)
            self.cartes.remove(c)
        
    def is_empty(self):
        return self.cartes==[]