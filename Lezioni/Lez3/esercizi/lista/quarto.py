'''
Autore: Matteo Meringolo
Data: 20/04/2024
Titolo: 
Scrivere un programma Python per dividere una data lista in due parti in cui viene data la
lunghezza della prima parte della lista.
Esempio:
Lista originale: [1, 1, 2, 3, 4, 4, 5, 1]
Lunghezza della prima parte della lista: 3
Output : Prima parte: [1, 1, 2] ,
Seconda parte: [3, 4, 4, 5, 1]
'''

def dividereLista(lista, lunghezza):
    '''
    Funzioen dividereLista

    parametri

    lista -> inserisco la stringa che voglio verifica
    lunghezza -> quanto voglio dividere la stringa
    '''
    # Verifica se la lunghezza della prima parte è valida
    if lunghezza < 0 or lunghezza > len(lista):
        return "Errore: La lunghezza della prima parte non è valida"

    # Divide la lista in due parti
    primaParte = lista[:lunghezza]
    secondaParte = lista[lunghezza:]

    # Restituisce il risultato formattato
    return "Prima parte: " + str(primaParte) + ", Seconda parte: " + str(secondaParte)

# Lista originale e lunghezza della prima parte
lista = [1, 1, 2, 3, 4, 4, 5, 1]
lunghezza = 3

# Chiama la funzione e stampa il risultato
print(dividereLista(lista, lunghezza))
