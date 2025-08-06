# dans cet exercice, nous allons voir les operations pour les 
# listes doublement chaines


class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

def affichage_elements(head):
    """affiche les elts d ela liste doublements chaines"""

    q = head 
    while q is not None:
        print(f"val = {q.val}")
        q = q.next

def affichage_reverse(head):
    """affiche les elts de la liste a l'envers"""

    q = head
    while q is not None:
        r = q
        q = q.next

  

    while r != None:
        print(f"{r.val}")
        r = r.prev
    

# travaillons maintenant avec une fonction recursive

def affichage_recursive(head):
    """affiche les valeurs de la liste de maniere recursive"""

    if head is None:
        return # on sort de la fonction sans renvoyer aucune valeur
    else:
        print(f"{head.val}",end= " ")
        affichage_recursive(head.next)

def reverse_affichage(tail):
    """affiche les elts mais dans l'ordre inversee"""

    reverse = tail
    while reverse is not None:
        print(f"{reverse.val}",end= " ")
        reverse = reverse.prev
    
# passons aux operations d'insertions

def insertion_debut(head,val):
    """
    insert un noeud au debut de la liste chainee
    """

    node = Node(val)
    #if head is None:
     #   return node
    
    node.next = head
    head.prev = node
        
    return node


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 =  Node(5)

    # on construit la liste chaines en hardcodant

    n1.next = n2
    n1.prev = None
    n2.prev = n1
    n2.next = n3
    n3.prev = n2
    n3.next = n4
    n4.prev = n3
    n4.next = n5
    n5.prev = n4
    n5.next = None

    affichage_elements(n1)
    print()
    affichage_reverse(n1)

    print()

    affichage_recursive(n1)

    print("\n")
    reverse_affichage(n5)
    print("\n")
    # go pour tester l'insertion au debut de la liste chainee
    insertion_debut(n1,10)
    affichage_elements(n1.prev)