'''
Autore: Matteo Meringolo
Data: 22/04/2024
Titolo:Creare una funzione che abbia come parametri formali un numero arbitrario di valori
numerici. Si vuole che restituisca la somma dei soli numeri pari e il prodotto dei soli numeri
dispari. Successivamente creare un programma che richiami tale funzione e che stampi in
output i risultati . No standard input.

'''
##
## Funzioni:
##
'''
def fun(param1: int, param2: float) -> int:

Funzione: sommaProdotto

Parametri formali:
float pari -> inserimento di n numeri pari


Valore di ritorno:
somma, dispari -> ritorno la somma se sono numeri pari e il prodotto se sono numeri dispari

'''

def sommaProdotto(*pari: float) -> tuple:
    somma = 0
    dispari = 1
    for num in pari:
        if num % 2 == 0:
            somma += num
        else:
            dispari *= num
    return somma, dispari

#definisco un array di numeri con all'interno numeri pari e dispari
numeri = (2, 3, 8, 3)

#salvo i risultati delle funzio
risultatoSomma, risultatoProdotto = sommaProdotto(*numeri)

print("Risultato somma:", risultatoSomma)
print("Risultato prodotto:", risultatoProdotto)


