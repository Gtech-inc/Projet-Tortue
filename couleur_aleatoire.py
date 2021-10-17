from random import *
import turtle


def couleur_aleatoire():
    """
    renvoie un triplet de 3 nombres entier compris entre 0 et 255
    Ce triplet correspond à une couleur codée en RVB
    """
    outputformat = 'test' # RGB or return a string
    if outputformat == 'RGB':
        RGB = (randint(0,256),randint(0,256),randint(0,256))
        return RGB
    else:
        return choice(['white', 'green', 'blue', 'cyan', 'red', 'yellow', 'orange'])

if __name__ == "__main__":
    print(couleur_aleatoire())
    RGB = (randint(0,256),randint(0,256),randint(0,256))
    print(RGB)
