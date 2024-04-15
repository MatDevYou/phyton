'''
Autore: Matteo Meringolo
Data: 15/04/2024
Titolo:Leggere una successione di numeri interi passati dall’utente, fermandosi al primo numero
che rende la successione non crescente e restituendo quanti numeri formano la
successione inserita.
'''
#input di quanti numeri vuoi inserire
numeri = int(input("Quanti numeri vuoi passare in input: "))

#dichiarazione delle variabili
maggiore = 0
contatore = 0

#eseguo un ciclo che vada da i a il numero di input che ho inserito
for i in range(numeri):
    n = int(input("Inserisci i numeri che vuoi: "))
    if n > maggiore:
        maggiore = n
        contatore +=1

print ("Lunghezza:", contatore)
