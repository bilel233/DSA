# dans cet exercice on va apprendre a supprimer un caractere c dans s a
# une position specifique pos

def suppression(s,pos):
    """suppression d'un caractere a une position donnee"""

    if pos < 0 or pos >=len(s):
        return -1
    return s[0:pos] + s[pos+1:len(s)]

# on teste maintenant

if __name__=="__main__":
    assert suppression("bilel",0) == "ilel"
    assert suppression("bilel",1) == "blel"
    assert suppression("bilel",10) == -1