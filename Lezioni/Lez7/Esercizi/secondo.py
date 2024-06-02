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

class AritmeticaDue(object):
    def __init__(self,operando1,operando2):
        self.__operando1=operando1
        self.__operando2=operando2

    def getOperando1(self):
        return self.__operando1
    
    def getOperando2(self):
        return self.__operando2
    
    def setOperando1(self,val):
        self.__operando1=val

    def setOperando2(self, val):
        self.__operando2=val

    def __str__(self):
        return f"Operando1:{self.__operando1} Operando2:{self.operando2}"
    
    def differenza(self):
        return self.__operando1-self.__operando2
    
    def prodotto(self):
        return self.__operando1*self.__operando2
    
    def confronto(self,a):
        if self.prodotto()>a.prodotto():
            return True
        else:
            return False

class AritmeticaTre(AritmeticaDue):
    def __init__(self, operando1, operando2, operando3):
        super().__init__(operando1, operando2)
        self.__operando3=operando3

    def getOperando3(self):
        return self.__operando3

    def setOperando3(self, val):
        self.__operando3=val

    def __str__(self):
        return f"Operando1:{self.__operando1} Operando2:{self.__operando2} Operando3:{self.__operando3}"
    
    def differenza(self):
        return self.__operando1-self.__operando2-self.__operando3

    def somma(self):
        return self.__operando1+self.__operando2+self.__operando3

    def somma(self):
        return self.__operando1+self.__operando2+self.__operando3
    

aritmeticaDue = AritmeticaDue(3,2)
print(aritmeticaDue)