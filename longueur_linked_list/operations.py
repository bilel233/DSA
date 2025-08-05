# dans cet exercice, on va revoir les operations
# des listes chaines


class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

# on a cree une classe noeud qui va symboliser le noeud d'une
# liste chainee

def longueur(head):
    """renvoie la longueur d'une liste chainee"""

    cpt = 0
    q = head
    while q is not None:
        cpt+=1
        q = q.next

    return cpt

if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    l = longueur(n1)
    print(f"{l}")

    # on lit les noeuds. on harcode la liste chainee simple

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = None

    # on rappelle la fonction longueur

    assert longueur(n1) == 4