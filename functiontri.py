#fonction 11.5


def functri(source, chars):
    """retourner un texte source sans les caracteres presents dans le parametre chars
    source : string
    chars : liste de chaine (["a","b",...])
    """
    compteur = 0
    resultat = ""
    for caractere in source:
        if caractere in chars:
            print("1 caracteres supprimés")
            compteur += 1
        else:
            resultat = resultat + caractere
    return (resultat, compteur)
    



if __name__ == "__main__":
    caracteres_supprimes = input("quelles lettres du texte doivent etre ecartées  ?")
    print(caracteres_supprimes)
    caracteres_supprimes = list(caracteres_supprimes)
    print(caracteres_supprimes)

    fichier = open("test.txt", "r")
    text_source = fichier.read()
    fichier.close()

    print(text_source)

    texte, compteur = functri(text_source, caracteres_supprimes)

    print(texte)
    print(compteur)

    fichier = open("test_out.txt", "w")
    fichier.write(texte)
    fichier.close()