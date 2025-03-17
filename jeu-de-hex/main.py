# Définir la taille de la grille
n = 5

# Représentation du plateau, chaque case est un dictionnaire
# qui contient les voisins possibles sous forme de tuples de coordonnées

init = True

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
            "occupied_by": None  # Ajout d'un champ pour indiquer si la case est occupée par un joueur
        })
    board.append(row)


# Nouvelle fonction pour afficher le plateau de jeu
def affichage():
    for row in board:
        row_display = []
        for cell in row:
            if cell["occupied_by"]:
                row_display.append(cell["occupied_by"])  # Affiche le symbole du joueur
            else:
                row_display.append(".")  # Une case vide est représentée par un point
        print(" ".join(row_display))
    print()  # Ligne vide pour séparer les affichages


# Fonction pour qu'un joueur joue
def jouer(player, symbol, position):
    x, y = position
    if 0 <= x < n and 0 <= y < n:
        cell = board[x][y]
        if cell["occupied_by"] is None:
            cell["occupied_by"] = symbol
            if init == False:
                print(f"Le joueur {player} a joué à la position {position}.")
                affichage()
        else:
            print(f"La case {position} est déjà occupée.")
    else:
        print("Position invalide.")


# Fonction pour réinitialiser la partie
def reinit():
    init = True
    jouer("Joueur A", "A", (0, 2))
    jouer("Joueur B", "B", (2, 0))
    print("La partie commence.")
    affichage()
    init = False

reinit()
