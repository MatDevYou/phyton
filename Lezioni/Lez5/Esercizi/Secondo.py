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
    '''
    Funzione genera

    parametri :
    n -> il range di quanti numeri deve generare
    
    La funzione crea un dizionario dove le chiavi sono i numeri
    da 1 a n e i valori sono i quadrati di questi numeri.
    '''

    # Inizializzo un dizionario vuoto
    dizionario = {}  
    # Itero attraverso i numeri da 1 a n inclusi
    for i in range(1, n + 1):  
        # Assegna al dizionario la chiave 'i' con il valore 'i' al quadrato
        dizionario[i] = i * i  
    return dizionario 

 # Chiedo all'utente di inserire un numero intero
n = int(input("inserisci quanti numeri vuoi generare : ")) 

# Stampo il dizionario generato dalla funzione 'genera'
print(genera(n))  



