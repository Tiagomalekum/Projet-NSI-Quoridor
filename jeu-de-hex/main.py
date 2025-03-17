# Définir la taille de la grille
n = 5

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
            "occupied_by": None  # Ajout d'un champ pour indiquer si la case est occupée par un joueur
        })
    board.append(row)

# Fonction pour qu'un joueur joue
def jouer(player, position):
    x, y = position
    if 0 <= x < n and 0 <= y < n:
        cell = board[x][y]
        if cell["occupied_by"] is None:
            cell["occupied_by"] = player
            print(f"Le joueur {player} a joué à la position {position}.")
        else:
            print(f"La case {position} est déjà occupée.")
    else:
        print("Position invalide.")

# Nouvelle fonction pour afficher le plateau de jeu
def affichage():
    for row in board:
        row_display = []
        for cell in row:
            if cell["occupied_by"]:
                row_display.append(cell["occupied_by"][0])  # Affiche la première lettre du joueur
            else:
                row_display.append(".")  # Une case vide est représentée par un point
        print(" ".join(row_display))
    print()  # Ligne vide pour séparer les affichages

# Affichage initial du plateau avec les voisins et l'état d'occupation
for row in board:
    for cell in row:
        print(f"Case {cell['position']} : Voisins -> {cell['neighbors']} | Occupée par -> {cell['occupied_by']}")

# Exemple d'utilisation de la fonction play_move
jouer("Joueur 1", (2, 2))
jouer("Joueur 2", (2, 2))
jouer("Joueur 2", (3, 3))

# Afficher le plateau après quelques mouvements
affichage()
