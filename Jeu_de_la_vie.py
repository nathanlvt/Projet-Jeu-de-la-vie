#######
## LE JEU DE LA VIE 
#######
# Avec et sans interface graphique (tkinter)
#######
# Auteur : Maïlane BOUCHER / Célia STEMMELIN / Etienne REMOND / Nathan LOUVET
# Classe : MPSI 1 
# Date : 17/06/2020
# Remerciement à Pierre Louis HABOURY qui a beaucoup oeuvré pour l'interface graphique.
#######

"""
Il y a deux programmes de jeu, demo_sans_interface_graphique() qui se joue dans la console et demo() qui est la version la plus aboutie avec une interface graphique. 
##
Pour éviter toutes erreurs dans le programme demo(). Il ne faut pas oublier de stopper l'animation avant de fermer la fenêtre !
##
Aller voir à la fin du programme pour jouer.
"""

#########

import numpy as np
import random as rd
from tkinter import *

#####
##### Le tableau :
#####

def tableau(k):
    """Permet de générer un tableau carré de taille k remplie de 1 et de 0 aléatoirement."""
    tab = np.zeros([k,k], np.int)
    for n in range(k):
        for p in range(k):
            tab[n][p] = rd.randint(0,1)
    return(tab)

#print(tableau(10))

#####
##### Coin du carré :
#####

def coin_haut_gauche(n, p, k, tab):
    """Compte le nombre de 1 voisin de la cellule située dans le coin en haut à gauche d'un tableau carré (tab) de taille k. n (resp. p) représente les lignes (resp. les colonnes)."""
    liste_coor = []
    compteur_voisin = 0
    liste_coor.append(tab[n][p])
    if tab[n][p + 1] == 1:
        compteur_voisin += 1
    if tab[n + 1][p] == 1:
        compteur_voisin += 1
    if tab[n + 1][p + 1] == 1:
        compteur_voisin += 1
    liste_coor.append(compteur_voisin)
    return liste_coor

def coin_haut_droit(n, p, k, tab):
    """Compte le nombre de 1 voisin de la cellule située dans le coin en haut à droite d'un tableau carré (tab) de taille k. n (resp. p) représente les lignes (resp. les colonnes)."""
    liste_coor = []
    compteur_voisin = 0
    liste_coor.append(tab[n][p])
    if tab[n][p - 1] == 1:
        compteur_voisin += 1
    if tab[n +  1][p - 1] == 1:
        compteur_voisin += 1
    if tab[n + 1 ][p] == 1:
        compteur_voisin += 1
    liste_coor.append(compteur_voisin)
    return liste_coor

def coin_bas_gauche(n, p, k, tab):
    """Compte le nombre de 1 voisin de la cellule située dans le coin en bas à gauche d'un tableau carré (tab) de taille k. n (resp. p) représente les lignes (resp. les colonnes)."""
    liste_coor = []
    compteur_voisin = 0
    liste_coor.append(tab[n][p])
    if tab[n - 1][p] == 1:
        compteur_voisin += 1
    if tab[n - 1][p + 1] == 1:
        compteur_voisin += 1
    if tab[n][p + 1] == 1:
        compteur_voisin += 1
    liste_coor.append(compteur_voisin)
    return liste_coor

def coin_bas_droit(n, p, k, tab):
    """Compte le nombre de 1 voisin de la cellule située dans le coin en bas à droit d'un tableau carré (tab) de taille k. n (resp. p) représente les lignes (resp. les colonnes)."""
    liste_coor = []
    compteur_voisin = 0
    liste_coor.append(tab[n][p])
    if tab[n - 1][p - 1] == 1:
        compteur_voisin += 1
    if tab[n - 1][p] == 1:
        compteur_voisin += 1
    if tab[n][p - 1] == 1:
        compteur_voisin += 1
    liste_coor.append(compteur_voisin)
    return liste_coor

#####
##### Les bords gauche & droit :
#####

def bord_gauche(n, p, k, tab):
    """Compte le nombre de 1 voisin des cellules situées sur le bord gauche d'un tableau carré (tab) de taille k. n (resp. p) représente les lignes (resp. les colonnes)."""
    liste_coor = []
    compteur_voisin = 0
    liste_coor.append(tab[n][p])
    if tab[n - 1][0] == 1:
        compteur_voisin += 1
    if tab[n - 1][1] == 1:
        compteur_voisin += 1
    if tab[n][1]:
        compteur_voisin += 1
    if tab[n + 1][1] == 1:
        compteur_voisin += 1
    if tab[n + 1][0] == 1:
        compteur_voisin += 1
    liste_coor.append(compteur_voisin)
    return liste_coor

def bord_droit(n, p, k, tab):
    """Compte le nombre de 1 voisin des cellules situées sur le bord droit d'un tableau carré (tab) de taille k. n (resp. p) représente les lignes (resp. les colonnes)."""
    liste_coor = []
    compteur_voisin = 0
    liste_coor.append(tab[n][p])
    if tab[n - 1][k - 1] == 1:
        compteur_voisin += 1
    if tab[n - 1][k - 2] == 1:
        compteur_voisin += 1
    if tab[n][k - 2]:
        compteur_voisin += 1
    if tab[n + 1][k - 2] == 1:
        compteur_voisin += 1
    if tab[n + 1][k - 1] == 1:
        compteur_voisin += 1
    liste_coor.append(compteur_voisin)
    return liste_coor

#####
##### Les bords haut & bas :
#####

def bord_haut(n, p, k, tab):
    """Compte le nombre de 1 voisin des cellules situées sur le bord haut d'un tableau carré (tab) de taille k. n (resp. p) représente les lignes (resp. les colonnes)."""
    liste_coor = []
    compteur_voisin = 0
    liste_coor.append(tab[n][p])
    if tab[0][p -1] == 1:
        compteur_voisin += 1
    if tab[0][p + 1] == 1:
        compteur_voisin += 1
    if tab[1][p - 1] == 1:
        compteur_voisin += 1
    if tab[1][p] == 1:
        compteur_voisin += 1
    if tab[1][p + 1] == 1:
        compteur_voisin += 1
    liste_coor.append(compteur_voisin)
    return liste_coor

def bord_bas(n, p, k, tab):
    """Compte le nombre de 1 voisin des cellules situées sur le bord bas d'un tableau carré (tab) de taille k. n (resp. p) représente les lignes (resp. les colonnes)."""
    liste_coor = []
    compteur_voisin = 0
    liste_coor.append(tab[n][p])
    if tab[k - 1][p - 1] == 1:
        compteur_voisin += 1
    if tab[k - 1][p + 1] == 1:
        compteur_voisin += 1
    if tab[k - 2][p - 1] == 1:
        compteur_voisin += 1
    if tab[k - 2][p] == 1:
        compteur_voisin += 1
    if tab[k - 2][p + 1] == 1:
        compteur_voisin += 1
    liste_coor.append(compteur_voisin)
    return liste_coor

#####
##### Le millieu :
#####

def milieu(n, p, k, tab):
    """Compte le nombre de 1 vosin des cellules situées au milieu d'un tableau carré (tab) de taille k. n (resp. p) représente les lignes (resp. les colonnes)."""
    liste_coor = []
    compteur_voisin = 0
    liste_coor.append(tab[n][p])
    if tab[n + 1][p - 1] == 1:
        compteur_voisin += 1
    if tab[n + 1][p] == 1:
        compteur_voisin += 1
    if tab[n + 1][p + 1] == 1:
        compteur_voisin += 1
    if tab[n][p - 1] == 1:
        compteur_voisin += 1
    if tab[n][p + 1] == 1:
        compteur_voisin += 1
    if tab[n -  1][p - 1] == 1:
        compteur_voisin += 1
    if tab[n - 1 ][p] == 1:
        compteur_voisin += 1
    if tab[n - 1 ][p + 1] == 1:
        compteur_voisin += 1
    liste_coor.append(compteur_voisin)
    return liste_coor

#####
##### Programme nombre de voisin :
#####

def voisins(tab, k):
    global liste_complete
    """Compte le nombre de 1 voisin des différentes cellules d'un tableau (tab) de taille k."""
    liste_complete = []
    liste_ligne = []
    compteur_voisin = 0
    for n in range(0, k):
        liste_ligne = []
        for p in range(0, k):
            if n == 0 and p == 0:                                     #coin haut gauche
                liste_ligne.append(coin_haut_gauche(n, p, k, tab))

            if n == 0 and p == (k - 1):                               #coin haut droit
                liste_ligne.append(coin_haut_droit(n, p, k,  tab))

            if n == (k - 1) and p == 0:                               #coin bas gauche
                liste_ligne.append(coin_bas_gauche(n, p, k, tab))

            if n == (k - 1) and p == (k - 1):                         #coin bas droit
                liste_ligne.append(coin_bas_droit(n, p, k, tab))

            if  (0 < n <= (k - 2)) and p == 0:                        #bord gauche
                liste_ligne.append(bord_gauche(n, p, k, tab))

            if n == 0 and (0 < p <= (k - 2)):                         #bord haut
                liste_ligne.append(bord_haut(n, p, k, tab))

            if (0 < n <= (k - 2)) and p == (k - 1):                   #bord droit
                liste_ligne.append(bord_droit(n, p, k, tab))

            if n == (k - 1) and (0 < p <= (k - 2)):                   #bord bas
                liste_ligne.append(bord_bas(n, p, k, tab))

            if (0 < n < (k - 1)) and (0 < p < (k - 1)):               #milieu
                liste_ligne.append(milieu(n, p, k, tab))
        liste_complete.append(liste_ligne)
    return liste_complete

#print(voisins(10))

#####
##### Les règles & Evolution tableau :
#####

def regles(liste_voisins, k):
    """A partir des éléments de la liste (liste_voisins), que retourne le programme 'voisins'. Ce programme retourne le tableau de taille k du jours d'après."""
    new_tab = np.zeros([k,k], np.int)
    compteur_lignes = 0
    compteur_naissances = 0
    compteur_deces = 0
    for i in liste_voisins:
        for j in range(k):
            if i[j][0] == 0:
                if i[j][1] == 3:                        #naissances cellules
                    new_tab[compteur_lignes][j] = 1
                    compteur_naissances += 1
                else:                                   #maintiens d'une cellule morte
                    new_tab[compteur_lignes][j] = 0
            else:
                if i[j][1] == 2 or i[j][1] == 3:        #maintiens d'une cellule vivante
                    new_tab[compteur_lignes][j] = 1
                else:                                   #deces cellules
                    new_tab[compteur_lignes][j] = 0
                    compteur_deces += 1
        compteur_lignes += 1
    return [new_tab, compteur_naissances, compteur_deces]


#print(regles(10))

#####
##### PROGRAME FINALE :
##### Sans interface graphique 

def demo_sans_interface_graphique():
    """Programme de jeu final sans interface graphique"""
    k = input("Entrer un entier correspondant à la taille du quadrillage : ")
    input("Frappez <ENTER> pour commencer, <f> pour terminer.")
    nb_cellules = int(k) * int(k)
    compteur_nb_1 = 0
    nombre_jour = 1
    frap = ''
    tab = tableau(int(k))
    liste_voisins = voisins(tab, int(k))
    listetab = regles(liste_voisins, int(k))
    new_tab = listetab[0]
    compteur_naissances = 0
    compteur_deces = 0
    print("\n Jour 0 : \n")
    print(tab)
    for ligne in range(int(k)):
        for colonne in range(int(k)):
            if tab[ligne][colonne] == 1:
                compteur_nb_1 += 1
    print("\n Il y a", compteur_nb_1, "cellules vivantes sur un total", nb_cellules, "cellules au 'Jour 0'.")
    while frap == '':
        frap = input("")
        if frap == "f":
            break
        else:
            mini_compteur_naissance = 0
            mini_compteur_deces = 0
            print("Jour", nombre_jour, ": \n")
            print(new_tab)
            liste_voisins = voisins(new_tab, int(k))
            listenewtab = regles(liste_voisins, int(k))
            new_tab = listenewtab[0]
            mini_compteur_naissance = listetab[1]
            mini_compteur_deces =  listetab[2]
            compteur_naissances += mini_compteur_naissance
            compteur_deces += mini_compteur_deces
            nombre_jour += 1
            listetab = listenewtab
            print("Naissances:",mini_compteur_naissance, "\nDécès:", mini_compteur_deces)
    return("Et voici ce qu'on obtient en "+str(nombre_jour-1)+" jours ! Il y a eu "+str(compteur_naissances)+" naissances et "+str(compteur_deces)+" décès.")

#print(demo_sans_interface_graphique())

#####
##### Interface graphique :
##### 
"""Pour simplifier les choses on a fixé la taille du quadrillage. On prendra dans la suite k = 60"""

######
# Fenêtre pour les règles :
######

# # #
# Règles
# # #
def fenetre_regles():
    """Permet que quand on clic sur le bouton 'Règles du jeu' d'afficher une fenêtre avec un titre, un message et un autre bouton permettant de fermer cette fenêtre """
    Rgl = Toplevel(app)
    Rgl.title("Le jeu de la vie")
    Rgl.geometry("1092x845")
    titre = Label(Rgl, text = "Le jeu de la vie", font = ("Verdana", 20, "italic underline"))
    titre.pack()
    Regles_jeu = Message(Rgl, text = "Le jeu de la vie est un jeu de simulation au sens mathématique plutôt que ludique.\nLe jeu se déroule sur une grille à deux dimensions, dont les cases — qu’on appelle des « cellules », par analogie avec les cellules vivantes — peuvent prendre deux états distincts : « vivante » ou « morte ».\nUne cellule possède huit voisins, qui sont les cellules adjacentes horizontalement, verticalement et diagonalement.\n À chaque étape, l’évolution d’une cellule est entièrement déterminée par l’état de ses huit voisines de la façon suivante :\n\n––une cellule morte possédant exactement trois voisines vivantes devient vivante (elle naît) ; \n––une cellule vivante possédant deux ou trois voisines vivantes le reste, sinon elle meurt.", font = ("Verdana", 13))
    Regles_jeu.pack()

 # # #
 # Bouton 'ferme la fenêtre des règles'
 # # #
    Bouton_quitrgl = Button(Rgl, text = 'Fermer', font = ("Verdana", 13),width = 20, command = Rgl.destroy)
    Bouton_quitrgl.pack()

######
# Construction & initatilation du quadrillage :
######

def liste():
    """Permet de créer le quadrillage de taille 60 sur 60"""
    l = list(range(60))
    for i in l:
        l[i] = list(range(60))
        for j in range(60):
            l[i][j] = 0
    return l
    
def ini(n,p):
    """Initialise une cellule, ie : colore une cellule de ligne n et de colonne p en noir"""
    rectangle[n][p] = ca.create_rectangle(n * 10, p * 10, n * 10 + 10, p * 10 + 10, fill = 'black')

def detruit(n,p):
    """Détruit une cellule ie : colore une cellule de ligne n et de colonne p en noir"""
    rectangle[n][p] = ca.create_rectangle(n * 10, p * 10, n * 10 + 10, p * 10 + 10, fill = 'white')

def initialisation():
    """Initialisation du tableau aléatoirement"""
    global tab, compteur_jour, ca
    
    tab = tableau(60)
    for n  in range(60):
        for p in range(60):
            ca.delete(rectangle[n][p])
            if tab[n][p] == 1:
                ini(n,p)
            else:
                detruit(n,p)
    voisins(tab, 60)
    regles(liste_complete,60)
    compteur_naissance = regles(liste_complete,60)[1]
    compteur_mort = regles(liste_complete,60)[2]
    compteur_jour=0
    compteur0 = ca.create_text(500,560,text="Nombre de jours: " + str(compteur_jour), fill='purple')
    compteur1 = ca.create_text(500,575,text="Nombre de naissances: " + str(compteur_naissance), fill='purple')
    compteur2 = ca.create_text(500,590,text="Nombre de morts: " + str(compteur_mort), fill='purple')


def start():
    """Permet d'afficher le tableau au jour d'après."""
    global m,vitesse,tab,n,p,compteur_jour
    
    ca.delete(ALL)
    voisins(tab, 60)
    tab = regles(liste_complete,60)[0]
    compteur_naissance = regles(liste_complete,60)[1]
    compteur_mort = regles(liste_complete,60)[2]
    compteur_jour += 1
    
    for n  in range(60):
        for p in range(60):
            if tab[n][p] == 1:
                ini(n,p)
            else:
                detruit(n,p)
                
    compteur0 = ca.create_text(500,560,text="Nombre de jours: " + str(compteur_jour), fill='purple')
    compteur1 = ca.create_text(500,575,text="Nombre de naissances: " + str(compteur_naissance), fill='purple')
    compteur2 = ca.create_text(500,590,text="Nombre de morts: " + str(compteur_mort), fill='purple')

def start2():
    """Permet de faire défiler les tableaux ainsi que les jours""" 
    global m,compteur_jour,tab,n,p,vitesse
    
    ca.delete(ALL)
    voisins(tab, 60)
    tab = regles(liste_complete,60)[0]
    compteur_naissance = regles(liste_complete,60)[1]
    compteur_mort = regles(liste_complete,60)[2]
    compteur_jour += 1
    
    for n  in range(60):
        for p in range(60):
            if tab[n][p] == 1:
                ini(n,p)
            else:
                detruit(n,p)
                
    compteur0 = ca.create_text(500,560,text="Nombre de jours: " + str(compteur_jour), fill='purple')
    compteur1 = ca.create_text(500,575,text="Nombre de naissances: " + str(compteur_naissance), fill='purple')
    compteur2 = ca.create_text(500,590,text="Nombre de morts: " + str(compteur_mort), fill='purple')
    if m == 1:
        app.after(vitesse,start2)

def stop():
    """Stop l'animation"""
    global m
    m = 0

def continuer():
    """Permet d'avoir l'animation en continue"""
    global m
    m = 1
    start2()

###
# Fonction permettant de gérer la vitesse de l'annimation :
###
def vitesse1():
    """L'animation se rafraichie toute les secondes"""
    global vitesse
    vitesse = 1000

def vitesse2():
    """L'animation se rafraichie toute les demi_secondes"""
    global vitesse
    vitesse = 500

def vitesse10():
    """L'animation se rafraichie toute les dixièmes de secondes"""
    global vitesse
    vitesse = 100
    
def vitesse1000():
    """L'animation se rafraichie toute les milisecondes"""
    global vitesse
    vitesse = 1

######
## FENETRE & PROGRAMME FINAL :
###### Avec interface graphique 
def demo():
    """Jeu final avec interface graphique"""
    global app,m, vitesse,ca, rectangle

    app = Tk()
    app.geometry("1000x900")                        #taille fenetre
    app.title('Le jeu de la vie')                   #titre
    app.positionfrom("user")
    app.config(background = "#AAE7C0")
    #Titre

    Titre = Label(app, text = "Le jeu de la vie", font = ("Verdana", 40), fg = 'black', bg = "#AAE7C0")
    Titre.pack(expand = YES)

    #Boite
    frame = Frame(app, relief = SUNKEN)
    frame.pack(expand = YES)
    

    def lancement_jeu():
        """Permet d'accèder à la fenêtre de jeu."""
        global ca, rectangle, vitesse 
        fen2 = Toplevel(app)
        fen2.title("Le jeu de la vie")
        fen2.geometry("1000x900")
        fen2.positionfrom("user")
        fen2.config(background = "#AAE7C0")
        frame_fen2 = Frame(fen2)
        frame_fen2.pack(expand = YES)
        
###
# Les boîtes :
###

    # # #
    # Boîte quadrillage
    # # #
        frame_quadri = Frame(fen2, bg = "#AAE7C0")
        frame_quadri.pack(expand = YES)
    
    # # #
    # Boîte bouton
    # # #
        frame_bouton = Frame(frame_quadri, relief = SUNKEN)
        frame_bouton.pack(side = LEFT)
    
    # # #
    # Boîte bouton règle
    # # #
        frame_regle = Frame(frame_quadri)
        frame_regle.pack(side = BOTTOM)

###
# Les boutons :
###

    # Bouton "Initialisation":
        bouton_depart = Button(frame_bouton, text = "Jour 0", font = ("Verdana", 13), width = 20, bg='white', command = initialisation)
        bouton_depart.pack()

    # Bouton, "Activation de l'annimation":
        bouton_start = Button(frame_bouton, text = "Passer au jour d'après", font = ("Verdana", 13), width = 20, bg='white', command = start)
        bouton_start.pack()

    # Bouton, "Avoir l'annimation en continue":
        bouton_continuer = Button(frame_bouton, text = "Défiler les jours", font = ("Verdana", 13), width = 20, bg='white', command = continuer)
        bouton_continuer.pack()

    # Boutons "vitesses":
        bouton_vitesse1 = Button(frame_bouton, text = "vitesse x1", font = ("Verdana", 13), width = 20, bg='white', command = vitesse1)
        bouton_vitesse1.pack()

        bouton_vitesse2 = Button(frame_bouton, text = "vitesse x2", font = ("Verdana", 13), width = 20, bg='white', command = vitesse2)
        bouton_vitesse2.pack()

        bouton_vitesse10 = Button(frame_bouton, text = "vitesse x10", font = ("Verdana", 13), width = 20, bg='white', command = vitesse10)
        bouton_vitesse10.pack()

        bouton_vitesse1000 = Button(frame_bouton, text = "vitesse x1000", font = ("Verdana", 13), width = 20, bg='white', command = vitesse1000)
        bouton_vitesse1000.pack()
    
    # Bouton "Arrêt de l'annimation":
        bouton_stop = Button(frame_bouton, text = "Stop", font = ("Verdana", 13), width = 20,  bg='white', command = stop)
        bouton_stop.pack()
        
    # Bouton fermer la fenêtre 

        Bouton_fermer = Button(frame_bouton, text = 'Fermer', font = ("Verdana", 13), width = 20, bg='white', command = fen2.destroy)
        Bouton_fermer.pack()

####
# Valeurs initiales :
####
        m = 0
        vitesse = 1000

#Permet de construire le quadrillage et de stocker les différents rectangles dans la liste rectangle
        rectangle = liste()
        ca = Canvas(frame_quadri, width = 600, height = 600)
        for i in range(60):
            for j in range(60):
                longeur = i * 10
                hauteur = j * 10
                rectangle[i][j] = ca.create_rectangle(longeur, hauteur, longeur + 10, hauteur + 10, outline='black', fill='white')
        ca.pack()
    
####
# Les Règles
####

    def Regles():
        """fonction qui permet d'accèder à la fenêtre avec les règles."""
        Rgl = Toplevel(app)
        Rgl.title("Règles du jeu")
        Rgl.geometry("1000x900")
        Rgl.positionfrom("user")
        Rgl.config(background = "#AAE7C0")
        lab = Label(Rgl, text = "Les Règles du jeu\n", font = ("Verdana", 30), bg = "#AAE7C0")
        Regles_jeu = Message(Rgl, text = "Le jeu de la vie est un jeu de simulation au sens mathématique plutôt que ludique.\nLe jeu se déroule sur une grille à deux dimensions, dont les cases — qu’on appelle des « cellules », par analogie avec les cellules vivantes — peuvent prendre deux états distincts : « vivante » ou « morte ».\nUne cellule possède huit voisins, qui sont les cellules adjacentes horizontalement, verticalement et diagonalement.\nÀ chaque étape, l’évolution d’une cellule est entièrement déterminée par l’état de ses huit voisines de la façon suivante :\n\n –– une cellule morte possédant exactement trois voisines vivantes devient vivante (elle naît) ; \n––une cellule vivante possédant deux ou trois voisines vivantes le reste, sinon elle meurt.\n", font = ("Verdana", 13), bg = "#AAE7C0")
        lab.pack()
        Regles_jeu.pack()
        Bouton_quitrgl = Button(Rgl, text = 'Fermer', font = ("Verdana", 20), command = Rgl.destroy)
        Bouton_quitrgl.pack()

####
# Boutons premières fenêtre 
####

    B1 = Button(frame, text = "Règles du jeu", font = ("Verdana", 20), bg='white', width = 20, command = Regles)
    Bouton_depart = Button(frame, text = "Commencer le jeu", font = ("Verdana", 20),  bg='white', width = 20, command = lancement_jeu)
    
    Bouton_depart.pack(expand = YES)
    B1.pack()
    
    
    app.mainloop()

########
## JOUER :
########
"""Décommenter pour commencer."""

#print(demo_sans_interface_graphique())  # Essayer avec 31
#print(demo()) 

########