import turtle
from rectangle import rectangle


def facade(x, y_sol, couleur, niveau):
    """
    Paramètres :
        x : abscisse du centre de la façade
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade
        niveau : num du niveau (0 pour les rdc, ...)
    remarque :
<<<<<<< HEAD
        Facade dessine une facade sans les élements interieurs
    '''
    turtle.penup()
=======
        Facade dessine une facade sans les éléments intérieurs
    """
    turtle.begin_fill()
>>>>>>> 6856f838d3dd33cea2eece4e993b52006c651a19
    turtle.fillcolor(couleur)
    turtle.setx(x)
    turtle.sety(y_sol)
    turtle.begin_fill()
    turtle.pendown()
    for i in range(2):
        turtle.forward(150)
        turtle.left(90)
        turtle.forward(75)
        turtle.left(90)

    turtle.end_fill()
<<<<<<< HEAD
    turtle.penup()
    
    
    pass
=======

>>>>>>> 6856f838d3dd33cea2eece4e993b52006c651a19

if __name__ == '__main__':
    facade(0, 0, "red", 0)
    # On ferme la fenêtre si il y a un clique gauche
    turtle.exitonclick()
