from random import *
import turtle


def couleur_aleatoire():
    """
    renvoie un triplet de 3 nombres entier compris entre 0 et 255
    Ce triplet correspond à une couleur codée en RVB
    """
    colors = ['white', 'green', 'blue', 'cyan', 'red', 'yellow', 'orange']
    return colors[randint(0, len(colors) - 1)]
