import pygame
from hex_jeu.constants import *

#initialisation
pygame.init()

#def de p_termine pour que le programme fonctionne
p_termine = False

#temps
temps = pygame.time.Clock()

fenetre = pygame.display.set_mode((larg,longu))

def get_local(x,y):
    ligne = y//hexa
    col = x//hexa
    
def main():
    run = True
    FPS = 60
    while run:
        temps.tick(FPS)
        #Pour fermer le jeu
        for event in pygame.event.get():
            if event.type == pygame. QUIT:
                run = False
                quit()

            #récupérer les coordonées de la souris quand on clique
            if event.type == pygame.MOUSEBUTTONDOWN and not p_termine:
                if pygame.mouse.get_pressed()[0]:
                    clickLoc = pygame.mouse.get_pos()
                    #PROBLEME: normallement ligne,col = get_local(clickLoc[0],clickLoc[1])
                    ligne,col = clickLoc[0],clickLoc[1]
                    #test pour confirmer que la position des cliques sont bien récupérés
                    print(ligne,col)

main()
