'''
    Autore: Matteo Meringolo
    Data: 04/06/2024

    Titolo:
    
'''

def salva_stringa():
    # Leggere la stringa da tastiera
    stringa = input("Inserisci una stringa: ")
    
    # Salvare la stringa nel file "stringa.txt"
    file = open("stringa.txt", "w")
    file.write(stringa)
    file.close()
    
    print("Stringa salvata su 'stringa.txt'.")

def verifica_salvataggio():
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
salva_stringa()
verifica_salvataggio()




