'''
Autore: Matteo Meringolo
Data: 06/05/2024
Titolo:Scrivere un programma per invertire una tupla
Esempio:
tpleIN=(‘a’,’c’,f’)
tpleOUT=(‘f’,‘a’,’c’)
'''

def controlloTupla(t1):
    '''
    funzione controlloTupla

    parametri:
    t1 -> li passiamo la tupla da far controllare
    
    '''
    if not t1:  # Controlla se la tupla è vuota
        return "Tupla vuota"
    else:
        return "Tupla normale: " + str(t1) + ", Tupla invertita: " + str(t1[::-1])

#dichiaro la tupla
tupla = ('a', 'c', 'f') 

#output richiamdando la funzione
print(controlloTupla(tupla))




