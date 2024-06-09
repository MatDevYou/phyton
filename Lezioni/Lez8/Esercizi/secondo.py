'''
Autore: Matteo Meringolo
Data: 04/06/2024

Titolo:Scrivi una classe che legga un file di testo e stampi sul file: “output.txt” la parola più lunga
contenuta. [Facoltativo: stampi sul file: “output.txt” le prime N parole più lunghe, N è dato in
input dall’utente).
Istanziare la classe e provare i metodi implementati.
    
'''


class File:
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

def salvaStringa():
    stringa = input("Inserisci una stringa: ")
    file = File('stringa.txt')
    file.scriviFile(stringa)
    print("Stringa salvata su 'stringa.txt'.")

def verificaParolaPiuLunga():
    file = File('stringa.txt')
    parolaPiuLunga = file.trovaParoleLunghe(1)[0]
    outputFile = File('output.txt')
    outputFile.scriviFile(parolaPiuLunga)
    print("La parola più lunga è stata salvata su 'output.txt'.")

def verificaNParolePiuLunghe():
    n = int(input("Inserisci il numero di parole più lunghe da trovare: "))
    file = File('stringa.txt')
    paroleLunghe = file.trovaParoleLunghe(n)
    outputFile = File('output.txt')
    outputFile.scriviFile('\n'.join(paroleLunghe))
    print(f"Le prime {n} parole più lunghe sono state salvate su 'output.txt'.")

# Eseguire le funzioni
salvaStringa()
verificaParolaPiuLunga()
verificaNParolePiuLunghe()

