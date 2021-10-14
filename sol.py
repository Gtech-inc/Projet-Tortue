# Module par sebastien

import turtle
from trait import trait


# ----- Sol de la rue -----
def sol(y_sol):
    """
    Paramètres
        y_sol : ordonnée du sol du la rue
    Cette fonction dessine un trait horizontale de 3 pixels d' épaisseur
    """
    if not turtle.isdown():
        turtle.pendown()
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(-380, y_sol-300)
    turtle.pendown()
    turtle.goto(380, y_sol-300)


if __name__ == '__main__':
    sol(0)
    # On ferme la fenêtre si il y a un clique gauche
    turtle.exitonclick()
