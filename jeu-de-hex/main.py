################################################################################
#                                                                              #
#                          PROJET DE HEX EN PYTHON                             #
#                                                                              #
################################################################################

import time
import tkinter as tk
import threading


# Définitions:
n = 5 # Taille de la grille
symbol = ""  # Symbole du joueur courant
partie_t = False
board = []




# Représentation du plateau, chaque case est un dictionnaire
# qui contient les voisins possibles sous forme de tuples de coordonnées
for i in range(n):
    row = []
    for j in range(n):
        neighbors = []
        
        # Ajouter des voisins basés sur des règles de voisinage pour un hexagone
        if i > 0:  # voisin en haut
            neighbors.append((i-1, j))
        if i < n-1:  # voisin en bas
            neighbors.append((i+1, j))
        if j > 0:  # voisin à gauche
            neighbors.append((i, j-1))
        if j < n-1:  # voisin à droite
            neighbors.append((i, j+1))
        if i > 0 and j < n-1:  # voisin en haut à droite
            neighbors.append((i-1, j+1))
        if i < n-1 and j > 0:  # voisin en bas à gauche
            neighbors.append((i+1, j-1))
        
        row.append({
            "position": (i, j),
            "neighbors": neighbors,
            "occupied_by": None  # Champ pour indiquer si la case est occupée par un joueur
        })
    board.append(row)



# Structure pour garder trace des coups joués
joueur_positions = {
    "A": [],
    "B": []
}



# Fonction d'affichage du plateau
def affichage():
    for row in board:
        row_display = []
        for cell in row:
            if cell["occupied_by"]:
                row_display.append(cell["occupied_by"])  # Affiche le symbole du joueur
            else:
                row_display.append(".")  # Une case vide est représentée par un point
        print(" ".join(row_display))  # Concaténation
    print()  # Ligne vide pour séparer les lignes    



def est_chemin(position, joueur, visited):
    x, y = position
    if joueur == "A" and y == n - 1:
        return True  # Joueur A atteint le bord droit
    if joueur == "B" and x == n - 1:
        return True  # Joueur B atteint le bord bas
    
    visited.add(position)
    
    for voisin in board[x][y]["neighbors"]:
        vx, vy = voisin
        if board[vx][vy]["occupied_by"] == joueur and voisin not in visited:
            if est_chemin(voisin, joueur, visited):
                return True
    
    return False



def a_gagne(joueur):
    if joueur == "A":
        for i in range(n):
            if board[i][0]["occupied_by"] == "A":
                if est_chemin((i, 0), "A", set()):
                    return True
    elif joueur == "B":
        for j in range(n):
            if board[0][j]["occupied_by"] == "B":
                if est_chemin((0, j), "B", set()):
                    return True
    
    return False



def change_time(time):
    global time_sec
    time_sec = time


            
def minuteur_start():
    def minuteur():
        global partie_t, time_sec
        while time_sec > 0:
            print(time_sec,end=' ')
            # Affiche le minuteur
          
            time.sleep(1)
            # Cette fonction fait une pause d'une 
            # seconde à chaque itération.
            
            time_sec -= 1
            # Cette ligne enlève 1 au timer après 1 seconde.
        
        if time_sec <= 0:
            if symbol == "A":
               print("Temps écoulé! Le joueur B a gagné! Entrez \"init(nombre de cases & colonnes)\" pour commencer une nouvelle partie.")
            if symbol == "B":
               print("Temps écoulé! Le joueur A a gagné! Entrez \"init(nombre de cases & colonnes)\" pour commencer une nouvelle partie.")
            partie_t = True
    threading.Thread(target=minuteur).start()
        

# La fonction jouer() est appelée pour effectuer un mouvement
def jouer(position):
    global partie_t,symbol, n
    if partie_t:
        print("Impossibilité de jouer, la partie est terminée. Entrez \"init(nombre de cases & colonnes)\" pour commencer une nouvelle partie.")
    else:
        x, y = position
        if 0 <= x < n and 0 <= y < n:  # Vérifier si la position est valide
            if 0 <= x < n and 0 <= y < n:  # Vérifier si la position est valide
                cell = board[x][y]
                if cell["occupied_by"] is None:  # Si la case est vide
                    cell["occupied_by"] = symbol
                    joueur_positions[symbol].append(position)
                    print(f"Le joueur {symbol} a joué à la position {position}.")
                
                    affichage()
            
                    if a_gagne("A"):
                        print("Le joueur A a gagné! Entrez \"init(nombre de cases & colonnes)\" pour commencer une nouvelle partie.")
                        partie_t = True
                    elif a_gagne("B"):
                        print("Le joueur B a gagné! Entrez \"init(nombre de cases & colonnes)\" pour commencer une nouvelle partie.")
                        partie_t = True
                    elif all(cell["occupied_by"] is not None for row in board for cell in row):
                        print("Il y a ex-aequo! Entrez \"init(nombre de cases & colonnes)\" pour commencer une nouvelle partie.")
                        partie_t = True

                    else:
                        # Passer au joueur suivant
                        if symbol == "A":
                            symbol = "B"
                            print(f"Au joueur {symbol} de jouer.")
                        elif symbol == "B":
                            symbol = "A"
                            print(f"Au joueur {symbol} de jouer.")
                        change_time(10 * n // 2 + 1)
                else:
                     print(f"La case {position} est déjà occupée.")  # Case déjà occupée
        else:
            print("Position invalide.")  # Position non-existante



# Initialisation du jeu
def init(number):
    """Reinitialise la partie."""
    global n, board, partie_t, symbol, time_sec

    n = number
    partie_t = False
    symbol = "A"  # Le joueur A commence
    time_sec = 10 * n // 2
    
    # Réinitialiser le plateau de jeu
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            neighbors = []

            # Ajouter des voisins basés sur des règles de voisinage pour un hexagone
            if i > 0:  # voisin en haut
                neighbors.append((i-1, j))
            if i < n-1:  # voisin en bas
                neighbors.append((i+1, j))
            if j > 0:  # voisin à gauche
                neighbors.append((i, j-1))
            if j < n-1:  # voisin à droite
                neighbors.append((i, j+1))
            if i > 0 and j < n-1:  # voisin en haut à droite
                neighbors.append((i-1, j+1))
            if i < n-1 and j > 0:  # voisin en bas à gauche
                neighbors.append((i+1, j-1))

            row.append({
                "position": (i, j),
                "neighbors": neighbors,
                "occupied_by": None  # Champ pour indiquer si la case est occupée par un joueur
            })
        board.append(row)
    
    # Réinitialiser les coups des joueurs
    joueur_positions["A"] = []
    joueur_positions["B"] = []

    print("La partie commence.")
    affichage()
    print("Au joueur A de jouer. (\"jouer((ligne,colonne))\" pour jouer!!)")
    minuteur_start()




def donner_occupes():
    print(joueur_positions)
    
def donner_neighbors():
    for row in board:
        for cell in row:
            print(f"Case {cell['position']} : Voisins -> {cell['neighbors']}")

# Initialisation
init(5)
