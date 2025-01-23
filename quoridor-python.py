# Initialisation du plateau de jeu
def init_tableau():
    print("entrer valeur neuil")
    tableau = [['X' for _ in range(5)] for _ in range(5)]
    tableau[0][3] = 'A'
    tableau[4][3] = 'B'
    affichage_tableau()

def affichage_tableau():
    print(tableau)
#Tiago et Gabriel n'oubliez pas d'expliquer le code.
#Tester indépendamment chaque script que vous créer
#pour vérifier que tout fonctionne comme il faut.
