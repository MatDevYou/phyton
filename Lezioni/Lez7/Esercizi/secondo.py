'''
Autore: Matteo Meringolo
Data: 27/05/2024

Titolo:Creare una classe AritmeticaDue con attributi operando1 e operando2. Definire il
costruttore utilizzando parametri con valori predefiniti e il metodo str.
Aggiungere due metodi uno che restituisca la differenza e l’altro il prodotto dei due
operandi. Implementare un terzo metodo che permetta il confronto tra il risultato del
prodotto di due oggetti AritmeticaDue (in sostanza indicare se il prodotto è maggiore di
quello calcolato nell’oggetto AritmeticaDue passato come parametro).
Derivare dalla classe AritmeticaDue la classe AritmeticaTre aggiungendo l’attributo
operando3. Ridefinire il costruttore, il metodo str e i tre metodi differenza, prodotto e
confronto. Aggiungere un metodo per il calcolo della somma di tutti gli attributi.
Provare le classi e i metodi implementati.

'''

class AritmeticaDue:
    def __init__(self, operando1=0, operando2=0):
        """
        Costruttore della classe AritmeticaDue.
        Inizializza gli attributi operando1 e operando2 con valori predefiniti.
        """
        self.__operando1 = operando1
        self.__operando2 = operando2

    def getOperando1(self):
        """
        Restituisce il valore di operando1.
        """
        return self.__operando1
    
    def getOperando2(self):
        """
        Restituisce il valore di operando2.
        """
        return self.__operando2
    
    def setOperando1(self, val):
        """
        Imposta un nuovo valore per operando1.
        """
        self.__operando1 = val

    def setOperando2(self, val):
        """
        Imposta un nuovo valore per operando2.
        """
        self.__operando2 = val

    def __str__(self):
        """
        Restituisce una rappresentazione in stringa degli attributi.
        """
        return f"Operando1: {self.__operando1}, Operando2: {self.__operando2}"
    
    def differenza(self):
        """
        Restituisce la differenza tra operando1 e operando2.
        """
        return self.__operando1 - self.__operando2
    
    def prodotto(self):
        """
        Restituisce il prodotto tra operando1 e operando2.
        """
        return self.__operando1 * self.__operando2
    
    def confronto(self, altro):
        """
        Confronta il prodotto dell'oggetto corrente con quello di un altro oggetto AritmeticaDue.
        Restituisce True se il prodotto dell'oggetto corrente è maggiore, altrimenti False.
        """
        return self.prodotto() > altro.prodotto()

class AritmeticaTre(AritmeticaDue):
    def __init__(self, operando1=0, operando2=0, operando3=0):
        """
        Costruttore della classe AritmeticaTre.
        Inizializza gli attributi operando1, operando2 e operando3 con valori predefiniti.
        """
        super().__init__(operando1, operando2)
        self.__operando3 = operando3

    def getOperando3(self):
        """
        Restituisce il valore di operando3.
        """
        return self.__operando3

    def setOperando3(self, val):
        """
        Imposta un nuovo valore per operando3.
        """
        self.__operando3 = val

    def __str__(self):
        """
        Restituisce una rappresentazione in stringa degli attributi.
        """
        return f"\nOperando1: {self.getOperando1()}, Operando2: {self.getOperando2()}, Operando3: {self.__operando3}"
    
    def differenza(self):
        """
        Restituisce la differenza tra operando1, operando2 e operando3.
        """
        return self.getOperando1() - self.getOperando2() - self.__operando3

    def prodotto(self):
        """
        Restituisce il prodotto tra operando1, operando2 e operando3.
        """
        return self.getOperando1() * self.getOperando2() * self.__operando3

    def confronto(self, altro):
        """
        Confronta il prodotto dell'oggetto corrente con quello di un altro oggetto AritmeticaTre.
        Restituisce True se il prodotto dell'oggetto corrente è maggiore, altrimenti False.
        """
        return self.prodotto() > altro.prodotto()

    def somma(self):
        """
        Restituisce la somma di operando1, operando2 e operando3.
        """
        return self.getOperando1() + self.getOperando2() + self.__operando3

# Test delle classi
aritmeticaDue = AritmeticaDue(3, 2)
aritmeticaTre = AritmeticaTre(3, 2, 1)

# Prova dei metodi
print(aritmeticaDue)
print("Differenza:", aritmeticaDue.differenza())
print("Prodotto:", aritmeticaDue.prodotto())

print(aritmeticaTre)
print("Differenza:", aritmeticaTre.differenza())
print("Prodotto:", aritmeticaTre.prodotto())
print("Somma:", aritmeticaTre.somma())

# Confronto tra due oggetti AritmeticaDue
aritmeticaDue1 = AritmeticaDue(4, 2)
print("\nConfronto tra aritmeticaDue e aritmeticaDue1:", aritmeticaDue.confronto(aritmeticaDue1))

# Confronto tra due oggetti AritmeticaTre
aritmeticaTre1 = AritmeticaTre(4, 2, 1)
print("\nConfronto tra aritmeticaTre e aritmeticaTre1:", aritmeticaTre.confronto(aritmeticaTre1))
