'''

Autore: Matteo Meringolo
Data: 13/05/2024
Titolo:Scrivete uno script Python per generare e stampare un dizionario che contenga un numero
(compreso tra 1 e n) nella forma (x, x*x).
Esempio:
n = 5
Dizionario: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

'''

def genera(n):
    dizionario = {}
    for i in range(1, n + 1):
        dizionario[i] = i * i
    return dizionario

n = int(input("inserisci quanti numeri vuoi generare : "))

print(genera(n))


