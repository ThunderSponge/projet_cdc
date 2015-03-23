# -*- coding: iso-8859-15 -*-

import joueur
import pile
import paquet
from operator import imod

default_settings={'Noms':['Gabriel','Théo','Michou','Sabine','Quentin']}

def getinput():
    try:
        x = input()
    except NameError as e:
        for pname, pvalue in vars(e).iteritems():
            print((pname, ": ", pvalue))
        error_string = str(e)
        x = error_string[error_string.index('\'') + 1: error_string.rfind('\'')]
    return x

class CDC:
    
    
    def __init__(self,nb_joueur=5):
        self.pile=pile.Pile()
        self.nb_joueur=nb_joueur
        self.joueurs=[]
        self.paquet=paquet.Paquet()
        self.classement=[]
        
        
        if self.nb_joueur==2:
            self.status=['Grand duc','Trou de chouette']
        elif self.nb_joueur==3:
            self.status=['Grand duc','Mi chouette','Trou de chouette']
        elif self.nb_joueur==4:
            self.status=['Grand duc','Duc','Chouette moisie','Trou de chouette']
        elif self.nb_joueur==5:
            self.status=['Grand duc','Duc','Mi chouette','Chouette moisie','Trou de chouette']
        elif self.nb_joueur==6:
            self.status=['Grand duc','Duc','Mi chouette','Mi chouette','Chouette moisie','Trou de chouette']
            
        i=0
        
        #Création des joueurs
        while i < nb_joueur:
            self.joueurs.append(joueur.Joueur(i,default_settings['Noms'][i]))
            i+=1
        
        #Melange et distribution en nb_joueurs tas
        self.paquet.melanger()
        mains = self.paquet.distribuer(nb_joueur)
        
        #Attribution des mains
        i=0
        for m in mains:
            self.joueurs[i].attributer_main(m)
            i+=1
        #A ce moment là, on a donc nb_joueur joueurs qui possedent chacun une main complete
            
    def clore_partie(self):
        # L'endroit où on gere les fins de manche [bout au bout, cdc raté, passe montagne, etc ]
        # V 0.1. On ajoute le dernier joueur restant au bas du classement
        j=self.get_joueur_actif() # C'est le seul joueur en jeu, donc c'est le joueur actif ! habile le mec!
        self.classement.append(j)
    
    
    
    def nouvelle_partie(self):
        # On defausse les cartes restantes en main tout le monde reviens en jeu
        for j in self.joueurs:
            j.defausser_main(self.pile)
            j.pas_passer()
            j.set_inGame(True)
            
        # On met a jour les gagnants / perdants. Le Trou de chouette deviens premier joueur
        # Nb: Au premier coup il n'y a pas de classement donc ok
        i=0
        for j in self.classement:
            j.maj_status(self.status[i])
            i+=1
            if i == self.nb_joueur:
                j.activer(True)
            else:
                j.activer(False)
        
        self.classement=[]
        
        # On remplis le paquet avec la défausse (moins les eventuelles cartes dans le cueille cerise)
        self.paquet.remplir_paquet(self.pile.get_defausse())
        self.pile.vider_defausse()
        self.paquet.melanger()
        mains = self.paquet.distribuer(self.nb_joueur)
        
        # Attribution des mains
        i=0
        for m in mains:
            self.joueurs[i].attributer_main(m)
            i+=1
            
        # reste à distribuer le cueille cerise entre les trou de chouettes et ratons
        # TODO
        
    def turnover(self):
        i=0
        for j in self.joueurs:
            if not j.is_vendu() and j.is_inGame():
                i+=1
        return i <= 1
        
    def nouveau_tour(self):
        
        # Les joueurs reviennent en jeu
        for j in self.joueurs:
            j.pas_passer()
            
        # On nettoie la pile
        self.pile.tour_suivant()
        
    def show_tour(self):
        self.pile.show_tour()
    
    def isOver(self):
        i=0
        for j in self.joueurs:
            if j.is_inGame():
                i+=1
        return i <= 1
        
        
    def set_names(self):
        print("Entrez les noms des joueurs")
        i=0
        for j in self.joueurs:
            i+=1
            print("Joueur {}".format(i))
            n=getinput()
            j.set_name(n)
            
    def get_carte(self,chaine):
        # A partir d'une chaine de string de la forme valeur-couleur;valeur-couleur; ....
        # Renvoie la liste de carte correspondante
        # Renvoie False si une des cartes n'existe pas
        ret=[]
        if chaine=='vendu':
            ret.append(self.paquet.gen_pass())
            return ret
        for c in chaine.split(';'):
            if len(c.split('-'))!=2:
                return False
            ret.append(self.paquet.get_carte(c.split('-')[0],c.split('-')[1]))
            if not ret[-1]:
                return False
        return ret
        
    def joueur_suivant(self):
        j=self.get_joueur_actif()
        i=imod(j.get_idj() + 1,self.nb_joueur)
        for j in self.joueurs:
            if i==j.get_idj():
                if j.is_vendu() or not j.is_inGame():
                    # Le joueur suivant est vendu ou a fini! On donne la main au joueur d'après
                    j.activer(False)
                    i=imod(i+1,self.nb_joueur)
                else:
                    j.activer(True)
            else:
                j.activer(False)
                
        #Deuxieme tour pour la forme
        for j in self.joueurs:
            if i==j.get_idj():
                if j.is_vendu() or not j.is_inGame():
                    # Le joueur suivant est vendu ! On donne la main au joueur d'après
                    j.activer(False)
                    i=imod(i+1,self.nb_joueur)
                else:
                    j.activer(True)
            else:
                j.activer(False)
                
        
    def get_joueur_actif(self):
        for j in self.joueurs:
            if (j.is_actif()):
                return j
        return self.joueurs[0]
    
    def jouer_carte(self,joueur,liste_carte):
        if liste_carte[0].get_valeur()=='VENDU':
            if self.pile.get_tour_en_cours()=='':
                print("On ne peut pas passer au premier coup !")
                return False
            joueur.passer()
            return True
        
        retval= joueur.jouer_carte(self.pile,liste_carte)
        
        #Si un joueur viens de poser toutes ses cartes, on l'ajoute au classement
        if not joueur.is_inGame():
            self.classer(joueur)
        return retval    
        
    def classer(self,joueur):
        # Quand un joueur fini, il prend la premiere place libre dans le classement
        # On gere pas encore le cas des mecs perdant d'office... a voir plus tard
        self.classement.append(joueur)
        
        
    def __str__(self):
        ret='Etat de la table \n\n'
        ret+='Liste des joueurs\n'
        for j in self.joueurs:
            ret+=str(j)
            ret+='\n'
            ret+=str(j.get_main())
            ret+='\n\n'
        return ret
            