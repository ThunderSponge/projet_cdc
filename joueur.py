# -*- coding: iso-8859-15 -*-

import regles

STATUS={'Raton laveur':'Raton laveur','Trou de chouette':'Raton laveur','Chouette moisie':'Belette','Belette':'Belette',
        'Mi chouette':'Mi chouette',
        'Duc':'Bebe pelican','Bebe pelican':'Bebe pelican','Grand duc':'Pelican','Pelican':'Pelican'}

class Joueur:
    
    def __init__(self,idj,nom):
        self.idj=idj
        self.main=[]
        self.status='Mi chouette'
        self.spree=1
        self.pelicanisme=0
        self.nom=nom
        self.inGame=True
        self.passe=False
        self.joueur_actif=False

    def __str__(self):
        st=self.status
        if st in ['Pelican','Bebe pelican']:
            st+=' '+str(self.pelicanisme)+'.'+str(self.spree)
        if self.nom=='Michou':
            st=st.replace('Duc','Canard') .replace('duc','canard').replace("Mi chouette","Michou ette")  
        return 'joueur : {} (id:{}), statut: {}'.format(self.nom,self.idj,st)
        
    def get_idj(self):
        return self.idj
    
    def get_name(self):
        return self.nom
        
    #Gestion du statut
    def set_name(self,nom):
        self.nom=nom
    
    def is_inGame(self):
        return self.inGame
    
    def set_inGame(self,inGame):
        self.inGame=inGame
        
    #Gestion de la main
    def show_main(self):
        print(self.main)
        
    def get_main(self):
        return (self.main)
        
    def attributer_main(self,main):
        self.main=main
        
    #Ajouter ou enlever des cartes de sa main
    def prendre_carte(self,carte):
        self.main.ajouter_carte(carte)
        # En prévision de la morte couille
#         self.inGame=True
        
    def defausser_carte(self,pile,carte):
        if carte in self.main.get_cartes():
            pile.add_defausse(carte)
    
    def defausser_main(self,pile):
        for carte in self.main.get_cartes():
            self.defausser_carte(pile,carte)
        self.main.vider()
        
    def jouer_carte(self,pile,liste_carte):
        for carte in liste_carte:
            if carte not in self.main.get_cartes():
                print("Vous ne possedez pas une ou plusieurs de ces cartes !")
                return False
            
        coup=regles.Coup(liste_carte)
        if coup.estValide(pile):
            self.main.play(pile,liste_carte)
        else:
            return False
        
        if self.main.is_empty():
            print(self.nom+' a posé toutes ses cartes!')
            self.inGame=False
        return True
    
    # Vendu pas vendu
    def passer(self):
        self.passe=True
        
    def pas_passer(self):
        self.passe=False
        
    def is_vendu(self):
        return self.passe
    
    def activer(self,actif):
        self.joueur_actif=actif
    
    def is_actif(self):
        return self.joueur_actif
        
    #Gestion du grade
    def maj_status(self,status):
        if self.status == status or (self.status=='Pelican' and status=='Grand duc') or (self.status=='Bebe pelican' and status=='Duc') \
            or (self.status=='Belette' and status=='Chouette moisie') or (self.status=='Raton laveur' and status=='Trou de chouette'):
            self.spree+=1
        
            if ( not (self.status=='Pelican' or self.status=='Bebe pelican') and self.spree==3 or self.spree==4):
                self.spree=1
                self.status=STATUS[self.status]
                self.pelicanisme+=1
        else:
            self.spree=1
            self.pelicanisme=0
            self.status=status