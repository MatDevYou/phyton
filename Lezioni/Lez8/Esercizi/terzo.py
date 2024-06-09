'''
Autore: Matteo Meringolo
Data: 04/06/2024

Titolo:Progetta una classe che legga un file di testo. Tale classe deve avere un metodo che
restituisca la parola con frequenza maggiore. [Suggerimento: si consideri l’esercizio che
contava le frequenze delle lettere in una stringa utilizzando i dictionary]
Provare il programma con testi classici come la Divina Commedia di Dante Alighieri
reperibile sul sito del progetto Gutenberg.
    
''' 

class Classe:
    def __init__(self, nomefile):
        self.nomefile = nomefile

    def scriviFile(self, contenuto):
        file = open(self.nomefile, 'w')
        file.write(contenuto)
        file.close()

    def leggiFile(self):
        file = open(self.nomefile, 'r')
        contenuto = file.read()
        file.close()
        return contenuto

    def trovaParoleLunghe(self, n=1):
        contenuto = self.leggiFile()
        parole = contenuto.split()
        paroleOrdinate = sorted(parole, key=len, reverse=True)
        return paroleOrdinate[:n]