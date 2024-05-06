'''
Autore: Matteo Meringolo
Data: 06/05/2024
Titolo:Scrivere un programma per sostituire l'ultimo valore delle liste in una tuple
con un valore richiesto in input.
Esempio:
valore : 100
TuplaIN: ([10, 20, 40], [40, 50, 60], [70, 80, 90])
TuplaOUT: ([10, 20, 100], [40, 50, 100], [70, 80, 100])
'''

def aggiornaLista(t1, valore):
    tuplaModificata = []

    for lista in t1:
        ultimoElemento = lista.index(lista[-1])  # Trova l'indice dell'ultimo elemento
        listaModificata = lista[:ultimoElemento] + [valore]  # Sostituisci l'ultimo elemento con il valore inserito
        tuplaModificata.append(listaModificata)
    
    return tuplaModificata


tupla = ([10, 20, 40], [40, 50, 60], [70, 80, 90])

valore = int(input("Inserisci il valore da sostituire: "))

print(aggiornaLista(tupla, valore))
