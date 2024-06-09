'''
Autore: Matteo Meringolo
Data: 04/06/2024

Titolo:Scrivere un programma che permetta di copiare il contenuto di un file in un altro file.
    
'''

class File:
    def __init__(self, nomefile):
        self.nomefile = nomefile

    def leggiFile(self):
        file = open(self.nomefile, 'r')
        contenuto = file.read()
        file.close()
        return contenuto

    def scriviFile(self, contenuto):
        file = open(self.nomefile, 'w')
        file.write(contenuto)
        file.close()

def copiaFile(nomefileSorgente, nomefileDestinazione):
    fileSorgente = File(nomefileSorgente)
    contenuto = fileSorgente.leggiFile()
    fileDestinazione = File(nomefileDestinazione)
    fileDestinazione.scriviFile(contenuto)
    print(f"Contenuto copiato da '{nomefileSorgente}' a '{nomefileDestinazione}'.")

# Esempio di utilizzo
copiaFile('Lezioni/Lez8/Esercizi/stringa.txt', 'Lezioni/Lez8/Esercizi/output.txt')
