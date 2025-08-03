# dans cet exercice, on verifie si deux chaines de caracteres sont identiques

def are_the_same(s1,s2):
    """
    Verifie si deux chaines de caracteres sont identiques
    """

    return s1 == s2

if __name__ == '__main__':
    s1 = "abc"
    s2 = "abd"

    assert are_the_same(s1,s2) == False

    

