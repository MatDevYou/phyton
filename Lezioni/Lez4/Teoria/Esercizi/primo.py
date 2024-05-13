'''
Autore: Matteo Meringolo
Data: 06/05/2024
Titolo: Scrivere un programma per rimuovere 
l'n- esimo carattere da una tupla non vuota.

''' 

#dichiarazione della tupla e dell'input 
tupla = ("pane", 12, 4, 9)
n = int(input("Quale posizione della tupla vuoi eliminare? "))

# Verifica se l'indice n è valido
if 0 <= n < len(tupla):
    # Creazione di una nuova tupla che contiene tutti gli elementi tranne quello in posizione n
    nuovaTupla = tupla[:n] + tupla[n+1:]
    print("Tupla originale:", tupla)
    print("Nuova tupla senza l'elemento in posizione", n, ":", nuovaTupla)
else:
    print("Indice non valido. La tupla non è stata modificata.")
