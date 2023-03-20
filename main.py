from deps import *
from random import randint
import os
from time import sleep

# ~~~~~~~~~~ Variables principaux du programme ~~~~~~~~~~ #
taille_tableau = 5  # Valeur defaut
grille = []
points = 0

enCourse = True
etatJeu = "MENU"

delai = 0.45  # 450ms delai pour l'animation

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def creer_grille_aleatoire(N: int):
    """
    Crée et renvoie une grille 2D de taille NxN avec des valeurs aleatoires 
    (qui correspondent aux types de Bonbon sur l'objet 'Bonbons')    
    """
    return [[randint(1, len(CouleursBonbons)-1) for i in range(N)] for i in range(N)]


def creer_grille_vide(N: int):
    """
    Crée et renvoie une grille 2D vide de taille NxN (vide: valeur 0)
    """
    return [[0]*N]*N


def copier_grille(grille: list) -> list:
    liste_copie = creer_grille_vide(len(grille))
    for i in range(len(grille)):
        liste_copie[i] = grille[i].copy()
    return liste_copie


def coordonnees_in_range(grille, i, j):
    """
    Helper function: verifie si les coordonnees sont bien dans la grille
    """
    # Pas du tout la meilleure façon de verifier les bornes, j'ai juste bien aimé la notation des maths XD
    if (i not in range(0, len(grille)) or j not in range(0, len(grille[0]))):
        return False
    else:
        return True


def echanger_bonbons(grille, i1, i2, j1, j2) -> bool:
    """
    Échange la position dans la grille du bonbon de coordonnées (i1,j1) avec 
    celui de coordonnées (i2, j2), choisis par le joueur (si les coordonnées
    sont valides: à côté l'une de l'autre).
    """
    if coordonnees_in_range(grille, i1, j1) and coordonnees_in_range(grille, i2, j2):
        # Si les bonbons sont alignées horizontalement ou verticalement(mais pas diagonalement) les échange
        if abs(i1-i2) + abs(j1-j2) == 1:
            temp = grille[i1][j1]
            grille[i1][j1] = grille[i2][j2]
            grille[i2][j2] = temp
            return True
        else:
            return False
    else:
        return False


def detecte_coordonnees_combinaison(grille, i, j) -> list:
    """
    Renvoie une liste contenant les coordonnées de tous les bonbons
    appartenant à la combinaison du bonbon (i, j), s'il y a une. 
    """
    if coordonnees_in_range(grille, i, j) and grille[i][j] != 0:
        # Fait d'abord l'analyse verticale
        bonbons = []  # Stocker les bonbons valides
        ind = i
        while ind >= 0 and grille[ind][j] == grille[i][j]:
            bonbons.append((ind, j))
            ind -= 1

        ind = i+1
        while ind < len(grille) and grille[ind][j] == grille[i][j]:
            bonbons.append((ind, j))
            ind += 1

        if len(bonbons) >= 3:
            return bonbons
        else:
            # Ensuite, s'il n'y a pas de combinaison verticale, verifie la droite horizontale
            bonbons = []
            ind = j
            while ind >= 0 and grille[i][ind] == grille[i][j]:
                bonbons.append((i, ind))
                ind -= 1

            ind = j+1
            while ind < len(grille[0]) and grille[i][ind] == grille[i][j]:
                bonbons.append((i, ind))
                ind += 1
            
            if len(bonbons) >= 3:
                return bonbons

    return []


def bouger_bonbons(grille, i1, i2, j1, j2, modifier=True):
    """
    Verifie si l'echange entre les bonbons est valide, au cas
    où echanger_bonbons est appelée et renvoie True, sinon
    renvoie False
    """
    grille_2 = copier_grille(grille)
    # Essaie de faire l'echange pour verifier si ça engendre des combinaisons
    echanger_bonbons(grille_2, i1, i2, j1, j2)
    if (len(detecte_coordonnees_combinaison(grille_2, i1, j1)) >= 3 or
       len(detecte_coordonnees_combinaison(grille_2, i2, j2)) >= 3):
       if modifier:
            echanger_bonbons(grille, i1, i2, j1, j2)
       return True
    else:
        return False


def explication_jeu():
    """
    Donne des explications sur le fonctionnement du jeu dans la lague choisi
    """
    print("Bienvenue dans ce merveilleux jeu\"Candy Crush\"!!")
    print("\nObjectif du jeu: ")
    print("Dans un temps défini par le joueur, l'objectif est de marquer des points en échangeant de position les bonbons")
    print("\nRègles du jeu: ")
    print("1. Une combinaison est possible si 3 bonbons de la même couleur ou plus sont alignés verticalement ou horizontalement")
    print("2. Pour créer cette combinaison, le joueur peut échanger un bonbon avec son voisin")
    print("3. Mais attention!!! C'est possible seulement si le changement crée une combinaison")
    print("4. Chaque combinaison realisée donne des points en fonction du nombre de bonbons")
    print("5. S'il n'y a plus de combinaison possibles, la grille sera remplacée automatiquement")

    print("Bienvenido a este maravilloso juego \"Candy Crush\"!!")
    print("\nObjetivo del juego: ")
    print("En un tiempo definido por el jugador, el objetivo es de conseguir puntos intercambiando las posiciones de los dulces ")
    print("\nReglas del juego: oh lala ")
    print("1. Una combinación es posible si tres o más dulces están alineados vertical u horizontalmente")
    print("2. Para crear esta combinación, el jugador puede intercambiar un dulce con su vecino")
    print("3. ¡¡¡Pero cuidado!!! Es posible solamente si el intercambio crea una combinación")
    print("4. Cada combinación realizada da puntos en función del número de dulces")
    print("5. Si no hay más combinaciones posibles, el tablero será remplazado automáticamente")
    
    

def affichage_grille(grille, nb_type_bonbons):
    """
    Affiche la grille de jeu "grille" contenant au
    maximum "nb_type_bonbons" couleurs de bonbons différentes.
    """

    s = f"{UNDERLINE} {chr(0x2502)}"  # Char pour barre verticale
    for i in range(len(grille)-1):
        s += f"{i}{chr(0x2502)}"
    s += f"{len(grille)-1}{ENDC}"
    print(s)

    for i in range(len(grille)):
        stringFinal = f"{i}{chr(0x2502)}"
        for bonbon in grille[i]:
            stringFinal += f"{CouleursBonbons[bonbon]}{CharsBonbons[bonbon]}{ENDC} "
        print(stringFinal)
    print()


def test_detecte_coordonnees_combinaison():
    """
    Test la fonction detecte_coordonnees_combinaison(grille, i, j).
    Pour chaque cas de test, affiche True si le test passe,
    False sinon
    """
    """
    # Test1: Description du cas testé    plt.imshow
    grille = # Donner une liste
    i = # Donner un entier
    j = # Donner un entier
    # print(detecte_coordonnees_combinaison(grille,i,j) == # Résultat attendu
    
    # Test2: Description du cas te    # ...sté
    grille = # Donner une liste
    i = # Donner un entier
    j = # Donner un entier
    # print(detecte_coordonnees_combinaison(grille,i,j) == # Résultat attendu
    
    # ...
    """


def supprime_bonbons(grille, index: list):
    """
    Supprime la combinaison de bonbons - remplace les valeurs par 0. 
    """
    for i, j in index:
        grille[i][j] = 0


def descendre_bonbons(grille):
    """
    Fait descendre les bonbons déjà existants pour remplir le trou
    laissé par la fonction supprime_bonbons
    """
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            y = i
            if grille[i][j]==0 :
                while y > 0 :
                    grille[y][j]=grille[y-1][j]
                    y -= 1
                if y == 0 :
                    grille[y][j]= randint(1, len(CouleursBonbons) - 1)
                    
                    
                

def nombre_vides(grille):
    """
    Fonction qui compte le nombre de cases vides
    """
    total = 0
    for i in grille:
        for j in i:
            if j == 0:
                total += 1
    return total


def remplir_grille(grille):
    """  ON EN A BESOIN?
    Remplit les trous vides de la grille avec des valeurs aléatoires entre 
    1 et 4 aprés avoir utilisé la fonction descendre_bonbons
    """


def verifier_possibilite(grille):
    """
    Verifie s'il est encore possible d'échanger deux bonbons pour faire une 
    combinaison. S'il est possible, renvoie True. Sinon, renvoie False.
    """
    combinaisons = 0
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if i+1 < len(grille) and bouger_bonbons(grille,i,j,i+1,j, modifier = False) == True :
                combinaisons += 1
            if j-1 > 0 and bouger_bonbons(grille,i,j,i,j-1) == True :
                combinaisons += 1
            if i-1 > 0 and bouger_bonbons(grille,i,j,i-1,j, modifier= False) == True :
                combinaisons += 1
            if j+1 < len(grille[0]) and bouger_bonbons(grille,i,j,i,j+1, modifier = False ) == True :
                combinaisons += 1
    
    if combinaisons == 0 :
        return False 
    else :
        return True 


def quitter():
    """
    Verifie l'etat du jeu: si on est en train de jouer
    retourne au menu principal, sinon arrete le programme
    """
    if etatJeu == "JEU":  # Si le jeu est en cours d'execution, retourne à l'ecran principale
        etatJeu = "MENU"
    else:                 # Sinon, quitter le programme
        enCourse = False

def efface_ecran(cmd):
    os.system(cmd)

def afficher_commandes_possibles(etatJeu):
    print(JAUNE + "Serie de commandes possibles: " + ENDC)
    for i in range(len(commandes)):
        commande = commandes[i]
        if etatJeu == "JEU" and commandes[i] in ['quitter', 'echanger', 'redemarrer']:
            print(f"\tEcrivez {BOLD}{commande}{ENDC} pour: {explications[i]}")
        elif etatJeu == "MENU" and commandes[i] in ['quitter', 'commencer', 'taille']:
            print(f"\tEcrivez {BOLD}{commande}{ENDC} pour: {explications[i]}")
    print()

def 


def main():
    grille = creer_grille_vide(taille_tableau)

    commande_efface_ecran = ""  
    if os.name == 'nt':  # Si on est sur Windows
        commande_efface_ecran = "cls"
    elif os.name == 'posix':  # Si on est sur Linux
        commande_efface_ecran = "clear"

    efface_ecran(commande_efface_ecran)
    while enCourse:
        afficher_commandes_possibles(etatJeu)
        if etatJeu == "JEU":
            affichage_grille(grille, 0)
            mise_a_jour_jeu()
        
        commande = input("Commande: ").split(" ")
        gerer_entree(commande[0], commande)

        efface_ecran(commande_efface_ecran)

if __name__=="__main__":
    main()