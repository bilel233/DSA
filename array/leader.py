# dans cet exercice, on cherche l'element leader d'une liste


def leader(arr):
    """
    renvoie une liste contenant les elements leaders de arr
    """

    L = list()

    for i in range(0,len(arr)):
        for k in range(i+1,len(arr)):
            if arr[i] < arr[k]:
                break   # on sort d ela boucle et on avance
        # arriver ici, c'est check
        else:
            L.append(arr[i])

    return L

if __name__ == "__main__":
    print(leader([16,17,4,3,5,2]))