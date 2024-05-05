'''
Autore: Matteo Meringolo
Data: 20/04/2024
Titolo: Scrivere un programma che dica se una stringa è palindroma.
Esempio:
str="ABBA" PALINDROMA
str="PIPPO" NON PALINDROMA

'''

def palindroma(stringa):
    '''
    Funzione Palindroma

    stringa -> li passo la stringa da controllare nelal funzione
    '''

    #il [::-1] mi capovolge la stringa e in questo modo posso verificare se e' palindoma
    if stringa == stringa[::-1]:
        print("palindroma")
    else:
        print("non palindroma")

#dichiaro stinga da verificare
str = "ABBA"


#output
palindroma(str)