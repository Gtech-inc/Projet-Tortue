import turtle
from rectangle import rectangle
from trait import trait


def fenetre_balcon(x, y):
    """
    Paramètres :
        x est l'abcisse du centre de la porte-fenetre-balcon
        y est l'ordonnée du sol du niveau de la porte-fenetre-balcon
    Remarque:
        Dessine une porte-fenetre avec balcon en 2 temps: la porte fenetre de 30 pixels de large par 50 pixels de hauteur
        puis le balcon
    """
    # porte-fenetre

    turtle.setposition(x, y)
    turtle.pendown()
    absi = x
    ordo = y
    # ----Sans boucle----
    turtle.begin_fill()
    turtle.fillcolor("grey")
    absi += 15
    turtle.setx(absi)
    ordo += 50
    turtle.sety(ordo)
    absi -= 30
    turtle.setx(absi)
    ordo -= 50
    turtle.sety(ordo)
    absi += 15
    turtle.setx(absi)
    absi -= 15
    turtle.setposition(absi, ordo)
    turtle.end_fill()
    turtle.penup()


    # balcon

    absi -= 5  # se décale pour faire le balcon
    setwidth = 2  # Set la largeur du trait
    turtle.setpos(absi, ordo)
    turtle.pensize(setwidth)
    for i in range(8):
        turtle.pendown()
        if turtle.isdown:
            ordo += 25
            turtle.sety(ordo)
            absi += 5
            turtle.setx(absi)
            ordo -= 25
            turtle.sety(ordo)
            absi -= 5
            turtle.setx(absi)
        absi += 5
        turtle.setx(absi)

    # reinitialisation de la taille du crayon
    turtle.pensize(0)


if __name__ == '__main__':
    fenetre_balcon(0, 0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
