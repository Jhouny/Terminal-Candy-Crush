WARNING = '\033[91m'
JAUNE = '\033[93m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

CouleursBonbons = ['\033[0m',  # Vide
                   '\033[94m', # Bleu
                   '\033[91m', # Rouge
                   '\033[93m', # Jaune
                   '\033[92m', # Vert
                  ]

CharsBonbons = [' ',         # Vide
                chr(0x263C), # Bleu
                chr(0x2666), # Rouge
                chr(0x25D8), # Jaune
                chr(0x25BC), # Vert
                ]

commandes = ['quitter',
             'taille',
             'commencer',
             'echanger',
             'redemarrer',
             'niveau']

explications = ["Quitter le jeu si pendant une partie, sinon fermer le programme",
                "Definir la taille du tableau de n lignes et colonnes (ex: taille 6)",
                "Commencer la partie",
                "Echanger la position de deux bonbons (ex : echanger i1,j1 i2,j2)",
                "Redemarrer la partie en cours",
                "Change le niveau du jeu (1, 2 ou 3) (ex: niveau 2)"]


def explication_jeu(langue):
    """
    Donne des explications sur le fonctionnement du jeu dans la langue choisi

    """

    if langue.lower() == "es" :
        print("Bienvenido a este maravilloso juego \"Candy Crush\"!!")
        print("\nObjetivo del juego: ")
        print("En un nivel definidos por el jugador, el objetivo es de conseguir puntos intercambiando las posiciones de los dulces ")
        print("\nReglas del juego: ")
        print("\t1. Dependiendo del nivel escogido por el jugador, una combinación puede ser realizada de diferentes maneras")
        print("\t2. Para crear esta combinación, el jugador puede intercambiar un dulce con uno de sus vecinos")
        print("\t3. ¡¡¡Pero cuidado!!! Es posible solamente si el intercambio crea una combinación")
        print("\t4. Cada combinación realizada da puntos en función del número de dulces")
        print("\t5. Si no hay más combinaciones posibles, el juego terminará")
        print("\nNiveles del juego: ")
        print("\tNivel 1: Eliminamos solamente las combinaciones de 3 dulces del mismo color alineados vertical u horizontalmente. Así, si 4 dulces están alineados, solamente 3 son eliminados")
        print("\tNivel 2: Eliminamos todos los dulces del mismo color que están alineados horizontal o verticalmente, con un mínimo de 3 dulces.")
        print("\tNivel 3: Si al menos 3 dulces están alineados horizontal o verticalmente, entonces eliminamos todos los dulces del mismo color que se acerquen a un dulce eliminado")

    elif langue.lower() == "pt" :

        print("Bem-vindo a este maravilhoso jogo \"Candy Crush\"!!")
        print("\nObjetivo do jogo: ")
        print("Marcar pontos mudando as posições dos doces, em um nivel limite definido pelo jogador")
        print("\nRegras do jogo: ")
        print("\t1. Temos uma combinação quando três ou mais doces estão alinhados horizontalmente ou verticalmente")
        print("\t2. Para criar esta combinação, o jogador pode mudar um doce com um dos seus vizinhos")
        print("\t3. Mas cuidado!!! Só é permitido se a mudança criar uma combinação")
        print("\t4. Cada combinação realisada dá pontos em função do número de doces")
        print("\t5. Se não há mais combinações possíveis, o jogo terminará")
        print("\nNivel de jogo: ")
        print("\tNivel 1 : So eliminamos os combinaçoes de 3 doces da mesma cor alinhados verticalmente ou horizontalmente. Por isso, se temos 4 doces alinhados, apenas 3 são eliminados")
        print("\tNivel 2 : Eliminamos todos os doces da mesma cor alinhados verticalmente ou horizontalmente com um minimo de 3 doces.")
        print("\tNivel 3 : Se pelo menos 3 doces estiverem alinhados (verticalmente ou horizontalmente), então eliminamos todos os doces da mesma cor que são vizinhos dum doce eliminado")
    else : 
        print("Bienvenue dans ce merveilleux jeu\"Candy Crush\"!!")
        print("\nObjectif du jeu: ")
        print("Dans un niveau définis par le joueur, l'objectif est de marquer des points en échangeant de position les bonbons")
        print("\nRègles du jeu: ")
        print("\t1. Selon le niveau choisi par le joueur, une combinaison peut se faire de différentes manières")
        print("\t2. Pour créer cette combinaison, le joueur peut échanger un bonbon avec l'un de ses voisins")
        print("\t3. Mais attention!!! C'est possible seulement si le changement crée une combinaison")
        print("\t4. Chaque combinaison realisée donne des points en fonction du nombre de bonbons")
        print("\t5. S'il n'y a plus de combinaison possible, le jeu finira")
        print("\nNiveaux du jeu: ")
        print("\tNiveau 1: On supprime seulement des combinaisons de 3 bonbons de même couleur alignés verticalement ou horizontalement. Ainsi, si 4 bonbons sont alignés, seulement 3 sont supprimés")
        print("\tNiveau 2: On supprime tous les bonbons de même couleur qui sont alignés horizontalement ou verticalement, avec un minimum de 3 bonbons.")
        print("\tNiveau 3: Si au moins 3 bonbons sont alignés (verticalement ou horizontalement), alors on supprime tous les bonbons de même couleur qui sont voisins d’un bonbon supprimé (un des 3 bonbons d’origine, ou un voisins de voisin)")