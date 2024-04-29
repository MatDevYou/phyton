'''
Autore: Matteo Meringolo
Data: 20/04/2024
Titolo: Scrivere un programma che dica se una stringa è palindroma.
Esempio:
str="ABBA" PALINDROMA
str="PIPPO" NON PALINDROMA

'''

def palindroma(stringa):
    
    if stringa == stringa[::-1]:
        print("palindroma")
    else:
        print("non palindroma")

str = "ABBA"

palindroma(str)