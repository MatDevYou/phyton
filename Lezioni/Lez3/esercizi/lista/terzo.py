'''
Autore: Matteo Meringolo
Data: 20/04/2024
Titolo: Scrivi un programma per trovare il secondo numero più piccolo in una lista.
'''

def minimo(lista):
    if len(lista) < 2:
        return "La lista non ha abbastanza elementi"
    
    minimo = min(lista)  # Trova il minimo nella lista
    lista.remove(minimo)  # Rimuove il minimo dalla lista
    secondo = min(lista)  # Trova il minimo nella lista modificata
    
    return secondo

lista = [1, 9, 3]
print(minimo(lista))


