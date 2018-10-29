#!/usr/bin/python3

# La fonction affiche les nombres de 1 à 9

def constructGrille():
    i = 1
    for nLigne in range(3):
        ligne=[]
        for nColonne in range(3):
            ligne.append(i)
            i = i + 1
        grille.append(ligne)

def afficheGrille():
    for nLigne in range(3):
        for nColonne in range(3):
            print(grille[nLigne][nColonne], end=' ')
        print('\n', end='')

grille = []

constructGrille()

afficheGrille()

#Pour faire jouer les deux joueurs regarde la récursivité: https://www.lucaswillems.com/fr/articles/17/recursivite-accelerer-algorithmes

a = 0
#while true un classique, permet de relancer du code à gogo, par exemple tant que la partie est pas terminé.
while True:
    print(a)
    a = a + 1
    #pour demander une entré au joueur
    data = input("Joueur X joue: ")
    print(data)

    #La condition de sortie du code, a toi de trouver laquelle mettre
    if a > 10:
        break

#Good luck


