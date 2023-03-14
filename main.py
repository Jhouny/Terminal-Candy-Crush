import matplotlib.pyplot as plt
from random import randint
import os
from time import sleep

def creer_grille_aleatoire(N: int):
    """
    Crée et renvoie une grille 2D de taille NxN avec des valeurs aleatoires entre 
    1 et 4 pour les couleurs des bonbons -->
        1: Bleu
        2: Rouge
        3: Jaune
        4: Vert
    """
    return [[randint(1, 4) for i in range(N)] for i in range(N)]

def creer_grille_vide(N: int):
    """
    Crée et renvoie une grille 2D vide de taille NxN (vide: valeur 0)
    """
    return [[0]*N]*N

def coordonnees_in_range(grille, i, j):
    """
    Helper function: verifie si les coordonnees sont bien dans la grille
    """
    # Pas du tout la meilleure façon de verifier les bornes, j'ai juste bien aimé la notation des maths XD
    if (i not in range(0, len(grille)) or j not in range(0, len(grille[0]))):
        return False
    else:
        return True

def echanger_bonbons(grille, i1, i2, j1, j2):  # 
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
    
def detecte_coordonnees_combinaison(grille, i, j):
    """
    Renvoie une liste contenant les coordonnées de tous les bonbons
    appartenant à la combinaison du bonbon (i, j), s'il y a une. 
    """
    if coordonnees_in_range(grille, i, j):
        # Fait d'abord l'analyse horizontale
        bonbons = []  # Stocker les bonbons valides
        somme = 0  # Compte la taille de la combinaison
        ind = i
        while grille[ind][j] == grille[i][j]:
            bonbons.append((ind, j))
            ind -= 1
            somme += 1

        ind = i+1
        while grille[ind][j] == grille[i][j]:
            bonbons.append((ind, j))
            ind += 1
            somme += 1

        if somme >= 3:
            return bonbons
        else:
            # Ensuite, s'il n'y a pas de combinaison horizontale, verifie la droite verticale
            bonbons = []
            somme = 0 
            ind = j
            while grille[i][ind] == grille[i][j]:
                bonbons.append((ind, j))
                ind -= 1
                somme += 1

            ind = j+1
            while grille[i][ind] == grille[i][j]:
                bonbons.append((ind, j))
                ind += 1
                somme += 1

            if somme >= 3:
                return bonbons
    return []
        

def explication_jeu():
    """
    Donne des explications sur le fonctionnement du jeu
    """


def affichage_grille(grille, nb_type_bonbons):
    """
    Affiche la grille de jeu "grille" contenant au
    maximum "nb_type_bonbons" couleurs de bonbons différentes.
    """
    """
    plt.imshow(grille, vmin=0, vmax=nb_type_bonbons−1, cmap='jet')
    plt.pause(0.1)
    plt.draw()
    plt.pause(0.1)
    """
    print(" __|", end="")
    for i in range(len(grille)-1):
        print(f"_{i}", end="_|")
    print(f"_{len(grille)-1}", end="_")
    print()
    for i in range(len(grille)):
        print(f" {i} |", end="")
        for j in grille[i]:
            print(f" {j} ", end=" ")
        print()
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


def supprime_bonbons(grille, index):
    """
    Supprime la combinaison de 3 bonbons - remplace les valeurs par 0 et
    augmente les points. 
    """


def descendre_bonbons(grille, index):
    """
    Fait descendre les bonbons déjà existants pour remplir le trou
    laissé par la fonction supprime_bonbons
    """

def remplir_grille(grille):
    """
    Remplit les trous vides de la grille avec des valeurs aléatoires entre 
    1 et 4 aprés avoir utilisé la fonction descendre_bonbons
    """


def verifier_possibilite(grille):
    """
    Verifie s'il est encore possible d'échanger deux bonbons pour faire une 
    combinaison. S'il est possible, renvoie True. Sinon, renvoie False.
    """

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Jeu():
    def __init__(self) -> None:
        self.taille_tableau = -1
        self.grille = None
        self.commande_efface_ecran = ""  
        if os.name == 'nt':  # Si on est sur Windows
            self.commande_efface_ecran = "cls"
        elif os.name == 'posix':  # Si on est sur Linux
            self.commande_efface_ecran = "clear"

        self.enCourse = True
        self.etatJeu = False

        """
        Structure par index: 0 -> commande à appeller:
                             1 -> Description du commande
                             2 -> Nombre d'arguments que la fonction accepte
        """                       
        self.command_palette = {  
            'quitter': [self.quitter, "Quitte le jeu si pendant une partie, sinon ferme le programme"],
            'taille': [self.definir_taille_tableau, "Defini la taille du tableau "],
            'commencer': [self.commencer_jeu, "Commence la partie"],
            'echanger': [echanger_bonbons, "Echange la position de deux bonbons"],
            'redemarrer': [self.redemarrer, "Redemarre la partie en cours"],
        }


    def efface_ecran(self):
        os.system(self.commande_efface_ecran)

    def definir_taille_tableau(self, N: int):
        self.taille_tableau = N
        print(f"Taille defini égale à: {self.taille_tableau}...")
        sleep(2)  # Attends 2 secondes pour qu'on puisse lire

    def creer_tableau(self):
        self.grille = creer_grille_aleatoire(self.taille_tableau)
    

    # Serie des fonctions pour appelle des commandes
    def quitter(self):
        if self.etatJeu == True:  # Si le jeu est en cours d'execution, retourne à l'ecran principale
            self.etatJeu = False
        else:                     # Sinon, quitter le programme
            self.enCourse = False
    
    def commencer_jeu(self):
        self.etatJeu = True
        self.creer_tableau()

    def redemarrer(self):
        self.grille = creer_grille_aleatoire(self.taille_tableau)

    def afficher_commandes_possibles(self):
        print(bcolors.WARNING + "Serie de commandes possibles: " + bcolors.ENDC)
        for commande in self.command_palette.keys():
            print(f"Ecrivez {bcolors.BOLD}{commande}{bcolors.ENDC} pour: {self.command_palette[commande][1]}")

    def gerer_entree(self, commande: str, args):
        """
        Verifie si l'entree est valide, au cas où decide quoi faire --> echanger
        bonbons, quitter le jeu, redemarrer la partie, etc.
        """    

        if commande in self.command_palette.keys():
            arg = [int(i) for i in args[1:]]
            if len(arg) > 0:
                self.command_palette[commande][0](arg)
            else:
                self.command_palette[commande][0]()

    def commencer_jeu(self):
        self.etatJeu = True



def main():
    candyCrush = Jeu()
    candyCrush.efface_ecran()
    while candyCrush.enCourse:
        candyCrush.afficher_commandes_possibles()
        commande = input("Commande: ").split(" ")
        print(commande)
        candyCrush.gerer_entree(commande[0], commande)
        candyCrush.efface_ecran()

if __name__=="__main__":
    main()