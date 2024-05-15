'''

Autore: Matteo Meringolo
Data: 13/05/2024
Titolo:Scrivete un programma Python per rimuovere i duplicati dal dizionario.

'''

diz = {'v1':1,'v2':2,'v3':3, 'v4':6, 'v5':1}

for chiave in diz:
    if diz[chiave] == diz[chiave]:
        print(diz)


