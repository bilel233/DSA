# dans cet exercice on va apprendre a implementer une stack de differentes
# facon


# on suit le principe LIFO

from collections import deque

if __name__ == '__main__':

    stack = []      # la structure de list est utilise comme une pile.
    stack.append('a') # append joue le meme role que append
    stack.append('b')
    stack.append('c')

    print(f"voici ma stack {stack}")

    # on va utiliser la methode pop.

    stack.pop()
    print(f"on extrait un elt selon l'ordre LIFO {stack}")
    stack.pop()
    print(f"on extrait un elt selon l'ordre LIFO {stack}")
    stack.pop()
    print(f"on extrait un elt selon l'ordre LIFO {stack}")

    print(f"Voici l'etat de ma pile {stack}")

    # on va maintenant travailler avec dequeue()

    deq = deque()

    deq.append('a')
    deq.append('b')
    deq.append('c')

    print(f"{deq}")

    print("suppression des elts dans la dequeue")

    deq.pop()
    print(f"{deq}")
    deq.pop()
    print(f"{deq}")
    deq.pop()
    print(f"{deq}")

    # que se passe quand la dequeue est vide ?

    #deq.pop() impossible qd la dequeue est vide 





