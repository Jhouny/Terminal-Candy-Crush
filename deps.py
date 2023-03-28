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
                chr(0x263C), # Bleuquitter
                chr(0x2666), # Rouge
                chr(0x25D8), # Jaune
                chr(0x25BC), # Vert
                ]

commandes = ['quitter',
             'taille',
             'commencer',
             'echanger',
             'redemarrer']

explications = ["Quitter le jeu si pendant une partie, sinon ferme le programme",
                "Definir la taille du tableau",
                "Commencer la partie",
                "Echanger la position de deux bonbons (e.g. echanger i1,j1 i2,j2)",
                "Redemarrer la partie en cours",
                ]


def explication_jeu():
    """
    Donne des explications sur le fonctionnement du jeu dans la lague choisi
    """
    print("Bienvenue dans ce merveilleux jeu\"Candy Crush\"!!")
    print("\nObjectif du jeu: ")
    print("Dans un temps défini par le joueur, l'objectif est de marquer des points en échangeant de position les bonbons")
    print("\nRègles du jeu: ")
    print("\t1. Une combinaison est possible si 3 bonbons de la même couleur ou plus sont alignés verticalement ou horizontalement")
    print("\t2. Pour créer cette combinaison, le joueur peut échanger un bonbon avec l'un de ses voisins")
    print("\t3. Mais attention!!! C'est possible seulement si le changement crée une combinaison")
    print("\t4. Chaque combinaison realisée donne des points en fonction du nombre de bonbons")
    print("\t5. S'il n'y a plus de combinaison possibles, le jeu finira")

    print("Bienvenido a este maravilloso juego \"Candy Crush\"!!")
    print("\nObjetivo del juego: ")
    print("En un tiempo definido por el jugador, el objetivo es de conseguir puntos intercambiando las posiciones de los dulces ")
    print("\nReglas del juego: ")
    print("\t1. Una combinación es posible si tres o más dulces están alineados vertical u horizontalmente")
    print("\t2. Para crear esta combinación, el jugador puede intercambiar un dulce con uno de sus vecinos")
    print("\t3. ¡¡¡Pero cuidado!!! Es posible solamente si el intercambio crea una combinación")
    print("\t4. Cada combinación realizada da puntos en función del número de dulces")
    print("\t5. Si no hay más combinaciones posibles, el juego terminará")
    
    print("Bem-vindo a este maravilhoso jogo \"Candy Crush\"!!")
    print("\nObjetivo do jogo: ")
    print("Marcar pontos mudando as posições dos doces, em um tempo limite definido pelo jogador")
    print("\nRegras do jogo: ")
    print("\t1. Temos uma combinação quando três ou mais doces estão alinhados horizontalmente ou verticalmente")
    print("\t2. Para criar esta combinação, o jogador pode mudar um doce com um dos seus vizinhos")
    print("\t3. Mas cuidado!!! Só é permitido se a mudança criar uma combinação")
    print("\t4. Cada combinação realisada dá pontos em função do número de doces")
    print("\t5. Se não há mais combinações possíveis, o jogo terminará")
    