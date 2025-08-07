# dans cet exercice, on va travailler sur le largest elements d'un array


def maximun_array(tab,n):
    """renvoie le maximum dans le tableau tab"""

    maximum = tab[0]

    for i in range(1,n):    # parcourt par indice
        if (tab[i] > maximum):
            maximum = tab[i]
    return maximum

if __name__ == '__main__':
    tab = [1,2,3,10,100]
    res = maximun_array(tab,5)
    print(f"{res}")
    
