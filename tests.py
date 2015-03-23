# -*- coding: iso-8859-15 -*-
from CDC import CDC
from CDC import getinput

n=CDC()
# n.set_names()

print("on lance une nouvelle partie")
n.nouvelle_partie()

print (n)

while 1:
    
    
    joueur=n.get_joueur_actif()
    
    n.show_tour()
    
    # Choisir et jouer une carte
    print(joueur)
    joueur.show_main()
    print("Entrez votre coup : ")
    c=getinput()
    carte=n.get_carte(c)
    while not carte:
        print("Entrez un nom de carte valide")
        c=getinput()
        carte=n.get_carte(c)
    
    while not n.jouer_carte(joueur,carte):
        joueur.show_main()
        print("Entrez votre coup : ")
        c=getinput()
        carte=n.get_carte(c)
        while not carte:
            print("Entrez un nom de carte valide")
            c=getinput()
            carte=n.get_carte(c)
            
    # Passer au joueur suivant
    n.joueur_suivant()
    
    if n.turnover():
        print('on passe au tour suivant\n')
        n.nouveau_tour()
    
    if n.isOver():
        print("La mene est fini, on passe a la suivante\n")
        # Clore partie ça va etre l'endroit où on regler les trucs relous de fin de partie, 
        # Les derniers d'office, etc...
        n.clore_partie()
        
        n.nouvelle_partie()
        print(n)

print(n)