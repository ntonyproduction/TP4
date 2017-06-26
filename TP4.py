def doNothing():
    print("C'est juste un test pour le drop down menu.")

def creersorcier(): ##fenetre qui demandera saisie à l'utilisateur pour le sorcier
    fenetre2 = Tk()

def creerguerrier(): ## fenetre qui demandera saisie à l'utilisateur pour le guerrier
    fenetre3 = Tk()

# Importe les classes contenues dans le module tkinter
from tkinter import *

# utilisation de la classe Tk() qui fait apparaître une fenêtre
fenetre1 = Tk()

menu_fichier = Menu(fenetre1)
fenetre1.config(menu = menu_fichier)

subMenu1 = Menu(menu_fichier)
menu_fichier.add_cascade(label = "Fichier", menu = subMenu1)
subMenu1.add_command(label = "Ouvrir...", command = doNothing)
subMenu1.add_command(label = "Enregistrer", command = doNothing)
subMenu1.add_command(label = "Enregistrer Sous...", command = doNothing)
subMenu1.add_command(label = "Fermer", command = doNothing)
subMenu1.add_command(label = "Quitter", command = fenetre1.quit)

# Création d'un objet/widget avec la classe Label()
texte1 = Label(fenetre1, text = "La fenêtre principal se tient ici.", fg = "red")
texte1.pack(side = LEFT) # Activation de la méthode pack()

# Création d'un objet/widget avec la classe Button()
bouton1 = Button(fenetre1, text = "Créer un sorcier", width = 15,command = creersorcier)
bouton1.pack(side = TOP) # Activation de la méthode pack()

bouton2 = Button(fenetre1, text = "Créer un guerrier", width = 15, command=creerguerrier)
bouton2.pack(side = TOP)

bouton3 = Button(fenetre1, text = "Attaquer", width = 15)
bouton3.pack(side = TOP)

bouton4 = Button(fenetre1, text = "Réinitialiser l'énergie", width = 15)
bouton4.pack(side = TOP)

bouton5 = Button(fenetre1, text = "Crier", width = 15)
bouton5.pack(side = TOP)

#### Votre tp c'est laid #####
# Activation de la méthode mainloop() pour garder le programme actif en permanence
fenetre1.mainloop()
