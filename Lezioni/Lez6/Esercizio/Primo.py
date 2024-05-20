###
'''
Autore: Matteo Meringolo
Data: 20/05/2024

Titolo:Creare una classe Insegnante con attributi nome, età e stipendio, dove stipendio deve
essere un attributo privato.
Costruire tutti i metodi getter e setter per gli attributi (anche per quelli pubblici)
Effettuare loverriding del metodo __str__ in maniera tale che restituisca gli attributi nome e
età.
Provare la classe istanziando almeno due oggetti.
'''


# Definizione della classe Insegnante
class Insegnante(object):
    # Metodo di inizializzazione della classe, chiamato quando si crea un'istanza della classe
    def __init__(self, nome, eta, stipendio):
        # Inizializzazione degli attributi dell'oggetto
        self.nome = nome  
        self.eta = eta  
        self.__stipendio = stipendio
        
    def getNome(self):
        return self.nome  
    
    def getEta(self):
        return self.eta
    
    def getStipendio(self):
        return self.__stipendio
    
    def setNome(self,val):
        self.nome = val
        
    def setEta(self,val):
        self.eta = val
        
    def setStipendio(self,val):
        self.__stipendio = val
      
    # Metodo speciale che definisce la rappresentazione in stringa dell'oggetto
    def __str__(self):
    # Restituisce una stringa con gli attributi nome e età
        return f"\n\nNome: {self.nome}, \nEtà: {self.eta}"

# Creazione di un'istanza della classe Insegnante
i = Insegnante("Dario", 15, 1500)
i2 = Insegnante("Patrizio", 20, 3000)

# Stampa dell'oggetto i, che utilizza il metodo __str__
print(i,i2)
