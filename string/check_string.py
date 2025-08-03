# dans cet exercice, on verifie si deux chaines de caracteres sont identiques

def are_the_same(s1,s2):
    """
    Verifie si deux chaines de caracteres sont identiques
    """

    return s1 == s2

# fonction qui n'utilise pas la methode ==

def ma_methode(s1,s2):
    """
    renvoie True si les chaines sont identiques. False sinon
    """

    if len(s1) != len(s2):
        return False
    # dans le cas ou ils ont la meme longueur
    for i in range(0,len(s1)):
        if s1[i] != s2[i]:
            return False
    # au final, arrive ici, c'est True

    return True

if __name__ == '__main__':
    s1 = "abc"
    s2 = "abd"

    assert are_the_same(s1,s2) == False
    assert ma_methode(s1,s2) == False
    



