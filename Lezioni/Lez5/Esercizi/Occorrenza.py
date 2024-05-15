'''

Autore: Matteo Meringolo
Data: 06/05/2024
Titolo:Data una lista si vuole cercare tutte le ricorrenze di un elemento inserito in input. 
Tale ricerca deve essere effettuata utilizzando esclusivamente il metodo index e il metodo count della lista. 
    In output si vogliono le posizioni dell'elemento cercato.

Es: INPUT:  Lista = [1, 3, 4, 5, 3, 3] elemento = 3
OUTPUT: elemento 3 si trova alle posizioni: 1,4,5


'''

def ricerca(lista):
    


# Chiede all'utente quanti numeri vuole nella lista
n = int(input("Quanti numeri vuoi nella lista: "))

# Inizializza una lista vuota
lista = []

# Cicla n volte per ottenere gli elementi della lista
for i in range(n):
    # Aggiunge ogni elemento inserito dall'utente alla lista
    elemento = int(input("Inserisci un elemento nella lista: "))
    lista.append(elemento)

# Stampa la lista risultante
print("Lista:", lista)
