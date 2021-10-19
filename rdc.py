from random import randint
from facade import facade
from porte import porte
from porte2 import porte2
from fenetre import fenetre
from trait import trait
import turtle


def rdc(x, y_sol, c_porte, c_facade):
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
    facade(x, y_sol, c_facade)

    x += 25
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y_sol)

    randomNumber = randint(0, 2)
    
    if randomNumber == 0:
        randomDoor = randint(0, 1)
        if randomDoor == 0:
            porte(x, y_sol, c_porte)
        else:
            porte2(x, y_sol, c_porte)
        x += 50
        fenetre(x, y_sol + 20)
        x += 50
        fenetre(x, y_sol + 20)

    elif randomNumber == 1:
        fenetre(x, y_sol + 20)
        x += 50
        randomDoor = randint(0, 1)
        if randomDoor == 0:
            porte(x, y_sol, c_porte)
        else:
            porte2(x, y_sol, c_porte)
        x += 50
        fenetre(x, y_sol + 20)
    
    elif randomNumber == 2:
        fenetre(x, y_sol + 20)
        x += 50
        fenetre(x, y_sol + 20)
        x += 50
        randomDoor = randint(0, 1)
        if randomDoor == 0:
            porte(x, y_sol, c_porte)
        else:
            porte2(x, y_sol, c_porte)
         
    


if __name__ == '__main__':
    rdc(0, 0, "grey", "red")
    # On ferme la fenêtre si il y a un clique gauche
    turtle.exitonclick()
