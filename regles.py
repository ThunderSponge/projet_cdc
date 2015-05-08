# -*- coding: iso-8859-15 -*-


from textwrap import wrap

#Definition des regles du cul de chouettes

#Ho god why?

recouvrement={
'':[''],
'nsimple':['nsimple','bout'],
'ndouble':['ndouble','bout'],
'ntriple':['ntriple','bout'],
'nquad': ['nquad','bout'],
'asimple': ['asimple','bout'],
'adouble': ['adouble','bout'],
'atriple': ['atriple','bout'],
'bout': ['cdc'],
'Excuse': ['cdcb'],
'cdc':[],
'cdcb':['49'],
'69':['69','c69','bout'],
'c69':['69','c69','bout'], #contre coup du pervers -> c'est plus facile
'passesirop':['passesirop','bout']
}

coup_double={
'69':['6','9']
}

coup_triple={


}

coup_quadruple={
'royalisme':['11','12','13','14'],
'pmc':['7','8','8','10']

}
# Donne la liste des permutations possibles pour un mot donné
# Le mot est la liste des lettres !
# ex: ['1','2','3'] -> [  ['2','1','3'], .. '312', '231', '132', '123', '321']
def permutations(lettres):
    x,n=0,[]

    for t in lettres:
        n.append(lettres.count(t))

    trav=lettres

    while x<=len(lettres)-2: #nbre de lettres du mot
        sol=[]
        for i in range(0,len(lettres),1):
            for li in trav:
                p=li+lettres[i]
                pu=p.count(lettres[i])
                if pu<=n[i]:
                    sol.append(li+lettres[i])
        trav=list(set(sol))
        x+=1

    ret=[]
    for l in sol:
        ret.append(wrap(l,1))
    return ret


def seSuivent(liste):
    ####
    # Fonction qui determine si les valeurs de carte se suivent
  # /!!\ Attention, pour le moment ordre strict du 3 -> 4 ... -> As -> 2, pas de boucles
    ####
    nl=[]
    for c in liste:
        nl.append(c.get_real_valeur())
    nl.sort()
    pred=-1
    for v in nl:
        if pred==-1 or v==pred+1:
            pred=v
            pass
        else:
            return False
    return True


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
        # On vérifie:
        #    - Que le coup est valide
        #    - Que le coup peut recouvrir ce qui est sur la pile
        #    - Que le coup est plus fort que celui sur la pile
        #
        #########################################################################
        # Version 0.1 coups autorisés:
        #
        #    - Normal simple, double, triple, carré // Pas de nuts !
        #    - 1,2,3 atouts de suite
        #    - Bout sur n'importe quoi et cul de chouette (sans echange post partie)
        #    - Cul de chouette banjo et contre cul de chouette banjo (sans echange post partie)
        #
        #########################################################################
        if not self.estUnCoup():
            return False
        if not self.estCorrect(pile):
            return False
        if not self.estPlusFort(pile):
            return False

        if (self.cartes[0].get_valeur() != 'VENDU'):
            pile.set_tour_en_cours(self)
        return True

    def estUnCoup(self):
        # Verifie que les cartes forment bien une combinaison autorisée
        # On va supposer que les cartes ont été jouées dans l'ordre pour former un coup
        # Parce que sinon c'est pénible [voir pour une version x.0 où on fera comme on veut]

        # Dans cette fonction on determine également la force d'un coup
        # C'est un peu fat mama fonction quoi

        ###########################################################################
        #
        # Cas des coups à une carte
        #
        ###########################################################################
        if (len(self.cartes)==1):
            return self.coupMono()
        elif (len(self.cartes)==2):
            return self.coupDouble()
        elif (len(self.cartes)==3):
            return self.coupTriple()
        elif (len(self.cartes)==4):
            return self.coupQuadruple()
        elif (len(self.cartes)==7):
            return self.coupSeptuple()

        print("Ce coup n'existe pas ou n'est pas encore implemente")

        return False

    def estCorrect(self,pile):
        # Verifie que le coup est compatible avec ce qui est au centre
        if self.type=='VENDU':
            return True
        if pile.get_tour_en_cours()=='' or self.type in recouvrement[pile.get_type_tour_en_cours()]:
            return True

        print("On ne peux pas jouer un {} sur un {}".format(self.type,pile.get_type_tour_en_cours()))
        return False

    def estPlusFort(self,pile):
        # Verifie que le coup est plus fort que ce qui est au centre
        if self.type=='VENDU':
            return True
        if pile.get_tour_en_cours()=='' or self.force >= pile.get_force_tour_en_cours():
            return True

        print("Votre coup (force: {}) est trop faible par rapport à celui sur la pile (force: {})".format(self.force,pile.get_force_tour_en_cours()))
        return False


########################################################################################################################################################
#
#
    ###########################################################################
    #
    # Determination du type et de la force d'un coup reparti par nombre de carte dans le coup
    #
    ###########################################################################

    # Les coups contenant une seule carte
    def coupMono(self):
        if (self.cartes[0].get_valeur() == 'VENDU'):
            self.type='VENDU'
            return True
        else:
            if self.cartes[0].is_bout():
                if self.cartes[0].get_valeur()=='E':
                    self.type='Excuse'
                else:
                    self.type='bout'
                self.force=99
            elif self.cartes[0].is_normale():
                self.type='nsimple'
                self.force=self.cartes[0].get_real_valeur()
            elif self.cartes[0].is_atout():
                self.type='asimple'
                self.force=self.cartes[0].get_real_valeur()
            return True
        return False

    # Les coups contenant deux cartes
    def coupDouble(self):

        c1=self.cartes[0]
        c2=self.cartes[1]

        # Le cul de chouette
        if c1.is_bout():
            if c2.is_bout():
                # On verra plus tard pour les culs de chouette avec des pates de canard
                if 'E' not in (c1.get_valeur(),c2.get_valeur()):
                    self.type='cdcb'
                else:
                    self.type='cdc'
                self.force=99
                return True
            # Tout autre coup contenant un bout est forcement incorrect
            return False

        if c1.is_normale():
            if c2.is_normale():
                # Double
                print("DEBUG - coup double")
                if c1.get_real_valeur() == c2.get_real_valeur():
                    self.type='ndouble'
                    self.force=c1.get_real_valeur()
                    return True

        if c1.is_atout(): # Normalement c'est le cas hein, mais bon....
            if c2.is_atout():
                if seSuivent(self.cartes):
                # Deux atouts à la suite
                    self.type='adouble'
                    self.force=max(c1.get_real_valeur(),c2.get_real_valeur())
                    return True
                elif (c1.get_valeur(),c2.get_valeur()) in permutation('4','9'):
                # Contre cul de chouette banjo
                    self.type='49'
                    self.force=99
                    return True

    # Coup du pervers
        if [c1.get_valeur(),c2.get_valeur()] in permutation(['6','9']):
            if c1.is_atout() or c2.is_atout():
                self.type='c69' # on verifiera plus tard si le c69 est bien joué sur quelque chose
            else:
                self.type='69'
            self.force=99
            return True
    
        return False

    # Les coups contenant trois cartes
    def coupTriple(self):
        c1=self.cartes[0]
        c2=self.cartes[1]
        c3=self.cartes[2]

        if c1.is_bout() or c2.is_bout() or c3.is_bout():
            return False

        if c1.is_normale() and c2.is_normale() and c3.is_normale():
            if c1.get_real_valeur() == c2.get_real_valeur() and c1.get_real_valeur() == c3.get_real_valeur():
                self.type='ntriple'
                self.force=c1.get_real_valeur()
                return True
        if c1.is_atout() and c2.is_atout() and c3.is_atout():
            if seSuivent(self.cartes):
                self.type='atriple'
                self.force=max(c1.get_real_valeur(),c2.get_real_valeur(),c3.get_real_valeur())
                return True

        return False

    # Les coups contenant quatre cartes
    def coupQuadruple(self):
        c1=self.cartes[0]
        c2=self.cartes[1]
        c3=self.cartes[2]
        c4=self.cartes[3]

        if c1.is_normale() and c2.is_normale() and c3.is_normale() and c4.is_normale():
            if c1.get_real_valeur() == c2.get_real_valeur() and c1.get_real_valeur() == c3.get_real_valeur() and c1.get_real_valeur() == c4.get_real_valeur():
                self.type='nquad'
                self.force=c1.get_real_valeur()
                return True

        return False

    def coupQuintuple(self):
        c1=self.cartes[0]
        c2=self.cartes[1]
        c3=self.cartes[2]
        c4=self.cartes[3]
        c5=self.cartes[4]
        return False

    def coupSextuple(self):
        c1=self.cartes[0]
        c2=self.cartes[1]
        c3=self.cartes[2]
        c4=self.cartes[3]
        c5=self.cartes[4]
        c6=self.cartes[5]
        return False

  # Les coups spéciaux à sept cartes
    def coupSeptuple(self):
    # Le passe sirop
        c1=self.cartes[0]
        c2=self.cartes[1]
        c3=self.cartes[2]
        c4=self.cartes[3]
        c5=self.cartes[4]
        c6=self.cartes[5]
        c7=self.cartes[6]

        psirop=True
        for c in c1,c2,c3,c4,c5,c6,c7:
            psirop=psirop and c.is_normale()
        if psirop and seSuivent([c1,c2,c3,c4,c5,c6,c7]):
            self.type='passesirop'
            self.force=99
            for c in c1,c2,c3,c4,c5,c6,c7:
                self.force=min(self.force,c.get_real_valeur()) # point de regle: la force d'un passe sirop est celle de sa plus petite carte
            return True
    
        # Reste à verifier
    
        return False

#
#
########################################################################################################################################################


    ###########################################################################
    #
    # Accesseurs et divers
    #
    ###########################################################################

    def get_force(self):
        return self.force

    def get_type(self):
        return self.type

    def __str__(self):
        return 'Coup Coup'
