### Louis Cusson 111 142 104
### Anthony Gagnon
#constantes

energie_depart_defaut = 20
energie_depart_min = 1
energie_max = 100
longueur_nom_min = 3
longueur_nom_max = 30
nom= ""
energie_depart = 0
energie_courante = 0

class Personnage:

    def __init__(self, nom=nom, energie_depart=energie_depart_defaut): # constructeur tester
        nom_personnage = self.set_nom(str(nom))
        energie_courante_personnage = self.set_energie_depart(int(energie_depart))
        energie_courante_personnage = self.set_energie_courante(int(energie_depart))

        """
        Le constructeur du Personnage. Il doit initialiser le nom, l’énergie de départ et l’énergie courante. 
        À la création d’un objet personnage, l’énergie courante égale à l’énergie de départ.
        Args:
            nom (str): Le nom du personnage  
            energie_depart (int): L'énergie de départ 
        """

    def crier(self):

        """
        Méthode abstraite (sans code) utile pour l’héritage, cela forcera la classe dérivée à surcharger 
        la méthode (polymorphisme).
        """

    def attaquer(self, force_attaque):
        """
        Méthode abstraite (sans code) utile pour l’héritage, cela forcera la classe dérivée à surcharger 
        la méthode (polymorphisme).
        """

    def est_mort(self): # tester
        if self.energie_courante <= 0:
            self.energie_courante = 0
            return True
        else:
            return False

        """
        Retourne vrai lorsque l’énergie du personnage est à 0.
        Returns (bool): True si le personnage est mort, False sinon.
        """


    def valider_nom(self, nom): # tester
        if len(str(nom)) < longueur_nom_min or len(str(nom)) > longueur_nom_max:
            return False
        else:
            return True

        """
        Valide le nom du personnage. Un nom de personnage est valide lorsqu’il a la bonne longueur 
        (entre min et max) bornes incluses.
        Args:
            nom (str): Le nom à valider

        Returns (bool): True si le nom est valide, False sinon.
        """


    def valider_energie_courante(self, energie_courante): # tester
        if int(energie_courante) < 0 or int(energie_courante) > energie_max:
            return False
        else:
            return True

        """
        Valide l'énergie courante. Elle doit être positive (0 inclus) et ne doit pas dépasser energie_max.
        Args:
            energie_courante (int): L'énergie à valider.

        Returns (bool): True si l'énergie est valide, False sinon.
        """

    def valider_energie_depart(self, energie_depart): # tester
        if int(energie_depart) < energie_depart_min or int(energie_depart) > energie_max:
            return False
        else:
            return True

        """
        Valide l'énergie de départ. Elle est valide lorsqu’elle est entre energie_depart_min et 
        energie_max. (bornes incluses). 
        Args:
            energie_depart (int): L'énergie de départ 

        Returns (bool): True si l'énergie de départ est valide, False sinon.
        """

    def reset_energie(self): # tester
        self.energie_courante = self.energie_depart
        """
        Remet l’énergie courante du personnage à sa valeur de départ.
        """


    def get_energie_courante(self): #
        return self.energie_courante
        """
        Retourne l'énergie courante
        Returns (int): L'énergie courante
        """


    def set_energie_courante(self, energie_courante): # tester
        if self.valider_energie_courante(int(energie_courante)) == True:
            self.energie_courante = int(energie_courante)
            return True
        else:
            return False


        """
        Assigne l'énergie courante si elle est valide. 
        Args:
            energie_courante (int): L'énergie courante 

        Returns (bool): True si l'assignation a réussi, False sinon.
        """


    def get_nom(self): #
        return self.nom

        """
        Retourne le nom.
        Returns (str): Le nom.
        """


    def set_nom(self, nom): # tester
        if self.valider_nom(str(nom)) == True:
            self.nom = str(nom)
            return True
        else:
            return False

        """
        Assigne le nom s'il est valide. 
        Args:
            nom (str): Le nom

        Returns (bool): True si l'assignation a réussi, False sinon.
        """


    def get_energie_depart(self): #
        return self.energie_depart

        """
        Retourne l'énergie de départ.
        Returns (int): L'énergie de départ
        """


    def set_energie_depart(self, energie_depart): # tester
        if self.valider_energie_depart(int(energie_depart)) == True:
            self.energie_depart = int(energie_depart)
            return True
        else:
            return False

        """
        Assigne l'énergie de départ si elle est valide. 
        Args:
            energie_depart (int): L'énergie de départ 

        Returns (bool): True si l'assignation a réussi, False sinon.
        """


    def to_string(self): # tester
        return "Le personnage, " + str(self.nom) + ", a une énergie de " + str(self.energie_courante) + "."
        """
        Retourne une chaîne du genre : "Le personnage, nom de Personnage, a une énergie de valeur de 
        l’énergie."

        Returns (str): La chaîne représentant le guerrier. 
        """

if __name__ == "__main__":

    # méthode __init__
    tony = Personnage("Mo", energie_depart=99999)                                         # J'insère les valeurs de départ
                                                                                          # LES VARIABLES N'EXISTENT PAS PARCE QU'ELLES NE SONT PAS VALIDES
    tony = Personnage("Louis")
    assert tony.nom == "Louis"
    assert tony.energie_depart == energie_depart_defaut

    # méthode set_nom
    tony.set_nom("Anthony Gagnon")                              # Je set un nom
    assert tony.nom == "Anthony Gagnon"                         # Je vérifie si la variable fonctionne bien
    tony.set_nom("Mo")
    assert tony.nom == "Anthony Gagnon"

    # méthode set_énergie_depart
    tony.set_energie_depart(89)
    assert tony.energie_depart == 89
    tony.set_energie_depart(-4)
    assert tony.energie_depart == 89

    # méthode set_énergie_courante
    tony.set_energie_courante(60)
    assert tony.energie_courante == 60
    assert tony.set_energie_courante(60) == True
    tony.set_energie_courante(9999)
    assert tony.energie_courante == 60
    assert tony.set_energie_courante(9999) == False

    # méthode est_mort
    tony.energie_courante = -3
    assert tony.est_mort() == True
    tony.energie_courante = 10
    assert tony.est_mort() == False

    # méthode reset_energie
    tony.reset_energie()
    assert tony.energie_courante == 89

    # méthode to_string
    assert tony.to_string() == "Le personnage, " + "Anthony Gagnon" + ", a une énergie de " + "89" + "."

    # méthode valide_nom
    assert tony.valider_nom("Anthony Gagnon") == True
    assert tony.valider_nom("Mo") == False

    # méthode valider_energie_depart
    assert tony.valider_energie_depart(20) == True
    assert tony.valider_energie_depart(-20) == False

    # méthode valider_energie_courante
    assert tony.valider_energie_courante(30) == True
    assert tony.valider_energie_courante(-30) == False

    # méthode get_nom
    assert tony.get_nom() == "Anthony Gagnon"

    # méthode get_énergie_courante
    assert tony.get_energie_courante() == 89

    # méthode get_énergie_départ
    assert tony.get_energie_depart() == 89