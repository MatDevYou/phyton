'''
Autore: Matteo Meringolo
Data: 15/04/2024
Titolo:Si hanno in input due numeri reali A e B e una successione di numeri reali positivi che
termina con il valore 0. Si vuole in output la media dei soli numeri compresi tra A e B.
'''
#dichiarazione delle variabili
A = float(input("Inserisci il numero reale a: "))
B = float(input("Inserisci il numero reale b: "))
media = (A + B) / 2


#controllo se A e B sono numeri reali e se fossero reali allora stampa la media
if A > 0 and B > 0 and A > 0 and A < B:
    print("media: ", media)
else:
    print("impossibile")
    