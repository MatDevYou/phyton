'''
Autore: Matteo Meringolo
Data: 22/04/2024
Titolo:La seguente è la formula per valutare numericamente il numero di Nepero e:
(1)
4.a Scrivere una funzione che restituisca un valore approssimato di e all'ennesimo termine,
dove N è inserito come parametro formale alla funzione.
Esempio: 
valuta_e(3) restituirà il valore di e calcolato con tre termini della (1), cioè:
e= 1/0! + 1/1! + 1/2! = 1 + 1 + 0.5 = 2.5
La funzione calcola_e deve richiamare la funzione di calcolo del fattoriale.
Scrivere il codice della funzione e il programma principale che la chiama chiedendo in input
il numero N.
4.b Supponendo di porre il numero di Nepero = 2.718281828459045 dico che
errore = valuta_e(N) - Nepero
sia l'errore che commetto nella valutazione di e.
Modificare la funzione che restituisce la valutazione di e con N termini andando a far
restituire anche l'errore commesso nella valutazione. Suggerimento: la funzione valuta_e(N)
dovrà restituire due valori, 2.718281828459045 potrebbe essere memorizzato in una
variabile globale.
esempio: valuta_e(3) restituisce il valore calcolato nel punto 4.a 2.5 e 0,218281828459045
che rappresenta la differenza tra 2.718281828459045 e 2.5

'''
#dichiarazione variabile
Nepero = 2.718281828459045 

#definisco funzione che esegue un ciclo 
def valuta(n):
    '''
    Funzione: valuta
    
    Parametri formali:
    e , fattoriale -> 
    '''
    e = 0
    fattoriale = 1
    for i in range(n):
        e += 1 / fattoriale
        fattoriale *= (i + 1)
        errore = Nepero - e
    return e, errore

#inserisci numero che vuoi fattorizzare
n = int(input("Inserisci numero: "))
risultato = valuta(n)
print("Il valore approssimato di",n ,"e calcolato è:", risultato)

    