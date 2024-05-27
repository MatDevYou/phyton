'''
Autore: Matteo Meringolo
Data: 20/05/2024

Titolo:Creare una classe Rettangolo con attributi base e altezza. Costruire tutti i metodi setter e
getter per gli attributi. Aggiungere i metodi per il calcolo dell’area e del perimetro.

Implementare un metodo di nome: “contiene” che ha come parametro un oggetto
rettangolo. Tale metodo deve restituire true se il rettangolo oggetto chiamante contiene il
rettangolo oggetto parametro, false se non lo contiene. 

Un rettangolo “contiene” un altro
quando la sua altezza e la sua base sono maggiori rispettivamente della base e dell’altezza
del secondo rettangolo.
'''


class Rettangolo(object):
    # Metodo di inizializzazione della classe Rettangolo.
    # Inizializza le proprietà 'base' e 'altezza' con i valori forniti.
    def __init__(self, base, altezza):
        self.__base = base
        self.__altezza = altezza
        
    # Restituisce il valore della base del rettangolo.
    def GetBase(self):
        return self.__base
    
    # Restituisce il valore dell'altezza del rettangolo.
    def GetAltezza(self):
        return self.__altezza
    
    # Imposta un nuovo valore per l'altezza del rettangolo.
    def SetAltezza(self, val):
        self.__altezza = val
    
    # Imposta un nuovo valore per la base del rettangolo.
    def SetBase(self, val):
        self.__base = val
    
    # Calcola e restituisce l'area del rettangolo.
    def Area(self):
        return self.__base * self.__altezza
    
    # Calcola e restituisce il perimetro del rettangolo.
    def Perimetro(self):
        return (self.__base + self.__altezza) * 2
    
    # Verifica se il rettangolo corrente contiene un altro rettangolo.
    # Restituisce True se il rettangolo corrente ha sia una base che un'altezza
    # maggiori di quelle del nuovo rettangolo fornito, altrimenti False.
    def Contiene(self, NuovoRettangolo):
        return self.__base > NuovoRettangolo.GetBase() and self.__altezza > NuovoRettangolo.GetAltezza()
    
    # Restituisce una rappresentazione in stringa del rettangolo.
    def __str__(self):
        return f"\nBase: {self.__base}\nAltezza: {self.__altezza}\nPerimetro: {self.Perimetro()}\nArea: {self.Area()}"

# Creazione di due oggetti Rettangolo con valori di base e altezza specificati.
rettangolo = Rettangolo(10, 5)
rettangolo1 = Rettangolo(8, 3)

# Stampa delle informazioni sui rettangoli.
print(rettangolo)
print(rettangolo1)

# Verifica se il primo rettangolo contiene il secondo rettangolo.
contiene = rettangolo.Contiene(rettangolo1)

# Stampa il risultato della verifica di contenimento.
print("\nSe true lo contiene se false non lo contiene: ", contiene)

  
