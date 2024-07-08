# Créé par Fantôme, petit projet pour prendre en main pygame

# Pour jouer, lancer simplement le programme, vous devez cliquer sur les cercles, et ce avec la souris ou avec
# Les touches x et c . Si il y a 6 cercles en même temps sur le plateau, c'est perdu.
# Essayez de battre mon high score : 633
# Bon courage !





import pygame
import random
from pygame import *
from pygame import gfxdraw
from random import randint
from time import time

#Valeurs pour le jeu
Jeu = [0,0,0,0,0,0,0,0,0]

# Couleurs + données
Bleu = (0, 0, 255)
Rouge = (255, 0, 0)
Vert = (0,255,0)
Noir = (0,0,0)
Blanc = (255,255,255)
Rayon = 35
Coord = [(75,75),(75,150),(75,225),(150,75),(150,150),(150,225),(225,75),(225,150),(225,225)] # Coordonnées de tous les cercles

# --------------------------------------------------------- #
# Fonctions utilisées pour optimiser le programme principal
# --------------------------------------------------------- #


# Fonctions utilisées pour le jeu :
def normalisation_des_cos(Co):
    """Détecte le centre de cercle le plus proche (en x, puis en y) afin de le cliquer plus tard"""
    if Co <= 110 :
        m = 75
    elif 110 < Co and Co <= 185 :
        m = 150
    else :
        m = 225
    return m


def CentreDeRef(x,y):
    """Utilise les co x et y afin de déterminer le centre du cercle proche"""
    for j in range(9):
        if Coord[j][0] == x and Coord[j][1] == y :
            return j



def Changement_du_seuil(Niveau,Seuil,Score):
    """teste s'il y a eu un passage de niveau, au quel cas les modifie"""
    if Niveau == 0 and Score > 7:
        Seuil = 1.3
        Niveau += 1
        print("niveau 1")
    elif Niveau == 1 and Score > 14 :
        Seuil = 1.3
        Niveau += 1
        print("niveau 2")
    elif Niveau == 2 and Score > 29 :
        Seuil = 1.1
        Niveau += 1
        print("niveau 3")
    elif Niveau == 3 and Score > 45 :
        Seuil = 1.0
        Niveau += 1
        print("niveau 4")
    elif Niveau == 4 and Score > 69 :
        Seuil = 1.0
        Niveau += 1
        print("niveau 5")
    elif Niveau == 5 and Score > 94 :
        Seuil = 0.8
        Niveau += 1
        print("niveau 6")
    elif Niveau == 6 and Score > 119 :
        Seuil = 0.6
        Niveau += 1
        print("niveau 7")
    elif Niveau == 7 and Score > 199 :
        Seuil = 0.25
        Niveau += 1
        print("niveau 8")
    elif Niveau == 8 and Score > 299:
        Seuil = 0.20
        Niveau += 1
        print("niveau 9")
    elif Niveau == 9 and Score > 399 :
        Seuil = 0.15
        Niveau += 1
        print("niveau 10")
    elif Niveau == 10 and Score > 499 :
        Seuil = 0.12
        Niveau += 1
        print("niveau 11")
    elif Niveau == 11 and Score > 1000 :
        Seuil = 0.09
        Niveau += 1
        print("niveau 12")
    return (Niveau,Seuil)


# Fonction utilisées pour le reset de parties
def Test_Defaite():
    """test s'il y a plus de 6 cercles allumés et donc la défaite au quel cas """
    total_des_présences = 0
    for i in range(9):
        total_des_présences += Jeu[i]
    if total_des_présences >= 6:
        return True
    else :
        return False

def jaiplusperdu():
    """reset la variable Jeu"""
    for i in range(9):
        Jeu[i] = 0


def test_trop_de_spam(Spam,fenetre):
    if Spam == 3:
        Jeu[randint(0,8)] = 1
        for i in range(9):
            if Jeu[i] == 1 :
                pygame.gfxdraw.filled_circle(fenetre, Coord[i][0],Coord[i][1], Rayon, Rouge)
                pygame.display.update()
        return 0
    return Spam


# Fonction utlisée pour la création / modification du fichier highscore et donc du highscore
def gestion_highscore(Score):
    """Modifie le Highscore si jamais le joueur l'a effectué"""
    file = open("highscore.txt","r")
    if Score > float(file.readline()) :
        file.close()
        file = open("highscore.txt", "w")
        file.write(str(Score))
    file.close()


def test_presence_highscore():
    """Vérifie la présence du fichier 'highscore' sur l'ordinateur"""
    try:
        with open('highscore.txt'): pass
    except IOError:
        file = open("highscore.txt", "w")
        file.write("0")
        file.close()


# ---------------------------------------------------------

#Programme princiapl (en fonction pour pouvoir l'appeler de façon récursive)
def programme_principal():
    # Création de la fenêtre, setup de l'affichage graphique et des variables de base
    pygame.init()
    longueur = 300
    largueur = 300
    Score = 0
    Seuil = 1.5
    Niveau = 0
    Niveau_ref = 0
    Spam = 0
    Reset = time()
    fenetre = pygame.display.set_mode((largueur,longueur))
    pygame.display.flip()
    pygame.display.set_caption("Clique vite les cercles !")

    #Création des textes à l'écran : Niveau, Score, Highscore
    pygame.draw.rect(fenetre, Noir, pygame.Rect(00,00,300,300))
    police = pygame.font.SysFont("Monospace",18)

    image_texte = police.render ("Nombre de points = " + str(Score), 1, Blanc) # Affichache score
    for i in range(5):
        fenetre.blit(image_texte,(10,0))


    image_texte = police.render ("Niveau de difficulté = " + str(Niveau), 1, Blanc) # Affichage du niveau
    for i in range(15):
        fenetre.blit(image_texte,(10,20))


    file = open("highscore.txt","r")         # Affichage du highscore
    HighScore = int(file.readline())
    file.close()
    image_texte = police.render ("Highscore = " + str(HighScore), 1, Blanc)
    for i in range(5):
        fenetre.blit(image_texte,(10,270))

    #Création des cercles
    for i in range(0,9): #Cercles
        pygame.gfxdraw.filled_circle(fenetre, Coord[i][0], Coord[i][1], Rayon, Bleu)
    pygame.display.update()


    #Programme de la boucle, permettant de cliquer les cercles, de fermer la fenêtre et même de reset la fenêtre à la fin d'une partie
    continuer = 1
    while continuer > 0:
        Temps = time() - Reset #Ajoute du temps
        if Temps > Seuil: #teste si le seuil de temps est passé, au quel cas il crée un cercle aléatoirement
            Spam = 0
            Reset = time()
            if Niveau < 2:              #Spawn toujours un seul cercle
                Jeu[randint(0,8)] = 1
                for i in range(9):
                    if Jeu[i] == 1 :
                        pygame.gfxdraw.filled_circle(fenetre, Coord[i][0],Coord[i][1], Rayon, Rouge)
                        pygame.display.update()
            elif Niveau < 5 :           #Spawn 1 ou 2 cercle aléatoirement
                for i in range(randint(1,2)):
                    Jeu[randint(0,8)] = 1
                for i in range(9):
                    if Jeu[i] == 1 :
                        pygame.gfxdraw.filled_circle(fenetre, Coord[i][0],Coord[i][1], Rayon, Rouge)
                        pygame.display.update()
            elif Niveau < 8 :           #Spawn toujours 2 cercles
                Jeu[randint(0,8)] = 1
                Jeu[randint(0,8)] = 1
                for i in range(9):
                    if Jeu[i] == 1 :
                        pygame.gfxdraw.filled_circle(fenetre, Coord[i][0],Coord[i][1], Rayon, Rouge)
                        pygame.display.update()
            else : # Spawn des cercles 1 par 1 mais à une vitesse folle
                Jeu[randint(0,8)] = 1
                for i in range(9):
                    if Jeu[i] == 1 :
                        pygame.gfxdraw.filled_circle(fenetre, Coord[i][0],Coord[i][1], Rayon, Rouge)
                        pygame.display.update()
        if Niveau == (Niveau_ref + 1) : # Gère l'affichage du niveau en haut
                pygame.draw.rect(fenetre, Noir, pygame.Rect(250,20,40,15))
                image_texte = police.render ("Niveau de difficulté = " + str(Niveau), 1, Blanc)
                for i in range(5):
                    fenetre.blit(image_texte,(10,20))
                pygame.display.update()
                Niveau_ref += 1

        (Niveau,Seuil) = Changement_du_seuil(Niveau,Seuil,Score) #Teste s'il y a eu un passage de niveau, au quel cas les modifie
        Spam = test_trop_de_spam(Spam,fenetre)


        ##print(Temps) # simple test pour voir comment se comporte le temps
        for event in pygame.event.get():
            if (event.type == MOUSEBUTTONDOWN and mouse.get_pressed() == (1,0,0)) or (event.type == KEYDOWN and (event.key == K_x or event.key == K_c)):  #Teste les click du joueur et si les clicks ont des effets + gère l'affichage du score
                coordonnee = mouse.get_pos()
                Co_Souris_x = coordonnee[0]
                Co_Souris_y = coordonnee[1]
                x = normalisation_des_cos(Co_Souris_x)
                y = normalisation_des_cos(Co_Souris_y)
                j = CentreDeRef(x,y)
                hypo = ((Coord[j][0]-Co_Souris_x)**2 + (Coord[j][1]-Co_Souris_y)**2)**0.5
                if hypo <= Rayon :
                    if Jeu[j] == 1 :
                        pygame.gfxdraw.filled_circle(fenetre, x, y, Rayon, Bleu)
                        Score += 1
                        pygame.draw.rect(fenetre, Noir, pygame.Rect(220,00,40,15))
                        image_texte = police.render ("Nombre de points = " + str(Score), 1, Blanc)
                        for i in range(15):
                            fenetre.blit(image_texte,(10,0))
                        pygame.display.update()
                        Jeu[j] = 0
                    else :
                        Spam += 1
                else :
                    Spam += 1
            if event.type == KEYDOWN: #Permet de reset le jeu en cliquant sur "p" a n'importe quel moment
                if event.key == K_p:
                    pygame.quit()
                    jaiplusperdu()
                    gestion_highscore(Score)
                    programme_principal()
                    continuer = 0
            if event.type == QUIT : #Permet de quitter normalement le jeu sans avoir de problèmes
                pygame.quit()
                gestion_highscore(Score)
                continuer = 0
            if Test_Defaite() == True : #Teste si le joueur a plus de 6 cercles non cliqués, au quel cas il perd
                conti = 1
                pygame.draw.rect(fenetre, Rouge, pygame.Rect(00,100,300,70)) #Gère l'affichage du message à la mort
                gestion_highscore(Score)
                image_texte = police.render ("Vous avez perdu TT", 1, Bleu)
                for i in range(3):
                    fenetre.blit(image_texte,(40,110))
                image_texte = police.render ("Pour recommencer, appuyez", 1, Bleu)
                for i in range(3):
                    fenetre.blit(image_texte,(15,125))
                image_texte = police.render ("sur 'p' ", 1, Bleu)
                for i in range(3):
                    fenetre.blit(image_texte,(105,140))
                pygame.display.update()
                while conti >= 1: #Permet au joueur ayant perdu de quitter la fênetre ou restart le jeu avec "p"
                    for event in pygame.event.get():
                        if event.type == QUIT :
                            pygame.quit()
                            conti = 0
                        if event.type == KEYDOWN:
                            if event.key == K_p:
                                pygame.quit()
                                jaiplusperdu() #Reset la liste "jeu" afin de ne pas recommencer le jeu avec 6 cercles rouge dès le début
                                programme_principal()
                                conti = 0
                continuer = 0



# Programme principal 2

test_presence_highscore() # Comme son nom l'indique, teste la présence du fichier et s'il n'y en a pas, en crée un (Peut-être incompatible avec MacOs...)
programme_principal() #On l'appelle la première fois afin de le lancer dès le début du programme











