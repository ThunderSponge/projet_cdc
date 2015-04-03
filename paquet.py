# -*- coding: iso-8859-15 -*-

from cartes import Carte
from cartes import COULEUR,NB_ATOUTS,NB_NORMALES
from main import Main
import random
from operator import imod


class Paquet:
    def __init__(self):
        self.pioche=[]
        self.liste=[]
        for c in COULEUR:
            i=1
            if c=='atout':
                while i <= NB_ATOUTS:
                    if i==1 or i==21:
                        self.pioche.append(Carte(i,c,True))
                    else:
                        self.pioche.append(Carte(i,c,False))
                    i+=1
            else:
                while i <= NB_NORMALES:
                    self.pioche.append(Carte(i,c,False))
                    i+=1
#         self.pioche.append(Carte('n','nuts',False))
#         self.pioche.append(Carte('N','nuts',False))
        self.pioche.append(Carte('E','excuse',True))
        
        # Le conteneur de toutes les cartes
        self.liste=self.pioche
            
    def __str__(self):
        ret=''
        if not self.pioche:
            return 'Toutes les cartes ont été distribuées'
        for c in self.pioche:
            ret+=str(c)+', '
        return ret
            
    def remplir_paquet(self,cartes):
        self.pioche=cartes
    
    def melanger(self):
        random.shuffle(self.pioche)
        
    def distribuer(self,nbjoueurs=5):
        #par défaut on jouera à 5
        mains=[]
        i=0
        while i < nbjoueurs:
            mains.append(Main(i))
            i+=1
        i=0
        for c in self.pioche:
            mains[i].ajouter_carte(c)
            i=imod(i+1,nbjoueurs)
        self.pioche=[]
        return mains
    
    def get_carte(self,valeur,couleur):
        # Convertis deux string en une Carte
        for c in self.liste:
            if valeur==c.get_valeur() and couleur==c.get_couleur():
                return c
            
    def gen_pass(self):
        # Genere la carte qui fait passer quand on la joue
        # Choix d'implementation discutable
        return Carte('VENDU','VENDU',False)