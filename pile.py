# -*- coding: iso-8859-15 -*-

  
class Pile:
    def __init__(self):
        self.tour=[] #La pile du tour
        self.defausse=[] #L'ensemble des cartes jouées (pour navet'
        self.cueilleCerise=[]
        self.tour_en_cours='' #Le coup qui viens d'etre joué - contient les dernieres cartes joué et le type de coup -
        self.etat_jeu=[]      #Defini l'etat du jeu -> pattes de canard, revo, royalisme, etc. A definir
    
    def get_force_tour_en_cours(self):
        if self.tour_en_cours=='':
            return 0
        else:
            return self.tour_en_cours.get_force()    
    
    def get_type_tour_en_cours(self):
        if self.tour_en_cours=='':
            return 0
        else:
            return self.tour_en_cours.get_type()  
    
    def get_tour_en_cours(self):
        return str(self.tour_en_cours)
    
    def set_tour_en_cours(self,new_tour):
        self.tour_en_cours=new_tour
    
    def get_defausse(self):
        return self.defausse
    
    def vider_defausse(self):
        self.defausse=[]
    
    def add_defausse(self,carte):
        self.defausse.append(carte)
        
    def get_cueilleCerise(self):
        return self.cueilleCerise
    
    def vider_cueilleCerise(self):
        self.cueilleCerise=[]
        
    def show_tour(self):
        ret='Cartes jouées pendant ce tour:\n'
        for c in self.tour:
            ret+=str(c)+' -> '
        print(ret)
            
    
    def add_tour(self,carte):
        self.tour.append(carte)
        
    def tour_suivant(self):
        for c in self.tour:
            self.defausse.append(c)
        self.tour=[]
        self.tour_en_cours=''
    