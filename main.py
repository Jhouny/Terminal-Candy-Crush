import matplotlib.pyplot as plt
from random import randint

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
        if ( abs(i1-i2), abs(j1-j2) ) in [ (1, 0) , (0, 1) ]:
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

    for i in grille:
        for j in i:
            print(j, end=" ")
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

if __name__=="__main__":
    gr = creer_grille_aleatoire(5)
    affichage_grille(gr, 0)
    echanger_bonbons(gr, 0, 0, 1, 0)
    affichage_grille(gr, 0)
    print(len(detecte_coordonnees_combinaison(gr, 2, 2)))