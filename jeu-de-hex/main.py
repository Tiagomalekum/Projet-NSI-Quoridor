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
            "neighbors": neighbors
        })
    board.append(row)

# Affichage du plateau avec les voisins
for row in board:
    for cell in row:
        print(f"Case {cell['position']} : Voisins -> {cell['neighbors']}")
