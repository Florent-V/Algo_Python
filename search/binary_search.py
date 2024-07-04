"""
Binary search algorithm
"""

def binary_search(list, target):
    """
    Effectue une recherche binaire sur une liste triée pour trouver l'élément cible.
    
    Paramètres:
    liste (list): La liste triée dans laquelle rechercher l'élément cible.
    cible: L'élément à rechercher dans la liste.
    
    Retourne:
    int: L'index de l'élément cible dans la liste, ou -1 si l'élément n'est pas trouvé.
    """
    start = 0
    end = len(list) - 1
    
    while start <= end:
        middle = (start + end) // 2
        if list[middle] == target:
            return middle
        elif list[middle] < target:
            start = middle + 1
        else:
            end = middle - 1
    
    return -1

# Exemple d'utilisation
if __name__ == '__main__':
    list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    result = binary_search(list, target)
    if result != -1:
        print(f"Element trouvé à l'index: {result}")
    else:
        print("Element non trouvé dans la liste")