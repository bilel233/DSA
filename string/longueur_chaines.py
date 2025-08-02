# dans cet exercice on va apprendre a renvoyer la longueur d'une
#chaines de caracteres

def longueur(s):
    """renvoie la longueur d'une chaine"""

    return len(s)


if __name__ == '__main__':
    s = "abc"
    s1 = ""
    s2 = " "
    assert longueur(s) == 3
    assert longueur(s1) == 0
    assert longueur(s2) == 1

