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

def concatena(*dizionario):
    '''
    Funzione concatena

    parametri

    dizionario -> gli passo un numero di dizionari infinito
    
    '''
    somma = { }
    for i in dizionario:
        somma |= i
    return somma 


#dichiaro 3 dizionari per il momento per testare la funzione
diz1 = {'v1':1,'v2':2,'v3':3}
diz2 = {'v4':4,'v5':5,'v6':6}
diz3 = {'v7':7,'v8':8}


#output
print(concatena(diz1,diz2,diz3))