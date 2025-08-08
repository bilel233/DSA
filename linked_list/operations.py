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

def count_nodes_recursive(head):
    """renvoie la longueur de la liste chainee"""

    if head is None:
        return 0
    
    return 1 + count_nodes_recursive(head.next)

# creons une fonction pour afficher les elt d'une liste chainee

def print_val(head):
    """
    affiche les elts d'une liste chainee
    """

    current = head
    while current is not None:
        print(f" {current.val} ",end="")
        if current.next is not None:
            print(f"->",end="")
        # sinon ne rien faire
        current=current.next
    print()

def print_val_recursive(head):
    """affiche les val de la liste chainee de maniere recursive"""

    if head is None:
        return
    print(head.val)
    print_val_recursive(head.next)


#creons une fonction pour chercher un elt dans la liste chaines
def search_key(head,key):
    """renvoie l'elt present dans la liste chaine. sinon -1"""

    current = head

    while current is not None:
        if current.val == key:
            return key
        # sinon ne ruen faire faire
        current = current.next
    return -1

# recherchons un elt nais de maniere recursive

def search_elt_recursive(head,key):
    """
    renvoie false si l'elt nest pas present dans la linked list
    """

    if head is None:
        return False
    elif head.val == key:
        return key
    else:
        return search_elt_recursive(head.next,key)
    

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

    print(f"testons la fonction recursive")

    assert count_nodes_recursive(n1) == 3

    print(f"le test est passe")

    print()

    print_val(n1)

    print()

    print_val_recursive(n1)

    # testons la fonctions search_key

    res = search_key(n1,-1)
    print(f"{res}")

    print()

    value = search_elt_recursive(n1,20)

    if value == 20:
        print("yep")
    else:
        print("Nop")

