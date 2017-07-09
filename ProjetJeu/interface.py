
from tkinter import *
from tkinter.filedialog import *
#from gestion_personnages import GestionPersonnages


class Interface(Frame):
    """
    Classe héritant d'un Frame de TKInter et permetant d'afficher et de gérer l'interface graphique.
    """
    #gp = GestionPersonnages()

    fenetre1 = Tk()

    menu_fichier = Menu(fenetre1)
    fenetre1.config(menu=menu_fichier)

    subMenu1 = Menu(menu_fichier)
    menu_fichier.add_cascade(label="Fichier", menu=subMenu1)
    subMenu1.add_command(label="Ouvrir...", command=print("ouvrir..."))
    subMenu1.add_command(label="Enregistrer", command=print("enregistrer"))
    subMenu1.add_command(label="Enregistrer Sous...", command=print("enregistrer sous..."))
    subMenu1.add_command(label="Fermer", command="fermer")
    subMenu1.add_command(label="Quitter", command=fenetre1.quit)

    #def __init__(self, parent):
    #    Frame.__init__(self, parent)
    #    self.parent = parent
    #    self.initUI()

    #def initUI(self):
    #    self.parent.title("Personnages : Un exemple d'héritage et de polymorphisme")

allo = Interface()