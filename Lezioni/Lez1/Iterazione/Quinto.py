'''
Autore: Matteo Meringolo
Data: 15/04/2024
Titolo:Scrivere un programma che chieda quanti alunni ci sono in una classe poi per ogni alunno
fa inserire M voti, M dato in input, e ne scrive la media.

'''
#dichiaro in input alunni e M che sarebbe il numero di voti che gli studenti hanno 
alunni = int(input("Quanti studenti ci sono? "))
M = int(input("Quanti voti per ogni studente? "))

#inizio il ciclo con gli alunno cosi ogni volta che inizio il ciclo mi stampa il numero dello studente 
for i in range(alunni):
    totale_voti = 0
    print("\nAlunno", i+1)
#in questo ciclo invece ho creato una variabile voto dove l'utente puo inserire il voto dello studente
    for j in range(M):
        voto = float(input("Inserisci il voto : "))
        totale_voti += voto #mi salvo nella variabile totale_voti il numero di voti che ha messo l'utente cosi ci permette di fare la media
    media = totale_voti / M
    print("Media dell'alunno", i+1, ":", media)
