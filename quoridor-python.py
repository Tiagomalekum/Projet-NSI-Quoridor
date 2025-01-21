# Initialisation du plateau de jeu
def init_tableau():
    taille_tableau = 5
    tableau = [[' ' for _ in range(taille_tableau)] for _ in range(taille_tableau)]
    joueurs = {'1': (0, taille_tableau // 2), '2': (taille_tableau - 1, taille_tableau // 2)} #Positions initiales joueurs
    tableau[players['1'][0]][joueurs['A'][1]] = '1'
    tableau[players['2'][0]][joueurs['B'][1]] = '2'

# Affichage du plateau de jeu
def print_tableau(tableau):
    for row in tableau:
        print('+---' * len(tableau) + '+')
        print('| ' + ' | '.join(tableau) + ' |')
    print('+---' * len(tableau) + '+')
    return taleau, joueurs
#Tiago et Gabriel n'oubliez pas d'expliquer le code.
