# dans cet exercice, on va implementer les operations des stack

# d'abord, l'operation push

stack = []

stack.append(1) 
stack.append(2) # 2 au dessus de la pile , en haut
stack.append(3)
stack.append(4)
stack.append(5) # 5 au dessus de la pile

#print(f"{stack}")

while stack != []:
    print(stack[-1])
    stack.pop()


# operation de suppression de la pile , pop()

stack_new = []

stack_new.append(0)
stack_new.append(1)
stack_new.append(2)
stack_new.append(3)
print(f"la stack au depart : {stack_new}")
elt = stack_new.pop() # 3 est elt au dessus de la pile
print(f"{stack_new} et elt retire est {elt}")
print('######################################################')

# maintenant on va voir l'operation pour renvoyer l'elelemt au sommet de la pile

def topElelemt(stack):
    """renvoie l'elt au sommet de la pile"""

    return stack[-1]
# on teste maintenant
stack_1 = []

stack_1.append(1)
stack_1.append(2)
stack_1.append(3)

print(f"voici ma pile au depart : {stack_1}")
top_element = topElelemt(stack_1)

print(f"{top_element}")
#print(f"voici ma stack : {stack_1}")

