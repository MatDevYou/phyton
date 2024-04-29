'''
Autore: Matteo Meringolo
Data: 20/04/2024
Titolo: Scrivere un programma che date due liste stampi "OK" se hanno almeno un membro
comune altrimenti stampa "KO".
Esempio:
● lista1=[1,5,8] lista2=[3,1,10] -> output: "OK"
● lista1=[1,5,8] lista2=[3,11,10] -> output: "KO"
'''

def controllaLista(lista1, lista2): 
    '''
    Definizione funzione : controllaLista

    paremetri:
    uso lista1 e lista2 come parametri per farli confrontare
    '''
    for elemento in lista1: #controllo manualmente se ogni elemento della prima lista è presente nella seconda lista
        if elemento in lista2:
            print("OK")
            return
    print("KO")

#inizializzazione liste
lista1 = [12, 5, 8]
lista2 = [3, 1, 10]

#output
controllaLista(lista1, lista2)
