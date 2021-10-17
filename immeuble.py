# module immeuble
from couleur_aleatoire import couleur_aleatoire
from rdc import rdc
from toit import toit
import turtle
from random import randint
from etage import etage


def immeuble(x, y_sol):
    """
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
    Cette fonction dessine un immeuble Le nombre d'étage est compris aléatoirement entre 0 et 4
    La couleur de la façade et la couleur de la porte sont tirées au hasard
    """
    # Nombre d'étage (aléatoire)
    nbStage = randint(0, 5)

    # Couleurs des éléments (aléatoire)
    
    couleur = couleur_aleatoire()
    couleurPorte = "grey"

    # Dessin du RDC
    rdc(x, y_sol, couleurPorte, couleur)
    y_sol += 75

    # Dessin des étages
    for niveau in range(nbStage):
        etage(x, y_sol, couleur, niveau)
        y_sol += 75

    # Dessin du toit
    
    toit(x+75, 20, nbStage)

if __name__ == '__main__':
    immeuble(0, 0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
