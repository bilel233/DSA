# on va ici calculer la longueur d'une liste chainee


class Node:
    def __init__(self,val):
        self.val = val  # l'objet recoit la valeur val
        self.next = None # l'objet recoit None ; ie ; pointeur vers suivant


class List:
    def __init__(self):
        self.head = None # Au debut, la tete de la liste chainee est vide

    def longueur_linked_list(self):
        """methode qui renvoie le nombre de noeuds dans une liste chainee"""

        cpt = 0
        q = self.head
        while q is not None:
            cpt+=1
            q = q.next
        return cpt

# testons notre methode
    
if __name__ == '__main__':

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    # on va construire la liste chainee simple

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    # la liste est cree

    l = List()   # on cree la tete du pointeur
    l.head = n1
    length = l.longueur_linked_list()
    print(f"la longueur de la linked list est {length}")

        
# Note
# la tete d'une liste chainee permet d'acceder au noeud de la liste chainee
