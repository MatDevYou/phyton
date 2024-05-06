lista = [10,3,7,1,9,3,2,4,6,8]
tupla = (10,3,7,1,9,3,2,4,6,8)
stringa = "abdc45hyydsa"
print(lista[2:4])
print(tupla[2:4])
print(stringa[2:4])
print(lista[4:])
print(tupla[4:])
print(stringa[4:])
print(lista[:4])
print(tupla[:4])
print(stringa[:4])
print(lista[4])
print(tupla[4])
print(stringa[4])
print(lista[-4:])
print(tupla[-4:])
print(stringa[-4:])
print(lista[:-4])
print(tupla[:-4])
print(stringa[:-4])
print()
print()

stringa = "abdcdefghilmn"
print(stringa[2:8:
    2]) #012 e prendo d poi salto di 2 e prendo d e poi f e mi fermo perche il limite è 8
print(stringa[::3])#prendo solo caratteri ogni 3 posizioni
print(stringa[::-1])#capovolgi stringa
print(stringa[::-2])#al contrario saltando di 2