################################################################################
#                                                                              #
#                          PROJET DE HEX EN PYTHON                             #
#                                                                              #
################################################################################


# Définitions:

n = 5  # Taille de la grille
symbol = ""  # Symbole du joueur courant

# Représentation du plateau, chaque case est un dictionnaire
# qui contient les voisins possibles sous forme de tuples de coordonnées

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



# Fonction de recherche en profondeur (DFS) pour vérifier la victoire
def dfs(x, y, visited, joueur):
    if joueur == "A" and x == n - 1:  # Si on atteint le bord inférieur
        return True
    if joueur == "B" and y == n - 1:  # Si on atteint le bord droit
        return True
    
    visited.add((x, y))  # Marquer la case comme visitée
    for (nx, ny) in board[x][y]["neighbors"]:
        if (nx, ny) not in visited and board[nx][ny]["occupied_by"] == joueur:
            if dfs(nx, ny, visited, joueur):
                return True
    return False


    
# Fonction de vérification de victoire
def verifier_victoire():
    global symbol
    visited = set()

    # Pour le joueur A, vérifier s'il a réussi à relier le bord supérieur au bord inférieur
    if symbol == "A":
        for j in range(n):
            if board[0][j]["occupied_by"] == "A" and (0, j) not in visited:
                if dfs(0, j, visited, "A"):
                    affichage()
                    print("Le joueur A a gagné !")
                    return True

    # Pour le joueur B, vérifier s'il a réussi à relier le bord gauche au bord droit
    elif symbol == "B":
        for i in range(n):
            if board[i][0]["occupied_by"] == "B" and (i, 0) not in visited:
                if dfs(i, 0, visited, "B"):
                    affichage()
                    print("Le joueur B a gagné !")
                    return True

    return False


# La fonction jouer() est appelée pour effectuer un mouvement
def jouer(position):
    global symbol
    x, y = position
    if 0 <= x < n and 0 <= y < n:  # Vérifier si la position est valide
        cell = board[x][y]
        if cell["occupied_by"] is None:  # Si la case est vide
            cell["occupied_by"] = symbol
            joueur_positions[symbol].append(position)
            print(f"Le joueur {symbol} a joué à la position {position}.")
            if verifier_victoire():
                return
            # Passer au joueur suivant
            if symbol == "A":
                symbol = "B"
            elif symbol == "B":
                symbol = "A"
            affichage()
            print(f"Au joueur {symbol} de jouer.")
        else:
            print(f"La case {position} est déjà occupée.")  # Case déjà occupée
    else:
        print("Position invalide.")  # Position déjà prise


    
# Initialisation du jeu
def init():
    global symbol
    symbol = "A"  # Le joueur A commence
    
    # Réinitialiser le plateau de jeu
    for row in board:
        for cell in row:
            cell["occupied_by"] = None
    
    # Réinitialiser les coups des joueurs
    joueur_positions["A"] = []
    joueur_positions["B"] = []

    print("La partie commence.")
    affichage()
    print("Au joueur A de jouer. (\"jouer((x, y))\" pour jouer!!)")

# Initialisation
init()

#  Teste: ce teste montre que nimporte quelle chemin sans interuption donne une win
#jouer((0, 1))
#jouer((0, 4))
#jouer((0, 2))
#jouer((1, 4))
#jouer((1, 2))
#jouer((0, 0))
#jouer((2, 2))
#jouer((1, 1))
#jouer((3, 1))
#jouer((2, 4))
#jouer((3, 2))
#jouer((3, 0))
#jouer((4, 0))
