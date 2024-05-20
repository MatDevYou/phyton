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
    def __init__(self,base,altezza):
        self.__base = base
        self.__altezza = altezza
        
    def GetBase(self):
        return self.__base
    
    def GetAltezza(self):
        return self.__altezza
    
    def SetAltezza(self,val):
        self.__altezza = val
    
    def SetBase(self,val):
        self.__base = val
    
    def Area(self):
        return self.__base * self.__altezza
    
    def Perimetro(self):
        return (self.__base + self.__altezza) * 2
    
    def Contiene(self, NuovoRettangolo):
        return self.__base > NuovoRettangolo.GetBase() and self.__altezza > NuovoRettangolo.GetAltezza()
    
    def __str__(self):
        return f"\nBase: {self.__base}\nAltezza: {self.__altezza}\nPerimtro: {self.Perimetro()}\nArea: {self.Area()}"

rettangolo = Rettangolo(10,5)
rettangolo1 = Rettangolo(8,3)

print(rettangolo)
print(rettangolo1)


contiene = rettangolo.Contiene(rettangolo1)


print("\nSe true lo contiene se false non lo contiene: ",contiene)

