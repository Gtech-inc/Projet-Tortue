from random import *
from turtle import Screen
import turtle


def couleur_aleatoire():
    """
    renvoie un triplet de 3 nombres entier compris entre 0 et 255
    Ce triplet correspond à une couleur codée en RVB
    """
    turtle.colormode(255)
    outputformat = 'RGB' # RGB or return a string
    if outputformat == 'RGB':
        return randint(0,256),randint(0,256),randint(0,256)
    else:
        return choice(['white', 'green', 'blue', 'cyan', 'red', 'yellow', 'orange'])

if __name__ == "__main__":
    print(couleur_aleatoire())
