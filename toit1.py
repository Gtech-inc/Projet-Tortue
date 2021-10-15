import turtle


def toit1(x, y_sol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit triangulaire noir de base 160 pixels
    et de hauteur centrale 40 pixels
    etage : 75 de hauteur
    '''
    turtle.penup()
    niv = niveau * 75
    ordo = niv
    turtle.setposition(x, ordo)
    turtle.pendown()
    absi = x
    ordo = niv
    # ----Sans boucle----
    turtle.begin_fill()
    turtle.fillcolor("black")
    absi += 80
    turtle.setx(absi)
    absi -= 80
    ordo += 40
    turtle.setposition(absi, ordo)
    absi -= 80
    ordo -= 40
    turtle.setposition(absi, ordo)
    absi += 80
    turtle.setx(absi)
    absi -= 80
    turtle.setposition(absi, ordo)

    turtle.end_fill()
    turtle.penup()


if __name__ == '__main__':
    toit1(0, 0, 0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
