# dans cet exercice, on va realiser la somme des chiffres d'un nombre de maniere recursive


def somme_chiffre_recursivite(n):
    """on realise la somme du nombre de mainiere recursive"""

    if (n >=0 and n <=9):
        return n        # cas de base
    
    return n %10 + somme_chiffre_recursivite(n//10) # le coeur de la recursivite

if __name__ == '__main__':
    assert somme_chiffre_recursivite(9) == 9
    assert somme_chiffre_recursivite(0) == 0
    assert somme_chiffre_recursivite(12) == 3
    assert somme_chiffre_recursivite(12345) == 15


    