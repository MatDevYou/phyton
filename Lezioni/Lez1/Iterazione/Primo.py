'''
Autore: Matteo Meringolo
Data: 15/04/2024
Titolo:Si hanno in input due numeri reali A e B e una successione di numeri reali positivi che
termina con il valore 0. Si vuole in output la media dei soli numeri compresi tra A e B.
'''
# Dichiarazione delle variabili
A = float(input("Inserisci il numero reale a (maggiore di zero): "))
B = float(input("Inserisci il numero reale b (maggiore di zero): "))
somma = 0
count = 0
i = 1

# Controllo se A e B sono numeri reali e se fossero reali allora accumula i numeri e conta quanti sono
while i != 0:
    n = float(input("Inserisci un numero reale positivo (inserisci 0 per terminare): "))
    if n < 0:
        break
    if A < n < B:
        somma += n
        count += 1

# Calcolo della media solo se sono stati inseriti numeri compresi tra A e B
if count > 0:
    media = somma / count
    print("La media dei numeri compresi tra", A, "e", B, "è:", media)
else:
    print("Non sono stati inseriti numeri compresi tra", A, "e", B)
