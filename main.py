from deps import *
from random import randint
import os
from time import sleep

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
        somme = 0  # Compte la taille de la combinaison
        ind = i
        while ind >= 0 and grille[ind][j] == grille[i][j]:
            bonbons.append((ind, j))
            ind -= 1
            somme += 1

        ind = i+1
        while ind < len(grille) and grille[ind][j] == grille[i][j]:
            bonbons.append((ind, j))
            ind += 1
            somme += 1

        if len(bonbons) >= 3:
            return bonbons
        else:
            # Ensuite, s'il n'y a pas de combinaison verticale, verifie la droite horizontale
            bonbons = []
            somme = 0 
            ind = j
            while ind >= 0 and grille[i][ind] == grille[i][j]:
                bonbons.append((i, ind))
                ind -= 1
                somme += 1

            ind = j+1
            while ind < len(grille[0]) and grille[i][ind] == grille[i][j]:
                bonbons.append((i, ind))
                ind += 1
                somme += 1
            
            if len(bonbons) >= 3:
                return bonbons

    return []


def bouger_bonbons(grille, i1, i2, j1, j2):
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
       echanger_bonbons(grille, i1, i2, j1, j2)
       print("here")
       return True
    else:
        return False


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


def supprime_bonbons(grille, index: list):
    """
    Supprime la combinaison de bonbons - remplace les valeurs par 0. 
    """
    for i, j in index:
        grille[i][j] = 0


def descendre_bonbons(grille, index: list, pas = 1):
    """
    Fait descendre les bonbons déjà existants pour remplir le trou
    laissé par la fonction supprime_bonbons (retourné sur 'index')
    """
    elements = set(index)  # Au cas où 'index' contient des valeurs dupliquées
    while len(elements) > 0:
        x, y = min(elements)
        i = x
        while i < len(grille)-1 and grille[i][y] != 0:
            i += 1
        j = y
        steps = 0
        
        elements.remove((x,y))
        index.remove((x,y))
        supp = []
        for a,b in elements:
            if b == y and a > x:
                supp.append((a,b))
        for elem in supp:
            elements.remove(elem)

        while i >= 0 and i < len(grille) and steps < pas:
            try:
                if grille[i+1][j] == 0:
                    grille[i+1][j] = grille[i][j]
                    grille[i][j] = 0
            except IndexError:
                pass
            i -= 1
        grille[0][j] = randint(1, len(Bonbons)-1)


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
        self.grille = creer_grille_vide(self.taille_tableau)
        self.points = 0
        self.commande_efface_ecran = ""  
        if os.name == 'nt':  # Si on est sur Windows
            self.commande_efface_ecran = "cls"
        elif os.name == 'posix':  # Si on est sur Linux
            self.commande_efface_ecran = "clear"

        self.enCourse = True
        self.etatJeu = "MENU"

        self.delai = 0.6  # 600ms delai 

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
        self.points = 0
        self.grille = creer_grille_aleatoire(self.taille_tableau)
    
    def echanger(self, args: list):
        #echanger_bonbons(self.grille, int(args[0].split(',')[0]), int(args[1].split(',')[0]), int(args[0].split(',')[1]), int(args[1].split(',')[1]))
        succes = bouger_bonbons(self.grille, int(args[0].split(',')[0]), int(args[1].split(',')[0]), int(args[0].split(',')[1]), int(args[1].split(',')[1]))
        if not succes:
            print(bcolors.RED + bcolors.BOLD + "Les coordonnees donnees n'engendrent pas une combinaison..." + bcolors.ENDC)
            sleep(1.6)  # Valeur arbitraire

    # Serie des fonctions pour appelle des commandes
    def quitter(self):
        if self.etatJeu == "JEU":  # Si le jeu est en cours d'execution, retourne à l'ecran principale
            self.etatJeu = "MENU"
        else:                     # Sinon, quitter le programme
            self.enCourse = False
    
    def commencer_jeu(self):
        self.etatJeu = "JEU"
        self.points = 0
        self.creer_tableau()

    def redemarrer(self):
        self.points = 0
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

    def afficher_points(self):
        string = f"Points: {self.points}"
        print(f"{string:>{self.taille_tableau*2 + 12}}\n")

    def afficher_jeu(self):
        """
        Appele la fonction qui affiche la grille
        """
        if(self.etatJeu == "JEU"):
            self.afficher_points()
            affichage_grille(self.grille, 0)

    def animation(self, index: list):
        self.efface_ecran()
        while nombre_vides(self.grille):
            self.afficher_commandes_possibles()
            self.afficher_jeu()
            sleep(self.delai)
            self.efface_ecran()
            descendre_bonbons(self.grille, index)
        
        self.afficher_commandes_possibles()
        self.afficher_jeu()

    def mise_a_jour_jeu(self, animate=True):
        """
        Verifie les combinaisons et gère les points
        """
        enlevees = []
        for i in range(self.taille_tableau):
            for j in range(self.taille_tableau):
                coords = detecte_coordonnees_combinaison(self.grille, i, j)
                if len(coords) >= 3:  # Si il y a des cases où des combinaisons sont faits, supprime les et augmente les points
                    self.points += len(coords)
                    supprime_bonbons(self.grille, coords)
                    enlevees += coords
        if animate == True:
            self.animation(enlevees)


def main():
    candyCrush = Jeu()
    candyCrush.efface_ecran()
    while candyCrush.enCourse:
        candyCrush.afficher_commandes_possibles()
        if candyCrush.etatJeu == "JEU":
            candyCrush.afficher_jeu()
            candyCrush.mise_a_jour_jeu()
        
        commande = input("Commande: ").split(" ")
        candyCrush.gerer_entree(commande[0], commande)

        candyCrush.efface_ecran()

if __name__=="__main__":
    main()