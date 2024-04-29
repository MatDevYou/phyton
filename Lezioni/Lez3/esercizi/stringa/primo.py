'''
Autore: Matteo Meringolo
Data: 20/04/2024
Titolo: Scrivere un programma per rimuovere l'n- esimo carattere da una stringa non vuota.
Progettare una funzione che accetti la stringa, la posizione del carattere e restituisca la
stringa modificata.
'''

def rimuoviCarattere(stringa, n):
    # Verifica se l'indice n è valido
    if n < 0 or n >= len(stringa):
        return "Errore: Indice non valido"
    
    # Utilizza lo slicing per creare una nuova stringa senza il carattere in posizione n
    nuova_stringa = stringa[:n] + stringa[n+1:]
    
    return nuova_stringa

# Esempio di utilizzo della funzione
str = "ciao"
n = 2  # Rimuovere il terzo carattere ('a')
stringaMod = rimuoviCarattere(str, n)
print(str)  


