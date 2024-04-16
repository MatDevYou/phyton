'''
Autore: Matteo Meringolo
Data: 15/04/2024
Titolo:Scrivere un programma che chieda quanti alunni ci sono in una classe poi per ogni alunno
fa inserire M voti, M dato in input, e ne scrive la media.

'''

alunni = int(input("Quanti studenti ci sono? "))
M = int(input("Quanti voti per ogni studente? "))

for i in range(alunni):
    totale_voti = 0
    print("\nAlunno", i+1)
    for j in range(M):
        voto = float(input("Inserisci il voto : "))
        totale_voti += voto
    media = totale_voti / M
    print("Media dell'alunno", i+1, ":", media)
