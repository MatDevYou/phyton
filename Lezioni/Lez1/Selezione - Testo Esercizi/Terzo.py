'''
Autore: Matteo Meringolo
Data: 15/04/2024
Titolo: Scrivere un programma che legga il raggio r di una circonferenza e ne calcoli l'area e la
lunghezza.
'''
#dichiarazione raggio e delle formule riguardanti area e lunghezza
r = float(input("Inserisci raggio: "))

area = 3.1415 * r ** 2
circonferenza = 2 * 3.1415 * r

if r < 0:
    print("Impossibile")
else:
    print("Area: ", area)
    print("Circonferenza: ", circonferenza)

