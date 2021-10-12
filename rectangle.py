import turtle


def rectangle(x: int, y: int, w: int, h: int):
    """
    Paramètres
        x, y : coordonnées du centre de la base de rectangle
        w : largeur du rectangle
        h : hauteur du rectangle
    Cette fonction dessine un rectangle Le point de coordonnées (x,y) est
    sur le côté en bas au milieu
    """
    if turtle.isdown():
        turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.goto(x + w, y)
    turtle.goto(x + w, y - h)
    turtle.goto(x, y - h)
    turtle.goto(x, y)
    turtle.penup()


if __name__ == '__main__':
    rectangle(0, 0, 150, 100)
    # On ferme la fenêtre si il y a un clique gauche
    turtle.exitonclick()
