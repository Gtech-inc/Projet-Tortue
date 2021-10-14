from rectangle import rectangle
import turtle

def fenetre(x,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la fenêtre
        y est l'ordonnée du sol du niveau de la fenetre
    Remarque:
        dessine une fenetre de 30 pixels sur 30 pixels

    '''
    turtle.setposition(x,y)
    turtle.pendown()
    absi = x
    ordo = y
    #----Sans boucle----
    turtle.begin_fill()
    turtle.fillcolor("grey")
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
    absi -= 15
    turtle.setposition(absi, ordo)
    turtle.end_fill()
    turtle.penup()
    pass

if __name__ == '__main__':
    fenetre(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
