try:
    a = int(input("Inserisci un numero: "))
    b = int(input("Inserisci un numero: "))
    risultato = a / b
    print("Il risultato è:", risultato)
except ZeroDivisionError:
    print("Divisione per zero, impossibile")
except ValueError:
    print("Valore non valido, inserisci un numero diverso")