# module immeuble

from couleur_aleatoire import couleur_aleatoire
from random import randint
from rdc import rdc
from etage import etage
from toit import toit
import turtle

def immeuble(x, y_sol):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
    Cette fonction dessine un immeuble Le nombre d'étage est compris aléatoirement entre 0 et 4
    La couleur de la façade et la couleur de la porte sont tirées au hasard
    '''
    # Nombre d'étage (aléatoire)
    nbStage = randint(0, 7)

    #Couleurs des éléments (aléatoire)
    turtle.colormode(255)
    color1 = 244

    couleur = turtle.color(color1)

    # Dessin du RDC
    

    # Dessin des étages
    y= -200
    x = -300
    for niveau in range(nbStage):
        etage(x, y_sol, couleur, niveau)
        y+= 75

    # Dessin du toit


if __name__ == '__main__':
    immeuble(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()