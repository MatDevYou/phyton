'''
Autore: Matteo Meringolo
Data: 22/04/2024
Titolo:Conversione temperatura: implementare una funzione convertiCF che converta una
temperatura espressa in gradi Fahrenheit in una temperatura espressa in gradi Celsius.
Usare la seguente formula:
F = ( 9 / 5 ) * C + 32
Creare un programma principale che richiami la funzione e ne stampi il risultato
visualizzando solo 3 cifre decimali.


'''
##
## Funzioni:
##
'''
def fun(param1: int, param2: float) -> int:

Funzione: convertiCF

Parametri formali:
float celsius -> inserimento di gradi celsius per la conversione


Valore di ritorno:
f -> ritorno il risultato della formula per la conversione

'''

def convertiCF (celsius: float) -> float:
    f = ( 9 / 5 ) * celsius + 32
    return f

a = float(input("inserisci gradi: "))

if a < -273.15:
    print("Impossibile")
else:
    print("%.2f" % convertiCF(a))

