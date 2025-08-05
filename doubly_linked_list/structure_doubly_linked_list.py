# dans cet exercice, on va apprendre la structure
# d'une liste doublement chainee

class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    # on construit la liste chainee hardcoder

    n1.prev = None
    n1.next = n2
    n2.prev = n1
    n2.next = n3
    n3.prev = n2
    n3.next = None

    print(f"{n1.data}")
    print(f"{n1.next.next.data}")