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
    def __init__(self):
        pass
    
    def Factorial(self, n):
        """
        Calcola il fattoriale di un numero intero n.
        """
        if n == 0:
            return 1
        risultato = 1
        for i in range(1, n + 1):
            risultato *= i
        return risultato
    
    def Sum(self, n):
        """
        Calcola la somma dei primi n numeri interi.
        """
        if n < 0:
            return 0  # gestire il caso di numeri negativi
        return n * (n + 1) // 2
    
    def tableMult(self, n, massimo =10):
        """
        Stampa la tabellina del numero n fino a limit.
        """
        print(f"Tabellina del {n}:")
        for i in range( massimo + 1):
            print(f"{n} x {i} = {n * i}")
        print()  # Aggiungo una riga vuota per separare le tabelline
    
    def allTablesMult(self, n, massimo=10):
        """
        Stampa le tabelline dei numeri da 1 a n fino a limit.
        """
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
