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


