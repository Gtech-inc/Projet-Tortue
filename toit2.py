import turtle
from trait import trait


def toit2(x, y_sol, niveau):
    """
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit plat d'épaisseur 10 pixels et mesurant 140 pixels de large
    """
    turtle.penup()
    niv = niveau * 75
    ordo = niv
    turtle.setposition(x, ordo)
    turtle.pendown()
    absi = x
    # ----Sans boucle----
    turtle.begin_fill()
    turtle.fillcolor("black")
    absi += 140 / 2 - 2
    turtle.setx(absi)
    for i in range(2):  # arrondie inf droit
        ordo += 1
        turtle.sety(ordo)
        absi += 1
        turtle.setx(absi)
    ordo += 5
    turtle.sety(ordo)
    for i in range(3):  # arrondie sup droit
        absi -= 1
        turtle.setx(absi)
        ordo += 1
        turtle.sety(ordo)
    absi -= 140 - 4
    turtle.setx(absi)

    for i in range(3):  # arrondie sup gauche
        absi -= 1
        turtle.setx(absi)
        ordo -= 1
        turtle.sety(ordo)
    ordo -= 5
    for i in range(2):  # arrondie inf gauche
        ordo -= 1
        turtle.sety(ordo)
        absi += 1
        turtle.setx(absi)
    turtle.sety(ordo)
    absi += 140 / 2
    turtle.setx(absi)
    turtle.end_fill()
    turtle.penup()


if __name__ == '__main__':
    toit2(0, 0, 2)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
