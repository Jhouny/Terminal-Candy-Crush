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

explications = ["Quitte le jeu si pendant une partie, sinon ferme le programme",
                "Defini la taille du tableau",
                "Commence la partie",
                "Echange la position de deux bonbons (e.g. echanger i1,j1 i2,j2)",
                "Redemarre la partie en cours",
                ]
