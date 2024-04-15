'''
Autore: Matteo Meringolo
Data: 15/04/2024
Titolo: Scrivere un programma che legga i coefficienti a e b di un'equazione di primo grado ax=b e
ne scriva la soluzione (attenzione al dominio del coefficiente a)
'''


# Sezione di input Dati
# Inizializzazioni variabili
print("Questo programma risolve un'equazione di primo grado nella forma ax = b.")
# Leggi i coefficienti a e b dall'utente
a = float(input("Inserisci il coefficiente a: "))
b = float(input("Inserisci il coefficiente b: "))

# Verifica se a è diverso da zero (perché non possiamo dividere per zero)
if a != 0:
    # Calcola la soluzione e stampala
    soluzione = b / a
    print("La soluzione dell'equazione è:", soluzione)
elif b == 0:
        print("L'equazione è indeterminata: ha infinite soluzioni.")
else:
        print("L'equazione è impossibile: non ha soluzioni.")

    



