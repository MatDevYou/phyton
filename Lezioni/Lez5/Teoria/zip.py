#accetta sequenza e dizionari, iterabili
lista=[1, 2, 3, 4]
stringa="abcd"
zipped=zip(lista,stringa)
print(type(zipped))
print(zipped)

for ele in zipped:
    print(ele)

for ele in zip(lista):
    print(ele)