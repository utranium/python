#pacman










if __name__ == "__main__":

    #je demande a l'utilisateur une dimension

    largeur = int(input("donnez moi une largeur"))
    hauteur = int(input("donnez moi une hauteur"))
    tableau = {}

    #augmentation de la matrice pour la prise en compte des cotés
    largeur, hauteur = largeur+2, hauteur+2

    
    #avec une boucle for, je creer un tableau sous forme de dictionaire dans un dictionaire
    for compteur_hauteur in range(hauteur):
        for compteur_largeur in range(largeur):
            tableau[compteur_hauteur,compteur_largeur] = [" "]


    #mes murs sont disponibles sous forme de liste
    liste_murs = ['╔', ' === ', '╗', '║', '╚', '╝']

    #bordures horizontale
    for ligne in range(largeur):
        tableau[0,ligne] = tableau[(hauteur-1),ligne] = liste_murs[1]
    #bordures verticale
    for colonne in range(hauteur):
        tableau[colonne,0] = tableau[colonne,(largeur-1)] = liste_murs[3]

    #Extremitees du tableau
    tableau[0,0] = liste_murs[0]
    tableau[0,(largeur-1)] = liste_murs[2]
    tableau[(hauteur-1),(largeur-1)] = liste_murs[5]
    tableau[(hauteur-1),0] = liste_murs[4]

    #tracé du tableau
    for compteur_hauteur in range(hauteur):
        print("\n")
        for compteur_largeur in range(largeur):
            print(tableau[compteur_hauteur,compteur_largeur],end="")