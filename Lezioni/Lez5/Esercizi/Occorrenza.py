'''

Autore: Matteo Meringolo
Data: 06/05/2024
Titolo:Data una lista si vuole cercare tutte le ricorrenze di un elemento inserito in input. 
Tale ricerca deve essere effettuata utilizzando esclusivamente il metodo index e il metodo count della lista. 
    In output si vogliono le posizioni dell'elemento cercato.

Es: INPUT:  Lista = [1, 3, 4, 5, 3, 3] elemento = 3
OUTPUT: elemento 3 si trova alle posizioni: 1,4,5
'''

def creaLista(n, lista):

    '''
    funzione creaLista

    parametri
    n -> indica la lunghezza della lista
    lista -> lista vuota che viene riempita dall'input
    '''
    # Cicla n volte per ottenere gli elementi della lista
    for i in range(n):
        # Aggiunge ogni elemento inserito dall'utente alla lista
        elemento = int(input("Inserisci un elemento nella lista: "))
        lista.append(elemento)
    # Restituisce la lista aggiornata
    return lista

# Chiede all'utente quanti numeri vuole nella lista
n = int(input("Quanti numeri vuoi nella lista: "))

# Inizializza una lista vuota
lista = []

# Chiama la funzione creaLista per riempire la lista
creaLista(n, lista)

# Chiede all'utente quale elemento cercare nella lista
elemento = int(input("Inserisci elemento da cercare: "))

# Inizializza una lista per memorizzare le posizioni dell'elemento
posizioni = []

# Utilizza il metodo count per determinare quante volte l'elemento appare nella lista
conteggio = lista.count(elemento)

# Usa il metodo index in un ciclo per trovare tutte le posizioni dell'elemento
indiceInizio = 0
for i in range(conteggio):
    # Trova l'indice dell'elemento partendo dall'indice di inizio
    indice = lista.index(elemento, indiceInizio)
    # Aggiunge l'indice alla lista delle posizioni
    posizioni.append(indice)
    # Aggiorna l'indice di inizio per la prossima ricerca
    indiceInizio = indice + 1

# Stampa il risultato
if posizioni:
    print(f"Elemento {elemento} si trova alle posizioni: {posizioni}")
else:
    print(f"L'elemento {elemento} non è presente nella lista.")
