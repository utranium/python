#pacman

def trace_mon_tableau (hauteur, largeur):
    #hauteur : int : hauteur du tableau
    #largeur : int : largueur du tableau
    #tableau : dictionnaire a remplir
    #la fonction creer un tableau avec bordures grace aux sprites contenus dans la liste_mur


    #augmentation de la matrice pour la prise en compte des murs
    largeur, hauteur = largeur+2, hauteur+2
    tableau = {}

    
    #avec une boucle for, creation d'un tableau sous forme de dictionaire dans un dictionaire pour un systeme d'abcisses et ordonnées.
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

    return tableau







if __name__ == "__main__":

    #je demande a l'utilisateur une dimension

    largeur = int(input("donnez moi une largeur"))
    hauteur = int(input("donnez moi une hauteur"))

    tableau = trace_mon_tableau (hauteur, largeur)

    

    #tracé du tableau
    for compteur_hauteur in range((hauteur)+2):
        print("\n")
        for compteur_largeur in range((largeur)+2):
            print(tableau[compteur_hauteur,compteur_largeur],end="")