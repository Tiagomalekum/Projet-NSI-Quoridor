# Initialisation du plateau de jeu
def init_tableau():
    tableau = [['X' for _ in range(5)] for _ in range(5)]
    tableau[0][2] = 'A'
    tableau[4][2] = 'B'
    affichage_tableau()

def affichage_tableau():
    return tableau
#Tiago et Gabriel n'oubliez pas d'expliquer le code.
#Tester indépendamment chaque script que vous créer pour vérifier que tout fonctionne comme il faut.
#Informer les autres des fusions
