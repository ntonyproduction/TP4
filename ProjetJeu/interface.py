
from tkinter import *
from tkinter.filedialog import *
from gestion_personnages import GestionPersonnages


class Interface(Frame):
    """
    Classe héritant d'un Frame de TKInter et permetant d'afficher et de gérer l'interface graphique.
    """
    gp = GestionPersonnages()


    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Personnages : Un exemple d'héritage et de polymorphisme")

    fenetre1 = Tk()


    menu_fichier = Menu(fenetre1)
    fenetre1.config(menu=menu_fichier)

    subMenu1 = Menu(menu_fichier)
    menu_fichier.add_cascade(label="Fichier", menu=subMenu1)
    subMenu1.add_command(label="Ouvrir...", command=gp.gestion_ouvrir)
    subMenu1.add_command(label="Enregistrer", command=gp.gestion_enregistrer)
    subMenu1.add_command(label="Enregistrer Sous...", command=gp.gestion_enregistrer_sous)
    subMenu1.add_command(label="Fermer", command=gp.gestion_fermer)
    subMenu1.add_command(label="Quitter", command=fenetre1.quit)

    texte1 = Label(fenetre1, text="La fenêtre principal se tient ici.", fg="red")
    texte1.pack(side=LEFT)

    bouton1 = Button(fenetre1, text="Créer un sorcier", width=15, command=gp.gestion_creer_sorcier)
    bouton1.pack(side=TOP)

    bouton2 = Button(fenetre1, text="Créer un guerrier", width=15, command=gp.gestion_creer_guerrier)
    bouton2.pack(side=TOP)

    bouton3 = Button(fenetre1, text="Attaquer", width=15, command=gp.gestion_attaquer)
    bouton3.pack(side=TOP)

    bouton4 = Button(fenetre1, text="Réinitialiser l'énergie", width=15, command=gp.gestion_augmenter_energie)
    bouton4.pack(side=TOP)

    bouton5 = Button(fenetre1, text="Crier", width=15, command=gp.gestion_crier)
    bouton5.pack(side=TOP)

    fenetre1.mainloop()