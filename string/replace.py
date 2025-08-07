#dans cet exercice, on va apprendre a supprimer toutes les occurences
# du caractere c dans s


def delete_occurences(s,c):
    """supprime les occurences c dans s"""

    return s.replace(c,"")

if __name__ == '__main__':
    assert delete_occurences("lelbi",'l') == "ebi"