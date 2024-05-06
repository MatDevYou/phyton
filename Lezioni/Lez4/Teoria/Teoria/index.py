#ricerca elemento con index
lista = [10,3,7,1,9,3,2,4,6,8]
tupla = (10,3,7,1,9,3,2,4,6,8)
stringa = "abdc45hyydsa"
print(lista.index(3))
print(tupla.index(3))
print(stringa.index('d'))
print(lista.index(3,4))
print(lista.index(3,4,10))
print(lista.index(-2))

#altro metodo ma con in
lista = [10,3,7,1,9,3,2,4,6,8]
print(1 in lista)
print(-2 in lista)
print(-2 not in lista)
