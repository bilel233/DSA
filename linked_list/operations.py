# dans cet exercice, nous allons voir le soperations
# realisables pour les linked lists


class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


def count_nodes(head):
    """renvoie la longueur de la liste chainee"""

    cpt = 0

    current = head

    while current is not None:
        cpt = cpt + 1
        current = current.next

    return cpt

if __name__ == '__main__':
    # on va hardcoder la linked list

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    n1.next = n2
    n2.next = n3
    n3.next = None

    assert count_nodes(n1) == 3
    assert count_nodes(n1) != 0