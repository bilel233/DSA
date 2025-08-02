# on va coder la fonction factorielle mais de maniere recursive


def fact(n):
    """renvoie le factorielle de n"""

    if (n == 0):        # cas de base
        return 1
    else:
        return n * fact(n-1) # appel factorielle
    
if __name__ == '__main__':
    assert fact(0) == 1
    assert fact(1) == 1
    assert fact(2) == 2
    assert fact(3) == 6