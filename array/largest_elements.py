# dans cet exercice, on va travailler sur le largest elements d'un array


def maximun_array(tab,n):
    """renvoie le maximum dans le tableau tab"""

    maximum = tab[0]

    for i in range(1,n):    # parcourt par indice
        if (tab[i] > maximum):
            maximum = tab[i]
    return maximum

# de maniere recursive

def largest_recursive(tab,i):
    """
    renvoie le maximum dans tab a partir de l'indice i
    """

    if i == len(tab) -1:
        return tab[i]
    
    res = largest_recursive(tab,i+1)

    return max(res,tab[i])


if __name__ == '__main__':
    tab = [1,2,3,10,100]
    res = maximun_array(tab,5)
    print(f"{res}")
    # testons la fonctions recursive
    print()
    res_1 = largest_recursive(tab,0)
    print(f"{res_1}")



