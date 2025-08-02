# on va creer une classe d'une structure de donnee qui est la linked_list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


if __name__ == '__main__':
    n1 = Node(1)
    print(n1.data)
    print()
    n2 = Node(2)
    n3 = Node(3)
    n1.next = n2
    n2.next = n3
    print(n1.data)
    print(n2.data)
    print(n3.data)
    


