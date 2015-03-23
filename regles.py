# -*- coding: iso-8859-15 -*-

#Definition des regles du cul de chouettes

#Ho god why?

recouvrement={
'':[],
'nsimple':['nsimple','bout'],
'ndouble':['ndouble','bout'],
'ntriple':['ntriple','bout'],
'nquad': ['nquad','bout'],
'asimple': ['asimple','bout'],
'adouble': ['adouble','bout'],
'atriple': ['atriple','bout'],
'bout': ['cdc'],
'cdc':[]
}

class Regles:
    pass



class Coup:
    
    def __init__(self,cartes):
        self.cartes=cartes # Les cartes qui composent le coup #liste
        self.force=0       # La force du coup
        self.type=''       # Le type de coup 
        
    def estValide(self,pile):
        #########################################################################
        # Determine si un coup est un coup valide
        # On v�rifie:
        #    - Que le coup est valide
        #    - Que le coup peut recouvrir ce qui est sur la pile
        #    - Que le coup est plus fort que celui sur la pile
        #
        #########################################################################
        # Version 0.1 coups autoris�s:
        #
        #    - Normal simple, double, triple, carr� + nuts (AAAn et AAnN ok mais pas AAAAn)
        #    - 1,2,3 atouts de suite
        #    - Bout sur n'importe quoi et cul de chouette (sans echange post partie)
        #
        #########################################################################
        if not self.estUnCoup():
            return False
        if not self.estCorrect(pile):
            return False
        if not self.estPlusFort(pile):
            return False
                
        pile.set_tour_en_cours(self)
        return True
    
    def estUnCoup(self):
        # Verifie que les cartes forment bien une combinaison autoris�e
        # On va supposer que les cartes ont �t� jou�es dans l'ordre pour former un coup
        # Parce que sinon c'est p�nible [voir pour une version x.0 o� on fera comme on veut]
        
        # Dans cette fonction on determine �galement la force d'un coup
        # C'est un peu fat mama fonction quoi
        
 
        return True
    
    def estCorrect(self,pile):
        # Verifie que le coup est compatible avec ce qui est au centre
        if pile.get_tour_en_cours()=='' or self.type in recouvrement[pile.get_type_tour_en_cours()]:
            return True
        return False
        
        pass
    
    def estPlusFort(self,pile):
        # Verifie que le coup est plus fort que ce qui est au centre
        if pile.get_tour_en_cours()=='' or self.force >= pile.get_force_tour_en_cours():
            return True
        return False
    
    
    def get_force(self):
        return self.force
    
    def get_type(self):
        return self.type
    
    def __str__(self):
        return 'Coup Coup'