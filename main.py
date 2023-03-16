from deps import *
from random import randint
import os

def creer_grille_aleatoire(N: int):
    """
    Crée et renvoie une grille 2D de taille NxN avec des valeurs aleatoires 
    (qui correspondent aux types de Bonbon sur l'objet 'Bonbons')    
    """
    return [[randint(1, len(Bonbons)-1) for i in range(N)] for i in range(N)]

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

def echanger_bonbons(grille, i1, i2, j1, j2):
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
    if coordonnees_in_range(grille, j, i):
        # Fait d'abord l'analyse horizontale
        bonbons = []  # Stocker les bonbons valides
        somme = 0  # Compte la taille de la combinaison
        ind = i
        while grille[ind][j] == grille[i][j] and ind >= 0:
            bonbons.append((j, ind))
            ind -= 1
            somme += 1

        ind = i+1
        while grille[ind][j] == grille[i][j] and ind < len(grille):
            bonbons.append((j, ind))
            ind += 1
            somme += 1

        if somme >= 3:
            return bonbons
        else:
            # Ensuite, s'il n'y a pas de combinaison horizontale, verifie la droite verticale
            bonbons = []
            somme = 0 
            ind = j
            while grille[i][ind] == grille[i][j] and ind >= 0:
                bonbons.append((ind, i))
                ind -= 1
                somme += 1

            ind = j+1
            while grille[i][ind] == grille[i][j] and ind < len(grille[0]):
                bonbons.append((ind, i))
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

    tS = os.get_terminal_size()[0]
    s = f"\033[4m {chr(0x2502)}"
    for i in range(len(grille)-1):
        s += f"{i}{chr(0x2502)}"
    s += f"{len(grille)-1}\033[0m"
    print(s)

    for i in range(len(grille)):
        stringFinal = f"{i}{chr(0x2502)}"
        for j in grille[i]:
            bonbon = Bonbons[j]
            stringFinal += f"{bonbon.COULEUR()}{bonbon.CH()}{bcolors.ENDC} "
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


def supprime_bonbons(grille, index: list) -> int:
    """
    Supprime la combinaison de bonbons - remplace les valeurs par 0 et
    renvoie les points. 
    """
    for i, j in index:
        grille[i][j] = 0

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


class Jeu():
    def __init__(self) -> None:
        self.taille_tableau = 5  # Valeur defaut
        self.grille = None
        self.commande_efface_ecran = ""  
        if os.name == 'nt':  # Si on est sur Windows
            self.commande_efface_ecran = "cls"
        elif os.name == 'posix':  # Si on est sur Linux
            self.commande_efface_ecran = "clear"

        self.enCourse = True
        self.etatJeu = "MENU"

        """
        Structure par index: 0 -> commande à appeller:
                             1 -> Description du commande
                             2 -> Nombre d'arguments que la fonction accepte
                             3 -> "PRT" si le commande est toujours disponible (En Jeu et dans le Menu), 
                                  "JEU" si juste en jeu, "MENU" si juste en menu.
                            
        """                       
        self.command_palette = {  
            'quitter': [self.quitter, "Quitte le jeu si pendant une partie, sinon ferme le programme", 0, "PRT"],
            'taille': [self.definir_taille_tableau, "Defini la taille du tableau ", 1, "MENU"],
            'commencer': [self.commencer_jeu, "Commence la partie", 0, "MENU"],
            'echanger': [self.echanger, "Echange la position de deux bonbons (e.g. echanger i1,j1 i2,j2)", 0, "JEU"],
            'redemarrer': [self.redemarrer, "Redemarre la partie en cours", 0, "JEU"]
        }


    def efface_ecran(self):
        os.system(self.commande_efface_ecran)

    def definir_taille_tableau(self, args: list):
        self.taille_tableau = int(args[0])

    def creer_tableau(self):
        self.grille = creer_grille_vide(self.taille_tableau)
    
    def echanger(self, args: list):
        #echanger_bonbons(self.grille, int(args[0].split(',')[0]), int(args[1].split(',')[0]), int(args[0].split(',')[1]), int(args[1].split(',')[1]))
        echanger_bonbons(self.grille, int(args[0].split(',')[1]), int(args[1].split(',')[1]), int(args[0].split(',')[0]), int(args[1].split(',')[0]))

    # Serie des fonctions pour appelle des commandes
    def quitter(self):
        if self.etatJeu == "JEU":  # Si le jeu est en cours d'execution, retourne à l'ecran principale
            self.etatJeu = "MENU"
        else:                     # Sinon, quitter le programme
            self.enCourse = False
    
    def commencer_jeu(self):
        self.etatJeu = "JEU"
        self.creer_tableau()

    def redemarrer(self):
        self.grille = creer_grille_aleatoire(self.taille_tableau)

    def afficher_commandes_possibles(self):
        print(bcolors.YELLOW + "Serie de commandes possibles: " + bcolors.ENDC)
        for commande in self.command_palette.keys():
            if self.etatJeu == "JEU" and self.command_palette[commande][3] in ["PRT", "JEU"]:
                print(f"\tEcrivez {bcolors.BOLD}{commande}{bcolors.ENDC} pour: {self.command_palette[commande][1]}")
            elif self.etatJeu == "MENU" and self.command_palette[commande][3] in ["PRT", "MENU"]:
                print(f"\tEcrivez {bcolors.BOLD}{commande}{bcolors.ENDC} pour: {self.command_palette[commande][1]}")
        print()

    def gerer_entree(self, commande: str, args):
        """
        Verifie si l'entree est valide, au cas où decide quoi faire --> echanger
        bonbons, quitter le jeu, redemarrer la partie, etc.
        """    
        if commande in self.command_palette.keys():
            arg = args[1:]
            if len(arg) > 0:
                self.command_palette[commande][0](arg)
            else:
                self.command_palette[commande][0]()

    def afficher_jeu(self):
        """
        Appele la fonction qui affiche la grille
        """
        if(self.etatJeu == "JEU"):
            affichage_grille(self.grille, 0)
    
    def mise_a_jour_jeu(self):
        """
        Verifie les combinaisons et gère les points
        """


def main():
    candyCrush = Jeu()
    candyCrush.efface_ecran()
    while candyCrush.enCourse:
        candyCrush.afficher_commandes_possibles()
        if candyCrush.etatJeu == "JEU":
            candyCrush.afficher_jeu()
        commande = input("Commande: ").split(" ")
        candyCrush.gerer_entree(commande[0], commande)
        candyCrush.efface_ecran()

if __name__=="__main__":
    main()