'''
Autore: Matteo Meringolo
Data: 20/04/2024
Titolo: Scrivi un programma per trovare il secondo numero più piccolo in una lista.
'''

def minimo(lista):
    '''
    Funzione minimo

    parametri
    lista -> li passo la lista da controllare

    '''

    #faccio un controllo dato che la consegna dice che devo trovare il secondo numero piu piccolo
    if len(lista) < 2:
        return "La lista non ha abbastanza elementi"
    
    minimo = min(lista)  # Trovo il minimo nella lista
    lista.remove(minimo)  # Rimuovo il minimo dalla lista
    secondo = min(lista)  # Trovo il minimo nella lista modificata
    
    return secondo

lista = [1, 9, 3]
print(minimo(lista))


