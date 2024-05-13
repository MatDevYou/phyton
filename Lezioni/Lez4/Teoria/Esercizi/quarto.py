'''
Autore: Matteo Meringolo
Data: 06/05/2024
Titolo:Scrivere un programma per contare gli elementi in una lista finché non si incontra un
elemento di tipo tupla. [Suggerimento: si usi la funzione isinstance( )]
'''

def contaElementi(lista):
    '''
    Funzione : contaElementi

<<<<<<< HEAD
    parametri
    lista -> passo l 
    
    '''
    count = 0
    tuplaTrovata = False

    for elem in lista:
        if isinstance(elem, tuple):
            tupla_trovata = True
            break
        count += 1
    else:
        if not tuplaTrovata:
            print("Numero di elementi nella lista senza incontrare la tupla:", count)

    if tuplaTrovata:
        print("Numero di elementi prima della tupla:", count)

    return count, len(lista)

# Esempio di utilizzo
lista = [2, 5, 9, 7, 4, 1]
count_prima_tupla, count_totale = contaElementi(lista)
print("Numero totale di elementi nella lista:", contaElementi(lista))
=======

print(lista.len)
>>>>>>> 4603e118532b36d87f72411fef3adb4506fca1fd
