'''
Autore: Matteo Meringolo
Data: 15/04/2024
Titolo: Scrivere un programma che legga le lunghezze dei tre lati di un triangolo a, b, c e ne calcoli
il perimetro e l'area S, quest'ultima tramite la formula di Erone dove p è il semiperimetro.
'''

# Sezione di input Dati
a = float(input("Inserisci il lato a: "))
b = float(input("Inserisci il lato b: "))
c = float(input("Inserisci il lato c: "))

# Calcolo del perimetro
perimetro = a + b + c

# Calcolo del semiperimetro
p = perimetro / 2

# Calcolo dell'area utilizzando la formula di Erone
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

# Stampa risultati
print("Il perimetro del triangolo è:", perimetro)
print("L'area del triangolo è:", s)
