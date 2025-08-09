#dans cet exercice, nous allons revoir les exercices sur les strings


def length(s):
    """renvoie la longueur de la chaines de caracteres s"""

    return len(s)

def get_length(s):
    """renvoie la longueur de la chaine s"""

    cpt = 0

    for k in s:
        cpt = cpt + 1

    return cpt


if __name__ == '__main__':
    assert length("Epita") == 5
    assert length(" ") == 1

    assert get_length("Epita") == 5
    assert get_length("") == 0
