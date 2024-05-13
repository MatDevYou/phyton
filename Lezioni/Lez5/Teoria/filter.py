# funzioni che filtrano le vocali
def funLista(carattere):
    vocali = ['a', 'e', 'i', 'o', 'u']
    
    return carattere not in vocali
def funTupla(carattere):
    vocali = ('a', 'e', 'i', 'o', 'u')
    return carattere not in vocali

def funStringa(carattere):
    vocali = "aeiou"
    return carattere not in vocali

#suddiidere valori in due classi
# Sequenze
lista = ['e', 's', 'e', 'm', 'p', 'i', 'o']
tupla = ('e', 's', 'e', 'm', 'p', 'i', 'o')
stringa = 'esempio'
# filtraggio delle sequenze
filtered = filter(funLista, lista)
print(type(filtered))
for consonante in filtered:
    print(consonante,end = " ") #per stampare su stessa linea
print()

filtered = filter(funTupla, tupla)
for consonante in filtered:
    print(consonante,end = " ")
print()

filtered = filter(funStringa, stringa)
for consonante in filtered:
    print(consonante,end = " ")
