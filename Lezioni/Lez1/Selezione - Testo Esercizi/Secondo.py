'''
Autore: Matteo Meringolo
Data: 15/04/2024
Titolo: Scrivere un programma che legga i coefficienti a, b e c di un'equazione di secondo grado
ax2+bx+c=0 e ne scriva le soluzioni.
'''

# Sezione di input Dati
a = float(input("Inserisci il coefficiente a: "))
b = float(input("Inserisci il coefficiente b: "))
c = float(input("Inserisci il coefficiente c: "))

delta = b **2 - 4*a*c #mi salvo la formula del delta in una variabile



if delta > 0: 
    #2 soluzioni
    x1 = (-b - delta**0.5 / 2 * a)
    x2 = (-b + delta**0.5 / 2 * a)
    print("Le soluzioni sono:", x1, "e", x2)
elif delta == 0:
    #soluzione reale doppia
    x = (-b / 2 * a)
    print("x: ", x)
else:
    #nessuna soluzione reale
    print("impossibile")


    



