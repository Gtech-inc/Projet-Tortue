import turtle
from rectangle import rectangle


def porte(x, y, couleur):
    """
    Paramètres :
        x est l'abcisse du centre de la porte
        y est l'ordonnée du sol du niveau de la porte
        couleur : couleur de la porte
    remarque:
        Cette fonction dessine une porte de 30 pixels de large pour 50 pixels de hauteur
    """
    turtle.end_fill()
    turtle.penup()
    turtle.setposition(x, y)
    x += 15
    y += 50
    turtle.setx(x)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(couleur)
    turtle.sety(y)
    x -= 30
    turtle.setx(x)
    y -= 50
    turtle.sety(y)
    x += 30
    turtle.setx(x)
    turtle.end_fill()
    turtle.penup()
    turtle.setposition(x, y)


if __name__ == '__main__':
    porte(0, 0, "red")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
