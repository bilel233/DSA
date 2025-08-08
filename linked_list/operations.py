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


# voyons maintennat les operations d'insertions pour la linked list

def insert_begining(head,val):
    """insere un nouveau noeud au debut de las liste chainee"""

    new_node = Node(val)

    new_node.next = head

    head = new_node

    return new_node

def insert_node_position(head,key,new_data):
    """insere un noeud a une position specifique"""

    current = head

    while current is not None:
        if current.val == key:
            break
        current=current.next

    if current is None:
        print("la cle pour le noeud n'existe pas")
        return head
    
    #dans l'autre cas on commence la creation du noeud

    new_node = Node(new_data)

    new_node.next = current.next
    current.next = new_node

    return head



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

    print("testons la fonction insert\n")

    #new_node = Node(100)
    res = insert_begining(n1,100000)

    print_val_recursive(res)
    print()

    res_new = insert_node_position(n1,2,-102)
    print_val_recursive(res)