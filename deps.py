
class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


"""
Class qui contien les infos sur les types
de bonbons (couleur, nom, charactere 
respectif, etc.)
"""
class Bonbon:
    def __init__(self, nom, couleur, ch) -> None:
        self.nom = nom
        self.couleur = couleur
        self.ch = ch
        
    def NOM(self):
        return self.nom
    def COULEUR(self):
        return self.couleur
    def CH(self):
        return self.ch

# Dictionaire qui contien tous les types de bonbons
Bonbons = {
    0: Bonbon('Vide', bcolors.ENDC, ' '),
    1: Bonbon('Bleu', bcolors.BLUE, chr(0x263C)),
    2: Bonbon('Rouge', bcolors.RED, chr(0x2666)),
    3: Bonbon('Jaune', bcolors.YELLOW, chr(0x25D8)),
    4: Bonbon('Vert', bcolors.GREEN, chr(0x25BC))
}