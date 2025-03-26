import time
import threading
from tkinter import *
from tkinter import messagebox

# Définitions:
n = 5  # Taille de la grille
symbol = "A"  # Symbole du joueur courant
partie_t = False
board = []
time_sec = 0
hex_size = 30  # Taille des hexagones
timer_running = False
pause_timer = False
moves_played = 0  # Nouvelle variable pour suivre le nombre de coups joués
block_mode = False
bloqueurs_charges = {
    "A": 1,
    "B": 1
}



# Fonction d'affichage du plateau
def affichage():
    c = 0
    for row in board:
        row_display = []
        for cell in row:
            if cell["occupied_by"]:
                row_display.append(cell["occupied_by"])  # Affiche le symbole du joueur
            else:
                row_display.append(".")  # Une case vide est représentée par un point
        c += 1
        print(" " * c + " ".join(row_display))  # Concaténation et décalage des colonnes
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
        global partie_t, time_sec, timer_running, pause_timer, moves_played
        timer_running = True
        time_label.config(text=f"Time left: {time_sec}s")
        while time_sec > 0 and not partie_t:
            if not pause_timer:
                sleep_time = max(0.1, 1 - (moves_played * 0.03))  # Réduire le temps de sommeil progressivement
                time.sleep(sleep_time)
                time_sec -= 1
                time_label.config(text=f"Time left: {time_sec}s")

        if not partie_t:
            if symbol == "A":
                canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, 
                                   text="Temps écoulé! Le joueur B a gagné!", fill="black", font=("Arial", 24))
            if symbol == "B":
                canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, 
                                   text="Temps écoulé! Le joueur A a gagné!", fill="black", font=("Arial", 24))
            partie_t = True
        timer_running = False
    threading.Thread(target=minuteur).start()

def pause_resume_timer():
    global pause_timer
    pause_timer = not pause_timer
    pause_button.config(text="Reprendre" if pause_timer else "Pause")

def jouer(position):
    global partie_t, symbol, n, moves_played, pause_timer, block_mode, bloqueurs_charges
    if partie_t:
        messagebox.showwarning("Partie terminée", "Impossibilité de jouer, la partie est terminée. ")
    elif not pause_timer:
        x, y = position
        cell = board[x][y]
        if cell["occupied_by"] is None and not block_mode:  # Si la case est vide
            cell["occupied_by"] = symbol
            draw_hexagon(canvas, x, y, symbol)  # Mettre à jour l'affichage du plateau
            if a_gagne("A"):
                canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, 
                                   text="Le joueur A a gagné!", fill="black", font=("Arial", 24))
                partie_t = True
            elif a_gagne("B"):
                canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, 
                                   text="Le joueur B a gagné!", fill="black", font=("Arial", 24))
                partie_t = True
            elif all(cell["occupied_by"] is not None for row in board for cell in row):
                canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, 
                                   text="Il y a ex-aequo!", fill="black", font=("Arial", 24))
                partie_t = True
            else:
                # Passer au joueur suivant
                if symbol == "A":
                    symbol = "B"
                elif symbol == "B":
                    symbol = "A"
                change_time(2 * n + n)
                turn_label.config(text=f"Tour du joueur: {symbol}")  # Mettre à jour le tour du joueur
                moves_played += 1
                allturns_label.config(text=f"Coups joués: {moves_played}")
            
        elif cell["occupied_by"] is None and block_mode:
            cell["occupied_by"] = "Blocked"
            bloqueurs_charges[symbol] -= 1
            block_button.config(text=f"Bloquer une case (A:{bloqueurs_charges["A"]} B:{bloqueurs_charges["B"]})") # Mettre à jour le compteur du boutton bloqueur
            draw_hexagon(canvas, x, y, "Blocked")
            block_mode = False
            turn_label.config(text=f"Tour du joueur: {symbol}")
            moves_played += 1
            allturns_label.config(text=f"Coups joués: {moves_played}")
            
        else:
            messagebox.showwarning("Case occupée", f"La case {position} est déjà occupée.")  # Case déjà occupée

def block_cell(position):
    global symbol, bloqueurs_charges, time_sec, block_mode
    if bloqueurs_charges[symbol] > 0:
        if not block_mode:
            time_sec += n*4
        block_mode = True
        turn_label.config(text="Veuillez choisir une case à bloquer.")
    else:
        messagebox.showwarning("Vous avez déjà utilisé tous vos bloqueurs.")

def init(number):
    """Reinitialise la partie."""
    if not (type(number) == int):
        messagebox.showwarning("Erreur", "Le nombre de cases doit être un entier.")
        return
    if not (5 <= number <= 25):
        messagebox.showwarning("Erreur", "Le nombre de cases doit être compris entre 5 et 25.")
        return

    global n, board, partie_t, symbol, time_sec, timer_running, moves_played, hex_size, bloqueurs_charges
    n = number
    hex_size = 42-number*1.05
    partie_t = False
    symbol = "A"  # Le joueur A commence
    time_sec = 2 * n + n
    bloqueurs_charges = {
    "A": n // 3,
    "B": n // 3
    }
    block_button.config(text=f"Bloquer une case (A:{bloqueurs_charges["A"]} B:{bloqueurs_charges["B"]})") # Mettre à jour le compteur du boutton bloqueur
    moves_played = 0
    allturns_label.config(text=f"Coups joués: {moves_played}")

    # Réinitialiser le plateau de jeu
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            neighbors = []
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

    # Mettre à jour l'interface graphique
    canvas.delete("all")
    draw_board(canvas, n)
    time_label.config(text=f"Time left: {time_sec}s")
    turn_label.config(text=f"Tour du joueur: {symbol}")  # Afficher le tour du joueur
    partie_t = False
    if not timer_running:
        minuteur_start()

def quitter():
    root.destroy()

def draw_hexagon(canvas, row, col, player=None):
    # Calcul des positions x et y pour centrer les hexagones
    x_offset = (canvas.winfo_width() - ((n - 1) * hex_size * 2.615 + hex_size * (3**0.01))) / 2
    y_offset = (canvas.winfo_height() - (n * hex_size * 1.41)) / 2

    # Calcul des coordonnées du centre de l'hexagone
    x = x_offset + col * (hex_size * 1.8) + row * (hex_size * 0.9)
    y = y_offset + row * (hex_size * (3**0.4))

    points = [
        x, y - hex_size,
        x + hex_size * (3**0.5) / 2, y - hex_size / 2,
        x + hex_size * (3**0.5) / 2, y + hex_size / 2,
        x, y + hex_size,
        x - hex_size * (3**0.5) / 2, y + hex_size / 2,
        x - hex_size * (3**0.5) / 2, y - hex_size / 2
    ]
    fill = "white"
    if player == "A":
        fill = "red"
    elif player == "B":
        fill = "blue"
    elif player == "Blocked":
        fill = "black"
    canvas.create_polygon(points, outline="black", fill=fill, tags=f"{row},{col}")
    canvas.tag_bind(f"{row},{col}", "<Button-1>", lambda e, r=row, c=col: jouer((r, c)))

def draw_board(canvas, n):
    # Dessiner les hexagones
    for i in range(n):
        for j in range(n):
            draw_hexagon(canvas, i, j)
    
    # Dessiner les barres décoratives rouges à droite et à gauche
    canvas.create_rectangle(0, 0, 30 * 0.9, canvas.winfo_height(), outline="red", fill="red")
    canvas.create_rectangle(canvas.winfo_width() - 30 * 0.9, 0, canvas.winfo_width(), canvas.winfo_height(), outline="red", fill="red")
    
    # Ajouter l'étiquettes "A" dans les barres rouges
    canvas.create_text(30 * 0.45, canvas.winfo_height() / 2, text="A", fill="white", font=("Arial", 24))
    canvas.create_text(canvas.winfo_width() - 30 * 0.45, canvas.winfo_height() / 2, text="A", fill="white", font=("Arial", 24))
    
    # Dessiner les barres décoratives bleues en haut et en bas
    canvas.create_rectangle(0, 0, canvas.winfo_width(), 30 * 0.9, outline="blue", fill="blue")
    canvas.create_rectangle(0, canvas.winfo_height() - 30 * 0.9, canvas.winfo_width(), canvas.winfo_height(), outline="blue", fill="blue")

    # Ajouter l'étiquette "B" dans les barres bleues
    canvas.create_text(canvas.winfo_width() / 2, 30 * 0.45, text="B", fill="white", font=("Arial", 24))
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() - 30 * 0.45, text="B", fill="white", font=("Arial", 24))

# Initialisation de l'interface graphique
root = Tk()
root.title("Jeu de Hex")

# Cadre pour le plateau de jeu
canvas = Canvas(root, width=1200, height=800)
canvas.pack(pady=20)

# Boutons de contrôle
control_frame = Frame(root)
control_frame.pack(pady=10)

# Ajout d'un champ de saisie pour la taille du tableau dans l'interface graphique
size_entry_label = Label(control_frame, text="Taille du tableau (entre 5 et 25):")
size_entry_label.grid(row=0, column=3, padx=5)
size_entry = Entry(control_frame, width=5)
size_entry.grid(row=0, column=4, padx=5)

block_button = Button(control_frame, text=f"Bloquer une case (A:{bloqueurs_charges["A"]} B:{bloqueurs_charges["B"]})", command=lambda: block_cell((int(size_entry.get()), int(size_entry.get()))))
block_button.grid(row=0, column=5, padx=5)

# Réinitialisation de la partie avec choix de la taille de la grille
reset_button = Button(control_frame, text="Réinitialiser", command=lambda: init(int(size_entry.get())))
reset_button.grid(row=0, column=0, padx=5)

pause_button = Button(control_frame, text="Pause", command=pause_resume_timer)
pause_button.grid(row=0, column=1, padx=5)

quit_button = Button(control_frame, text="Quitter", command=quitter)
quit_button.grid(row=0, column=2, padx=5)

# Label pour le nombre de coups de la partie
allturns_label = Label(root, text=f"Coups joués: {moves_played}", font=("Arial", 10))
allturns_label.pack(side="bottom", pady=3)

# Label pour afficher le tour du joueur
turn_label = Label(root, text=f"Tour du joueur: {symbol}", font=("Arial", 13))
turn_label.pack(side="bottom", pady=10)

# Label pour le minuteur
time_label = Label(root, text=f"Temps restant: {time_sec}s", font=("Arial", 18))
time_label.pack(side="bottom", pady=10)

# Lancer le jeu
root.update_idletasks()  # Mettre à jour le canvas pour obtenir les bonnes dimensions
init(n)
root.mainloop()
