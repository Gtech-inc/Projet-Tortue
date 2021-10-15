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
    turtle.setx(x)
    turtle.sety(y_sol)
    # Nombre d'étage (aléatoire)
    nbStage = randint(0, 7)

    #Couleurs des éléments (aléatoire)
    couleur = couleur_aleatoire()

    # Dessin du RDC
    

    # Dessin des étages
    y_sol= -200
    x = -300
    for niveau in range(nbStage):
        etage(x, y_sol, couleur, niveau)
        y_sol += 75

    # Dessin du toit
    
    toit(x+75, 0, nbStage)

if __name__ == '__main__':
    immeuble(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()