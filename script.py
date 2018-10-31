#!/usr/bin/python3
# coding: utf-8

def reset():
    grille = []
    loop = 0
    constructGrille()

def constructGrille():
    grille = []
    i = 1
    for nLigne in range(3):
        ligne=[]
        for nColonne in range(3):
            ligne.append("*")
            i = i + 1
        grille.append(ligne)
    return grille

def afficheGrille(grille):
    for nLigne in range(3):
        for nColonne in range(3):
            print(grille[nLigne][nColonne], end=' ')
        print('\n', end='')

def play(player, grille):
    l = int(input("Joueur "+str(player)+" joue, entré la ligne: "))
    c = int(input("Joueur "+str(player)+" joue, entré la colonne: "))
    l = l - 1
    c = c - 1

    if grille[l][c] and grille[l][c] != "X" and grille[l][c] != "O":
        return l, c
    else:
        play(player)

def checkGame(grille, loop, playerOne, playerTwo):
    for nLigne in range(3):
        elements = []
        for lig in range(3):
            elements.append(grille[lig][nLigne])
        if grille[nLigne].count("X") == 3 or elements.count("X") == 3:
            print("Joueur 1 gagne")
            playerOne = playerOne + 1
            game()
        if grille[nLigne].count("O") == 3 or elements.count("O") == 3:
            print("Joueur 2 gagne")
            playerTwo = playerTwo + 1
            game()

    if loop == 5:
        exit("Equality")

def game():
    grille = constructGrille()
    loop = 0
    playerOne = 0
    playerTwo = 0
    reset()
    while True:
        loop = loop + 1
        afficheGrille(grille)
        l, c = play(1, grille)
        grille[l][c] = "X"
        checkGame(grille, loop, playerOne, playerTwo)

        afficheGrille(grille)
        l, c = play(2, grille)
        grille[l][c] = "O"
        checkGame(grille, loop, playerOne, playerTwo)

print("début de partie: Joueur VS Joueur")
game()
