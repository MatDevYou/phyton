'''
Autore: Matteo Meringolo
Data: 15/04/2024
Titolo:Scrivere un programma che legga N numeri da tastiera, N dato in input, e ne restituisca il
minimo.
'''

# input di quanti numeri vuoi inserire
numeri = int(input("Quanti numeri vuoi passare in input: "))

# inizializzazione del minore al primo numero inserito
minore = int(input("Inserisci il primo numero: "))

# eseguo un ciclo che vada da 1 a N-1 (poiché abbiamo già inserito il primo numero)
for i in range(1, numeri):
    n = int(input("Inserisci il numero successivo: "))
    if n < minore:
        minore = n
        
    
print("Il minore è:", minore)

