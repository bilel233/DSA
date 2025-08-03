# dans cet exercice on va afficher les elts d'un tableaux de maniere alternative


def alternate(tab):
    """affiche les elts d'un tableaux de maniere alternee"""

    for i in range(0,len(tab),2):
        print(tab[i])

if __name__ == "__main__":
    alternate([1,2,3,4,5])
    print()
    alternate([0,1,2,3,4,5,6,7])
    
