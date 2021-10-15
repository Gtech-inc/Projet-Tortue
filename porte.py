import turtle
from rectangle import rectangle

def porte(x,y,couleur):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte
        y est l'ordonnée du sol du niveau de la porte
        couleur : couleur de la porte
    remarque:
        Cette fonction dessine une porte de 30 pixels de large pour 50 pixels de hauteur
    '''
    turtle.begin_fill()
    turtle.fillcolor(couleur)
    x += 15
    turtle.setx(x)
    y += 50
    turtle.sety(y)
    x -= 30
    turtle.setx(x)
    y -= 50
    turtle.sety(y)
    x += 15
    turtle.setx(x)
    x -= 15
    turtle.setposition(x, y)
    turtle.end_fill()
    turtle.penup()
    pass


if __name__ == '__main__':
    porte(0,0,"red")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
