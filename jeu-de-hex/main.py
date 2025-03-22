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
        print("Position invalide.")  # Position non-existante

    
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
    print("Au joueur A de jouer. (\"jouer((x,y))\" pour jouer!!)")

# Initialisation
init()
