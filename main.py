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
    y_sol = -250
    x = -380
    # Dessin du sol de la rue
    sol(y_sol)
    # Dessin des 4 immeubles
    turtle.pensize(0)
    for i in range(4):
        immeuble(x, y_sol)
        turtle.setx(x)
        x += 200
    


    # On ferme la fenêtre si il y a un clique gauche
    turtle.exitonclick()


if __name__ == '__main__':
    main()
