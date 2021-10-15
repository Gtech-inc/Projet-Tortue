import  turtle

def porte2(x,y,couleur):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte
        y est l'ordonnée du sol du niveau de la porte
        couleur : couleur de la porte
    remarque:
        Cette fonction dessine une porte dont le haut est un demi cercle
        La porte a une largeur totale de 30 pixels
        La partie rectangulaire a une hauteur de 40 pixels
        La partie semi circulaire a un rayon de 15 pixels
    '''
    turtle.begin_fill()
    turtle.fillcolor(couleur)
    x += 30
    turtle.setx(x)
    y += 50
    turtle.sety(y)

    for i in range(30):
        coef = 0.88 *i
        x -= 1
        y += 1 - coef *0.08
        turtle.setx(x)
        turtle.sety(y)

    # for i in range(15):
    #     x -= 1
    #     y -= 1 + i * 0.1
    #     turtle.setx(x)
    #     turtle.sety(y)

    y -= 50
    turtle.sety(y)
    turtle.setposition(x, y)
    turtle.end_fill()
    turtle.penup()
    pass



if __name__ == '__main__':
    porte2(0,0,"red")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()