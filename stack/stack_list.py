# dans cet exercice on va apprendre a implementer une stack de differentes
# facon


# on suit le principe LIFO

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

    


