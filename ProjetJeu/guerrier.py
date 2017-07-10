#constantes

import math
from personnage import Personnage

force_defaut = 20
force_max = 80
perte_force_defaut = 2
gain_force_defaut = 10
force = 0


class Guerrier(Personnage):  ###ajout qui fait en sorte que la classe Guerrier herite de la classe Personnage

    def __init__(self, nom, energie_depart, energie, force=force_defaut): # tester
        Personnage.__init__(self, nom, energie_depart) ###Vient chercher les noms et énergie de départ de classe person
        self.energie=int(energie)
        force_guerrier = self.set_force(int(force))

        """
        Le constructeur du Guerrier. Il doit initialiser le nom, l’énergie de départ, l’énergie courante et la force. 
        NB : pensez à optimiser votre code et utiliser le constructeur de la classe parente.
        Args:
            nom (str): Le nom du guerrier 
            energie_depart (int): L'énergie de départ du guerrier 
            energie (int): L'énergie courante du guerrier 
            force (int): La force du guerrier 
        """


    def to_string(self): # tester
        return "Le guerrier, " + str(self.nom) + ", a une énergie de " + str(self.energie) + " et une force de " + str(self.force) + "."
        """
        Retourne une chaîne du genre : "Le guerrier, nom de Personnage, a une énergie de valeur de 
        l’énergie et une force de valeur de la force."
 
        Returns (str): La chaîne représentant le guerrier. 
        """


    def valider_force(self, force): # tester
        if int(force) > 0 and int(force) <= force_max:
            return True
        else:
            return False

        """
        Valide si la force en paramètre est valide (entre 0 et force_max inclusivement).
        Args:
            force (int): La force à valider 

        Returns (bool): True si la force est valide, False sinon
        """

    def crier(self): # tester
        return "Vous allez goûter à la puissance de mon épée!"
        """
        Retourne le cri du guerrier : "Vous allez goûter à la puissance de mon épée!"
        Returns (str): Le cri du guerrier
        """


    def attaquer(self, force_attaque): # tester
        if self.energie < int(force_attaque):
            self.energie = 0
            self.force = 0
        else:
            self.energie -= int(force_attaque)
            self.force = max(self.force - perte_force_defaut, 0)
        """
        Lorsqu’un guerrier se fait attaquer, son énergie est diminuée de la force de l’attaque.  
        Si la force de l’attaque est plus grande que son énergie, l’énergie du guerrier devient 0 (il meurt).
        Lors d’une attaque, la force du guerrier est aussi modifiée.  Elle est diminuée, à chaque attaque, 
        de la valeur de perte_force_defaut jusqu’à concurrence de 0.  Si le guerrier meurt pendant l’attaque, 
        sa force est aussi mise à 0.
        Args:
            force_attaque (int): La force de l'attaque 
        """

    def reset_energie(self): # tester
        self.energie = self.energie_depart
        self.force = min(self.force + gain_force_defaut, force_max)

        """
        Permet de remettre l’énergie courante du guerrier à sa valeur de départ (héritage) et 
        augmente sa force (la valeur de force) par la valeur de gain_force_defaut jusqu’à concurrence de 
        la force maximale sans jamais la dépasser.       
        """

    def get_force(self):  ##méthode get force
        return self.force


    def set_force(self,force):
        if self.valider_force(int(force)) == True:
            self.force = int(force)
            return True
        else:
            return False



## Test Unitaire ##
if __name__ == "__main__":

    ##méthode __init___
    baltazar = Guerrier("baltazar",40,20, 99999)
                                                    # LA VARIABLE FORCE N'EXISTE PAS PUISQU'ELLE N'EST PAS VALIDE

    baltazar = Guerrier("baltazar",40,20,30) #construit un nom
    assert baltazar.nom == "baltazar" #test si le nom du guerrier est bien le nom assigné
    assert baltazar.energie_depart == 40 #test si l'énergie de depart est de 40
    assert baltazar.energie == 20 #test si l'énergie est de 20
    assert baltazar.force == 30 #test la force du guerrier

    #méthode attaquer

    baltazar.attaquer(2) ##assigne une valeur de l'attque de 2
    assert baltazar.energie == 18 ##vérifie si la valeur de l'énergie est diminuer de l'attaque
    assert baltazar.force == 28 ## on regarde si la force à diminuer après l'attaque
    baltazar.attaquer(40)   ## assigne une valeur de 40
    assert baltazar.energie == 0 ##valide si l'energie du guerrier est de 0
    assert baltazar.force == 0 ## test si la force est à rendu à 0

    #méthode reset energie
    baltazar.reset_energie() ##on reset l'énergie du guerrier
    assert baltazar.energie == 40 ##on test si l'énergie a été resetté
    assert baltazar.force == 10 ## on test si la force à été resetté

    ##méthode to string
    baltazar.to_string()== "Le guerrier, "+"baltazar" + ", a une énergie de "+"40" + " et une force de "+"10"+"."

    ## méthode valider force
    assert baltazar.valider_force(30) == True
    assert baltazar.valider_force(100) == False

    ##méthode crier
    assert baltazar.crier() == "Vous allez goûter à la puissance de mon épée!"

    # méthode get_force
    assert baltazar.get_force() == 10

    #méthode set_force
    assert baltazar.set_force(30) == True
    assert baltazar.force == 30





