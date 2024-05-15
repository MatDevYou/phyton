'''

Autore: Matteo Meringolo
Data: 06/05/2024
Titolo:Progettare una funzione che accetti un numero indefinito di dizionari e restituisca un
dizionario che è la concatenazione di tutti i dizionari indicati come parametro formale alla
funzione. Scrivete uno script che utilizzi tale funzione.
Esempio:
diz1 = {'v1':1,'v2':2,'v3':3}
diz2 = {'v4':4,'v5':5,'v6':6}
diz3 = {'v7':7,'v8':8}
Dizionario restituito: {'v1': 1, 'v2': 2, 'v3': 3, 'v4': 4,
'v5': 5, 'v6': 6, 'v7': 7, 'v8': 8}

'''

def concatena(*dizionari):
    '''
    Funzione concatena

    parametri

    dizionari -> gli passo un numero di dizionari infinito
    
    La funzione prende un numero arbitrario di dizionari come input e
    restituisce un unico dizionario che è la combinazione di tutti i dizionari passati.
    '''
    # Inizializza un dizionario vuoto per memorizzare la somma dei dizionari
    somma = {}  
    # Itera attraverso tutti i dizionari passati come argomenti
    for i in dizionari:  
        # Unisce il dizionario corrente con 'somma' utilizzando l'operatore '|='
        somma |= i  
    return somma  

# Dichiaro 3 dizionari per testare la funzione
diz1 = {'v1': 1, 'v2': 2, 'v3': 3}
diz2 = {'v4': 4, 'v5': 5, 'v6': 6}
diz3 = {'v7': 7, 'v8': 8}

# Stampa il dizionario risultante dalla concatenazione dei tre dizionari
print(concatena(diz1, diz2, diz3))  
