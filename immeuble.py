# module immeuble

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
<<<<<<< HEAD
    '''
    turtle.setx(x)
    turtle.sety(y_sol)
    # Nombre d'étage (aléatoire)
    nbStage = randint(0, 7)

    #Couleurs des éléments (aléatoire)
    couleur = couleur_aleatoire()
=======
    """
    # Nombre d'étage (aléatoire)
    nbStage = randint(0, 7)

    # Couleurs des éléments (aléatoire)
    turtle.colormode(255)
    color1 = 244

    couleur = turtle.color(color1)
>>>>>>> 6856f838d3dd33cea2eece4e993b52006c651a19

    # Dessin du RDC

    # Dessin des étages
<<<<<<< HEAD
    y_sol= -200
    x = -300
    for niveau in range(nbStage):
        etage(x, y_sol, couleur, niveau)
        y_sol += 75
=======
    y = -200
    x = -300
    for niveau in range(nbStage):
        etage(x, y_sol, couleur, niveau)
        y += 75
>>>>>>> 6856f838d3dd33cea2eece4e993b52006c651a19

    # Dessin du toit
    
    toit(x+75, 0, nbStage)

if __name__ == '__main__':
    immeuble(0, 0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
