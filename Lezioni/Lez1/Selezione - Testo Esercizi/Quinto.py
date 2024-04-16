'''
Autore: Matteo Meringolo
Data: 15/04/2024
Titolo: Un negoziante per ogni spesa di importo superiore a 100 € effettua uno sconto del 5%, se
l’importo risulta superiore a 300€ lo sconto è del 10%. Scrivere un programma che richieda
all'utente l'ammontare della spesa e visualizzi quindi l'importo effettivo da pagare.
'''
#dichiarazione variabili
spesa = float(input("Inserisci importo della spesa: "))

#se la spesa è superiore di 300 applico uno sconto di 10%
if spesa > 300:
    sconto = spesa * 0.10
    totale = spesa - sconto
    print("Spesa: ",spesa,"Sconto: 10%",sconto,  "Totale: ", totale )
elif spesa > 100:
#se la spesa è superiore di 300 applico uno sconto di 5%
    sconto = spesa * 0.05
    totale = spesa - sconto
    print("Spesa: ",spesa,"Sconto: 5%",sconto,  "Totale: ", totale )
else:
    print("Nessuno sconto applicabile perche la spesa è inferiore a 100")
