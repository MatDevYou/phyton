'''
Autore: Matteo Meringolo
Data: 20/04/2024
Titolo: Scrivere un programma python che rimuova gli elementi duplicati da una lista.
Esempio:
listaIN = [2, -4 ,5,6,5,5,2]
listaOUT=[2,-4,5,6]
'''

#dichiaro una lista da verificare
lista = [2, -4, 5, 6, 5, 5, 2]

#in questa variabile uso il set, mi aiuta a eliminae i duplicati presenti nella lista
noDuplicati = list( set(lista))

#output lista normale e lista senza duplicati
print("listaIN =", lista)
print("listaOUT =", noDuplicati)

