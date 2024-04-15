'''
Autore: Matteo Meringolo
Data: 15/04/2024
Titolo:Si hanno in input N saldi di conti correnti bancari. Si vuole in output la media aritmetica dei
soli conti correnti che hanno un saldo negativo.
'''

# Input del numero di saldi
N = int(input("Quanti saldi ci sono: "))

# Inizializzazione della somma e del conteggio
s = 0
negativi = 0

# Ciclo per chiedere i saldi e calcolare la somma dei saldi negativi
for i in range(N):
    saldo = float(input("Inserisci il saldo del conto : "))
    if saldo < 0:
        s += saldo
        negativi += 1

# Calcolo della media solo se ci sono saldi negativi
if negativi > 0:
    media = s / negativi
    print("La media aritmetica dei soli conti correnti con saldo negativo è:", media)
else:
    print("Non ci sono conti correnti con saldo negativo.")
