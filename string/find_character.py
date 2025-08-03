# dans cet exercice, on va chercher l'occurence d'un carectere c dans s


def find(s,c):
    """
    renvoie la position de la premiere occurence dans s. -1 sinon
    """

    n = len(s)

    for i in range(0,n):
        if s[i] == c:
            return i
    return -1

if __name__ == '__main__':
    s = "lelbi"

    assert find(s,'a') == -1
    assert find(s,'l') == 0