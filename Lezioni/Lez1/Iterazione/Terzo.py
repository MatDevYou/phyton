'''
Autore: Matteo Meringolo
Data: 15/04/2024
Titolo:Leggere una successione di numeri interi passati dall’utente, fermandosi al primo numero
che rende la successione non crescente e restituendo quanti numeri formano la
successione inserita.
'''

numeri = int(input("Quanti numeri vuoi passare in input: "))

maggiore = int
contatore = 0

for i in numeri:
    n = int(input("Inserisci i numeri che vuoi: "))
    if n > maggiore:
        maggiore = n
        contatore +=1

print ("Lunghezza:", contatore)