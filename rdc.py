import random

import porte2
from facade import facade
from porte import porte
from fenetre import fenetre
from trait import trait
import turtle


def rdc(x, y_sol, c_facade, c_porte):
    """
    Paramètres
        x : (int) abscisse du centre
        y_sol : ordonnée du sol du la rue
        c_facade : couleur de la façade
        c_porte : couleur de la porte
    remarque:
        Cette fonction dessine le rdc en 2 étapes
        D' abord la façade
        Puis les 3 éléments : 1 porte et 2 fenêtres disposées au hasard
    """
    # Dessine la facade
    if not turtle.isdown():
        turtle.pendown()
    turtle.fillcolor(c_facade)
    turtle.begin_fill()
    trait(x-(140/2), y_sol, x+(140/2), y_sol)
    trait(x+(140/2), y_sol, x+(140/2), y_sol+60)
    trait(x+(140/2), y_sol+60, x-(140/2), y_sol+60)
    trait(x-(140/2), y_sol+60, x-(140/2), y_sol)
    turtle.end_fill()
    # Construit les 3 éléments (1 porte et 2 fenêtres)
    length = 140/4
    is_door = False
    for i in range(1, 4):
        choice = random.choice(['Door', 'Window'])
        if choice == 'Door':
            if not is_door:
                style = random.choice(['porte', 'porte2'])
                if style == 'porte':
                    porte(length*i, y_sol+(50/2), c_porte)
                else:
                    porte2.porte2(length*i, y_sol+(50/2), c_porte)
            else:
                fenetre(length*i, y_sol+())
        else:
            fenetre(length*i, y_sol+())


if __name__ == '__main__':
    rdc(0, 0, "red", "green")
    # On ferme la fenêtre si il y a un clique gauche
    turtle.exitonclick()
