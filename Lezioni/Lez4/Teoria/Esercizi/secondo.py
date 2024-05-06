'''
Autore: Matteo Meringolo
Data: 06/05/2024
Titolo:Scrivere un programma per invertire una tupla
Esempio:
tpleIN=(‘a’,’c’,f’)
tpleOUT=(‘f’,‘a’,’c’)
'''

def controlloTupla(t1):
    if not t1:  # Controlla se la tupla è vuota
        return "Tupla vuota"
    else:
        return "Tupla normale: " + str(t1) + ", Tupla invertita: " + str(t1[::-1])

tupla = ('a', 'c', 'f') 

print(controlloTupla(tupla))




