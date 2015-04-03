# -*- coding: iso-8859-15 -*-

COULEUR=['pique','coeur','carreau','trefle','atout']
VALEUR=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','N','n','E'] #Nuts, Excuse
NB_ATOUTS=21
NB_NORMALES=14

class Carte:
    def __init__(self,valeur='1',couleur='pique',isBout=False):
        self.valeur=str(valeur)
        self.couleur=couleur
        self.isBout =isBout
    
    def set_val(self,valeur):
        if str(valeur) in VALEUR:
            self.valeur=str(valeur)
    
    def set_couleur(self,couleur):
        if couleur in COULEUR:
            self.couleur=couleur
            
    def set_isBout(self,isBout):
        self.isBout=isBout
    
    def is_bout(self):
        return self.isBout
        
    def get_valeur(self):
        return self.valeur
    
    def get_real_valeur(self):
        if self.valeur=='1' and self.couleur != 'atout':
            return 15
        if self.valeur=='2' and self.couleur != 'atout':
            return 16
        
        if self.valeur=='1' or self.valeur=='21' or self.valeur=='E':
            return 99
        
        if self.valeur=='n' or self.valeur=='N':
            # Actuellement, tous les nuts sont des valets
            return 11
        
        return int(self.valeur)
        
    def is_normale(self):
        return self.couleur in ['pique','coeur','carreau','trefle','nuts']
    
    def is_atout(self):
        return self.couleur in ['atout']
            
    def get_couleur(self):
        return self.couleur
            
    def __str__(self):
        
        if self.valeur == 'E':
            return 'Excuse *'
        elif self.valeur =='n':
            return 'nuts'
        elif self.valeur =='N':
            return 'Nuts'
        
        b=' *' if self.isBout else ''
        d=' de ' if self.couleur!='atout' else ' d\''
        v=self.valeur
        if self.couleur != 'atout':
            if self.valeur=='11':
                v='Valet'
            elif self.valeur=='12':
                v='Cavalier'
            elif self.valeur=='13':
                v='Dame'
            elif self.valeur=='14':
                v='Roi'
            elif self.valeur=='1':
                v='As'
        
        return v + d + self.couleur + b