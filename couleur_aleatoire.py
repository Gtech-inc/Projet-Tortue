import turtle
from random import randint


def couleur_aleatoire():
    """
    renvoie un triplet de 3 nombres entier compris entre 0 et 255
    Ce triplet correspond à une couleur codée en RVB
    """
    listcolors = [""]
    turtle.colormode(255)
    return randint(0, 255), randint(0, 255), randint(0, 255)