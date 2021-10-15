import turtle


def toit1(x, y_sol, niveau):
    """
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit triangulaire noir de base 160 pixels
    et de hauteur centrale 40 pixels
    etage : 75 de hauteur
    """
    turtle.penup()
    y_sol = -200 + niveau * 75 + y_sol
    turtle.setposition(x, y_sol)
    turtle.pendown()
    absi = x
<<<<<<< HEAD
    #----Sans boucle----
=======
    ordo = niv
    # ----Sans boucle----
>>>>>>> 6856f838d3dd33cea2eece4e993b52006c651a19
    turtle.begin_fill()
    turtle.fillcolor("black")
    absi += 80
    turtle.setx(absi)
    absi -= 80
    y_sol += 40
    turtle.setposition(absi, y_sol)
    absi -= 80
    y_sol -= 40
    turtle.setposition(absi, y_sol)
    absi += 80
    turtle.setx(absi)
    absi -= 80
    turtle.setposition(absi, y_sol)

    turtle.end_fill()
    turtle.penup()


if __name__ == '__main__':
    toit1(0, 0, 0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
