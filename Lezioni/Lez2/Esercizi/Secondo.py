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

#pari scritto con * prima significa che accetta argomenti variabili , è dinamico posso mettere quanti numeri voglio
def sommaProdotto(*pari: float) -> tuple:
    '''
    Funzione: sommaProdotto

    Parametri formali:
    float pari -> inserimento di n numeri pari

    Valore di ritorno:
    somma, dispari -> ritorno la somma se sono numeri pari e il prodotto se sono numeri dispari

    '''
    somma = 0
    dispari = 1
    for num in pari:
        if num % 2 == 0:
            somma += num
        else:
            dispari *= num
    return somma, dispari

#definisco un array di numeri con all'interno numeri pari e dispari
numeri = (2, 8)

#salvo i risultati delle funzio
risultatoSomma, risultatoProdotto = sommaProdotto(*numeri)

#output dove stampo il risultato della somma dei numeri pari e il risultato del prodotto dei numeri dispari
print("Risultato somma:", risultatoSomma)
print("Risultato prodotto:", risultatoProdotto)


