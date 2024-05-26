'''
Autore: Matteo Meringolo
Data: 20/05/2024

Titolo:1 - Creare una classe Calcolo con un costruttore di default (senza parametri) che consenta
di eseguire vari calcoli su numeri interi.
2 - Creare un metodo chiamato Factorial() che permetta di calcolare il fattoriale di un intero.
Testare il metodo istanziando la classe.
3 - Creare un metodo chiamato Sum() che consenta di calcolare la somma dei primi n interi
1 + 2 + 3 + .. + n. Prova questo metodo.
5 - Creare un metodo tableMult() che crea e visualizza la tabellina di un dato intero. Quindi
creare un metodo allTablesMult() per visualizzare tutte le tabelline di numeri interi 1, 2, 3, ...,
'''


class Calcolo(object):
    # Metodo di inizializzazione della classe Calcolo.
    # In questo caso, non vengono inizializzati attributi, quindi il metodo è vuoto.
    def __init__(self):
        pass
    
    # Metodo per calcolare il fattoriale di un numero intero n.
    def Factorial(self, n):
        """
        Calcola il fattoriale di un numero intero n.
        """
        if n == 0:
            return 1  # Il fattoriale di 0 è 1
        risultato = 1
        # Calcolo del fattoriale mediante un ciclo for
        for i in range(1, n + 1):
            risultato *= i
        return risultato
    
    # Metodo per calcolare la somma dei primi n numeri interi.
    def Sum(self, n):
        """
        Calcola la somma dei primi n numeri interi.
        """
        if n < 0:
            return 0  # Gestire il caso di numeri negativi
        # Calcolo della somma utilizzando la formula della somma aritmetica
        return n * (n + 1) // 2
    
    # Metodo per stampare la tabellina del numero n fino a un valore massimo (default = 10).
    def tableMult(self, n, massimo=10):
        """
        Stampa la tabellina del numero n fino a massimo.
        """
        print(f"Tabellina del {n}:")
        # Stampa della tabellina utilizzando un ciclo for
        for i in range(massimo + 1):
            print(f"{n} x {i} = {n * i}")
        print()  # Aggiunge una riga vuota per separare le tabelline
    
    # Metodo per stampare le tabelline dei numeri da 1 a n fino a un valore massimo (default = 10).
    def allTablesMult(self, n, massimo=10):
        """
        Stampa le tabelline dei numeri da 1 a n fino a massimo.
        """
        # Stampa delle tabelline utilizzando un ciclo for
        for i in range(n + 1):
            self.tableMult(i, massimo)

# Test dei metodi della classe Calcolo
calcolo = Calcolo()

# Test del metodo Factorial
fattoriale = 5
print(f"Il fattoriale di {fattoriale} è: {calcolo.Factorial(fattoriale)}")

# Test del metodo Sum
numero = 5
print(f"La somma dei primi {numero} numeri interi è: {calcolo.Sum(numero)}")

# Test del metodo tableMult
numero = 5
calcolo.tableMult(numero)

# Test del metodo allTablesMult
numero = 5
calcolo.allTablesMult(numero)

