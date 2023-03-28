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

commande_efface_ecran = ""  
if os.name == 'nt':  # Si on est sur Windows
    commande_efface_ecran = "cls"
elif os.name == 'posix':  # Si on est sur Linux
    commande_efface_ecran = "clear"

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
    """
    Copie la grille initiale 
    
    """
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
    colonnes_modifiees = []
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            y = i
            if grille[i][j] == 0 and (j not in colonnes_modifiees):
                while y > 0:
                    grille[y][j] = grille[y-1][j]
                    y -= 1
                grille[y][j] = randint(1, len(CouleursBonbons) - 1)
                colonnes_modifiees.append(j)
                

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
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i,j] == 0 :
                grille[i,j] = (randint(1,len(CouleursBonbons)-1))


def verifie_possibilitees(grille):
    """
    Verifie s'il est encore possible d'échanger deux bonbons pour faire une 
    combinaison. S'il est possible, renvoie True. Sinon, renvoie False.
    """
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if i+1 < len(grille) and bouger_bonbons(grille,i,j,i+1,j, modifier = False) == True :
                return True
            elif j-1 > 0 and bouger_bonbons(grille,i,j,i,j-1) == True :
                return True
            elif i-1 > 0 and bouger_bonbons(grille,i,j,i-1,j, modifier= False) == True :
                return True
            elif j+1 < len(grille[0]) and bouger_bonbons(grille,i,j,i,j+1, modifier = False ) == True :
                return True
    


def quitter():
    """
    Verifie l'etat du jeu: si on est en train de jouer
    retourne au menu principal, sinon arrete le programme
    """
    global enCourse, etatJeu
    if etatJeu == "JEU":  # Si le jeu est en cours d'execution, retourne à l'ecran principale
        etatJeu = "MENU"
    else:                 # Sinon, quitter le programme
        enCourse = False
def changer_taille_grille(N: list):
    global taille_tableau
    taille_tableau = int(N[0])
def creer_tableau():
    global points, grille
    points = 0
    grille = creer_grille_aleatoire(taille_tableau)
def commencer_jeu():
    global etatJeu, points
    etatJeu = "JEU"
    points = 0
    creer_tableau()
def redemarrer():
    global points, grille
    points = 0
    grille = creer_grille_aleatoire(taille_tableau)
def echanger(args: list):
    global grille
    succes = bouger_bonbons(grille, int(args[0].split(',')[0]), int(args[1].split(',')[0]), int(args[0].split(',')[1]), int(args[1].split(',')[1]))
    if not succes:
        print(WARNING + BOLD + "Les coordonnees donnees n'engendrent pas une combinaison..." + ENDC)
        sleep(1.6)  # Valeur arbitraire

def efface_ecran(cmd=commande_efface_ecran):
    """
    Utilise la bibliotheque OS pour effacer le terminal
    """
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

fonctions = [quitter,
             changer_taille_grille,
             commencer_jeu,
             echanger,
             redemarrer]

def gerer_entree(commande: str, args):
    """
    Verifie si l'entree est valide, au cas où decide quoi faire --> echanger
    bonbons, quitter le jeu, redemarrer la partie, etc.
    """    
    if commande in commandes:
        ind = commandes.index(commande)
        arg = args[1:]
        if len(arg) > 0:
            fonctions[ind](arg)
        else:
            fonctions[ind]()

def afficher_points():
    string = f"Points: {points}"
    print(f"{string:>{taille_tableau*2 + 12}}\n")

def afficher_jeu():
    """
    Appele la fonction qui affiche la grille
    """
    if(etatJeu == "JEU"):
        afficher_points()
        affichage_grille(grille, 0)

def animation():
    efface_ecran()
    while nombre_vides(grille) > 0:
        afficher_commandes_possibles(etatJeu)
        afficher_jeu()
        sleep(delai)
        efface_ecran()
        descendre_bonbons(grille)
    afficher_commandes_possibles(etatJeu)
    afficher_jeu()

def mise_a_jour_jeu() -> bool:
    """
    Verifie les combinaisons et gère les points
    """
    global points, taille_tableau, grille
    des_combinaisons = False
    for i in range(taille_tableau):
        for j in range(taille_tableau):
            coords = detecte_coordonnees_combinaison(grille, i, j)
            if len(coords) >= 3:  # Si il y a des cases où des combinaisons sont faits, supprime les et augmente les points
                points += len(coords)
                supprime_bonbons(grille, coords)
                des_combinaisons = True
    return des_combinaisons


def main():
    global taille_tableau, etatJeu
    grille = creer_grille_vide(taille_tableau)

    efface_ecran(commande_efface_ecran)
    while enCourse:
        afficher_commandes_possibles(etatJeu)
        if etatJeu == "JEU":
            affichage_grille(grille, 0)
            mise_a_jour_jeu()
            animation()
            while mise_a_jour_jeu() == True:  # Verifie qu'après la descente il n'y reste plus des combinaisons
                sleep(0.7)  # Attends un peu pour "combiner" les resultats de la descente
                animation()
            if verifie_possibilitees(grille) == False:
                etatJeu = "MENU"
        
        commande = input("Commande: ").split(" ")
        gerer_entree(commande[0], commande)
        efface_ecran(commande_efface_ecran)

if __name__=="__main__":
    main()