from rectangle import rectangle
import turtle


def fenetre(x, y):
    """
    Paramètres :
        x est l' abscisse du centre de la fenêtre
        y est l' ordonnée du sol du niveau de la fenêtre
    Remarque:
        dessine une fenêtre de 30 pixels sur 30 pixels

    """
    turtle.setx(x)
    turtle.sety(y)
    absi = x
    ordo = y
    turtle.begin_fill()
    turtle.fillcolor("grey")
    turtle.pendown()
    # ----Sans boucle----
    absi += 15
    turtle.setx(absi)
    ordo += 30
    turtle.sety(ordo)
    absi -= 30
    turtle.setx(absi)
    ordo -= 30
    turtle.sety(ordo)
    absi += 15
    turtle.setx(absi)
    turtle.end_fill()
    turtle.penup()


if __name__ == '__main__':
    fenetre(0, 0)
    # On ferme la fenêtre si il y a un clique gauche
    turtle.exitonclick()
