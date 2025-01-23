# Initialisation du plateau de jeu
def init_tableau():
    taille_tableau = int(input())
    tableau = [['X' for _ in range(taille_tableau)] for _ in range(taille_tableau)]
    tableau[[0][taille_tableau / 2]] = '1'
    tableau[[taille_tableau - 1][taille_tableau / 2]] = '2'

# Affichage du plateau de jeu
def print_tableau(tableau):
    print(tableau)

#Tiago et Gabriel n'oubliez pas d'expliquer le code.
# Tester indépendamment chaque script que vous créer
# pour vérifier que tout fonctionne comme il faut.
