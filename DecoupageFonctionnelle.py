"""
Groupe: 82
Étudiants:  Jhony Minetto Araujo
            Imane Taarabit
            Nino Lemuet
            Sebastian Linares

Date: 13/03/2023            
"""

import matplotlib.pyplot as plt

def creer_grille_aleatoire(N: int):
    """
    Crée et renvoie une grille 2D de taille NxN avec des valeurs aleatoires entre 
    1 et 4 pour les couleurs des bonbons -->
        1: Bleu
        2: Rouge
        3: Jaune
        4: Vert
        
    
    Entrée : 
        N: int
        
    Sortie :
        grille: list
    """


def creer_grille_vide(N: int):
    """
    Crée et renvoie une grille 2D vide de taille NxN (vide: valeur 0)
        
    Entrée : 
        N: int
        
    Sortie :
        grille: list
    """


def echanger_bonbons(grille, i1, i2, j1, j2):
    """
    Échange la position dans la grille du bonbon de coordonnées (i1,j1) avec 
    celui de coordonnées (i2, j2), choisis par le joueur (si les coordonnées
    sont valides: à côté l'un de l'autre). Renvoie True si l'échange s'est bien 
    passée, False sinon.

    Entrée:
        grille: list
        i1: int
        i2: int
        j1: int
        j2: int
        
    Sortie:
        état: booléen
    """

    
def detecte_coordonnees_combinaison(grille, i, j):
    """
    Renvoie une liste contenant les coordonnées de tous les bonbons
    appartenant à la combinaison du bonbon (i, j). 
    
    Entrée :
        grille: list
        i : int
        j : int
    
    Sortie :
        liste : list
    """


def explication_jeu():
    """
    Donne des explications sur le fonctionnement du jeu
    """


def affichage_grille(grille, nb_type_bonbons):
    """
    Affiche la grille de jeu "grille" contenant au
    maximum "nb_type_bonbons" couleurs de bonbons différentes.
    """
    
    plt.imshow(grille, vmin=0, vmax=nb_type_bonbons−1, cmap=’jet’)
    plt.pause(0.1)
    plt.draw()
    plt.pause(0.1)


def test_detecte_coordonnees_combinaison():
    """
    Test la fonction detecte_coordonnees_combinaison(grille, i, j).
    Pour chaque cas de test, affiche True si le test passe,
    False sinon
    """
    
    # Test1: Description du cas testé
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


def supprime_bonbons(grille, index):
    """
    Supprime la combinaison de 3 bonbons - remplace les valeurs par 0 et
    augmente les points. 

    Entrée :
        index: list
        grille: list
        
    Sortie : 
        grille: grille 
    """


def descendre_bonbons(grille, index):
    """
    Fait descendre les bonbons déjà existants pour remplir le trou
    laissé par la fonction supprime_bonbons
    
    Entrée:arreter_jeuDecoupageFonctionnel
    """

def remplir_grille(grille):
    """
    Remplit les trous vides de la grille avec des valeurs aléatoires entre 
    1 et 4 aprés avoir utilisé la fonction descendre_bonbons

    Entrée:
        grille: list
    
    Sortie:
        grille: list
    """


def verifier_possibilite(grille):
    """
    Verifie s'il est encore possible d'échanger deux bonbons pour faire une 
    combinaison. S'il est possible, renvoie True. Sinon, renvoie False.

    Entrée:
        grille: liste
        
    Sortie:
        État: booléen
    """