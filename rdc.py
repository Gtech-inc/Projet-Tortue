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
    doorDrown = False
    windowdrown = 0
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y_sol)
    randomNumber = randint(0, 2)

    if randomNumber == 0 and windowdrown == False:
        fenetre(x, y_sol + 20)
        windowdrown = 1
    elif randomNumber == 1 and doorDrown == False:
        porte(x, y_sol, c_porte)
        doorDrown = True
    else:
        porte2(x, y_sol, c_porte)
        doorDrown = True

    turtle.penup()
    turtle.setx(x)
    turtle.sety(y_sol)

    for i in range(2):
        turtle.end_fill()
        randomNumber = randint(0, 2)
        x += 50
        turtle.penup()
        turtle.setx(x)
        turtle.sety(y_sol)
        turtle.begin_fill()
    
        if randomNumber == 0 and windowdrown != 2:
            fenetre(x, y_sol + 20)
            windowdrown += 1
        
        elif randomNumber == 1 and doorDrown == False:
            randomNumber = randint(0, 1)
            if randomNumber == 0:
                porte(x, y_sol, c_porte)
                doorDrown = True
            elif randomNumber == 1:
                porte2(x, y_sol, c_porte)
                doorDrown = True

        if i == 2 and doorDrown == False:
            randomNumber = randint(0, 1)
            if randomNumber == 0:
                porte(x, y_sol, c_porte)
                doorDrown = True
            elif randomNumber == 1:
                porte2(x, y_sol, c_porte)
                doorDrown = True
        
        if i == 1 and windowdrown != 2:
            fenetre(x, y_sol + 20)
            windowdrown += 1

        if i == 2 and windowdrown != 2:
            fenetre(x, y_sol + 20)
            windowdrown += 1

        # if randomNumber == 0:
        #     fenetre(x, y_sol + 20)
        #     windowdrown += 1
        # if randomNumber == 1 and doorDrown == False:
        #     porte(x, y_sol, c_porte)
        #     doorDrown = True
        # elif randomNumber == 1 and windowdrown != 2 and doorDrown == True:
        #     fenetre(x, y_sol + 20)
        # elif randomNumber == 2 and doorDrown == False:
        #     porte2(x, y_sol, c_porte)
        #     doorDrown = True
        # elif i == 1 and doorDrown == False:
        #     if randomNumber == 1 and doorDrown == False:
        #         porte(x, y_sol, c_porte)
        #         doorDrown = True
        #     elif randomNumber == 2 and doorDrown == False:
        #         porte2(x, y_sol, c_porte)
        #         doorDrown = True
         
        turtle.penup()


if __name__ == '__main__':
    rdc(0, 0, "grey", "red")
    # On ferme la fenêtre si il y a un clique gauche
    turtle.exitonclick()
