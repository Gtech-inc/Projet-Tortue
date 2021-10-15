import turtle
from sol import sol
from immeuble import immeuble
from random import randint


# ------------------------------
# ------------------------------
# ------------------------------

def main():
    turtle.setup(800, 600)
    turtle.speed(0)
    # On définit la hauteur du sol
    y_sol = -200
    x = -380
    # Dessin du sol de la rue
    sol(y_sol)
    # Dessin des 4 immeubles
    turtle.setposition(x, y_sol)
    for i in range(randint(1,4)):
        x += 28
        turtle.setx(x)
        immeuble()


    # On ferme la fenêtre si il y a un clique gauche
    turtle.exitonclick()


if __name__ == '__main__':
    main()
