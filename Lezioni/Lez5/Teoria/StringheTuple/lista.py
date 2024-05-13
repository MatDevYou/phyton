def funLista(lista):
    for i in range(len(lista)):
        lista[i] *=2
    return lista

l=[1,2,3,4]
print(funLista(l))
print(l)