from facade import facade
from random import shuffle,randint
from fenetre import fenetre
from fenetre_balcon import fenetre_balcon
import turtle

def etage(x, y_sol, couleur, niveau):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade de l'étage
        niveau : numéro de l'étage en partant de 0 pour le rdc
    Remarque
       Cette fonction dessine un étage d'un immeuble
    '''
    # dessin des murs
    facade(x, y_sol, couleur, niveau)

    y_sol += 10
    x += 25
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y_sol)

    fenetre(x, y_sol + 20)
    x += 50
    fenetre(x, y_sol + 20)
    x += 50
    fenetre_balcon(x, y_sol)

    print("x = " + str(x))
    print("y = " + str(y_sol))
    
    # dessin des 3 Eléments
    pass

if __name__ == '__main__':
    etage(0,0,"red",0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()