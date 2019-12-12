# Avec une boucle FOR
def traitement(a_remplacer, remplacant, fichier):
    content = ""
    with open(fichier, 'r') as fichier_only:
        for line in fichier_only.readlines():
            line = line.replace(a_remplacer, remplacant)
            content += line

    with open(fichier, 'w') as fichier_only:
        fichier_only.write(content)

if __name__ == '__main__':
    # parcours des fichiers dans une boucle for
    for fichier in ('fichier1.txt', 'fichier2.txt', 'fichiern.txt'):
        traitement('toto', 'tata', fichier)
