'''
Autore: Matteo Meringolo
Data: 22/04/2024
Titolo: Creare una funzione che riceva una quantità di tempo in formato ore, minuti e secondi e la
restituisca espressa solamente in secondi. Successivamente creare un programma
principale che chieda in input due quantità di tempo e stampi in output quale quantità di
tempo è maggiore. La funzione deve avere i parametri formali con valori predefiniti.
'''
##
## Funzioni:
##



def secondi(ore  : int = 0, minuti : int = 0, secondi : int = 0):
    '''
Funzione: secondi

Parametri formali:
int ore -> descrizione ore
int minuti -> descrizione minuti
int secondi -> descrizione secondi

Valore di ritorno:
totaleSecondi -> descrizione valore di ritorno

Funzione: confrontaTempo

Parametri formali:
int t1 -> descrizione del tempo 1
int t2 -> descrizione del tempo 1

Valore di ritorno:
 -> mi stampa quale dei due parametri messi prima ha il valore maggiore

'''
    totaleSecondi = ore * 3600 + minuti * 60 + secondi
    return totaleSecondi

def confrontaTempo(t1, t2):
    '''
    Funzoine. confrontaTempo
    
    Parametri formali:
    t1 e t2 -> indicano i due tempi inserisci dall'utente
    '''
    if t1 > t2:
        print("\nT1 è maggiore di T2")
    elif t2 > t1:
        print("\nT2 è maggiore di T1")
    else:
        print("\nil tempo è uguale")
        
def inserisciTempo():
    while (ora1 < 0) or (ora1 > 23):
        ora1 = int(input("Inserisci ora: "))
        

#inserisci i parametri del tempo 1
print("Inserisci TEMPO 1")
ora1 = int(input("Ora: "))
min1 = int(input("Minuto: "))
sec1 = int(input("Secondi: "))

#inserisci i parametri del tempo 2
print("\nInserisci TEMPO 2")
ora2 = int(input("Ora: "))
min2 = int(input("Minuto: "))
sec2 = int(input("Secondi: "))

#salvo nel tempo 1 e 2 i valori dei secondi calcolato con la funzione
tempo1 = secondi(ora1, min1, sec1)
tempo2 = secondi(ora2, min2, sec2)

confrontaTempo(tempo1, tempo2)


#while not 0 <= ora1 <= 23: uguale al while scritto sopra ma piu corta e capibile