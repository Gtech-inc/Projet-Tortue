from facade import facade
from random import randint
from fenetre import fenetre
from fenetre_balcon import fenetre_balcon
import turtle


def etage(x, y_sol, couleur, niveau):
    """
    Paramètres
        x : abscisse du centre de l' étage
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade de l' étage
        niveau : numéro de l' étage en partant de 0 pour le rdc
    Remarque
       Cette fonction dessine un étage d' un immeuble
    """
    # dessin des murs
    facade(x, y_sol, couleur)

    y_sol += 10
    x += 25
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y_sol)

    if randint(0, 1) == 0:
        fenetre(x, y_sol + 20)
    else:
        fenetre_balcon(x, y_sol)

    turtle.penup()
    for i in range(2):
        x += 50
        if randint(0, 1) == 0:
            fenetre(x, y_sol + 20)
        else:
            fenetre_balcon(x, y_sol)
        turtle.penup()


if __name__ == '__main__':
    etage(0, 0, "red", 0)
    # On ferme la fenêtre si il y a un clique gauche
    turtle.exitonclick()
