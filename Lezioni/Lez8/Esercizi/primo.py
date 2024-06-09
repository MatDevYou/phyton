'''
Autore: Matteo Meringolo
Data: 04/06/2024

Titolo:Scrivere un programma che, leggendo da tastiera una stringa, la salvi su file “stringa.txt”.
Successivamente aprire il file “stringa.txt” e verificare il salvataggio.
    
'''

def salvaStringa():
    # Leggere la stringa da tastiera
    stringa = input("Inserisci una stringa: ")
    
    # Salvare la stringa nel file "stringa.txt"
    file = open("Lezioni/Lez8/Esercizi/stringa.txt","w")
    file.write(stringa)
    file.close()
    
    print("Stringa salvata su 'stringa.txt'.")

def verificaSalvataggio():
    # Leggere il contenuto del file "stringa.txt"
    try:
        file = open("stringa.txt", "r")
        contenuto = file.read()
        file.close()
        print("Contenuto del file 'stringa.txt':")
        print(contenuto)
    except FileNotFoundError:
        print("Errore: Il file 'stringa.txt' non esiste.")

# Chiamare direttamente le funzioni
salvaStringa()
verificaSalvataggio()




