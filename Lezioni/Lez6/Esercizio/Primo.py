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
        self.nome = nome  # Attributo pubblico per il nome
        self.eta = eta  # Attributo pubblico per l'età
        self.__stipendio = stipendio  # Attributo privato per lo stipendio
        
    # Metodo per ottenere il valore dell'attributo 'nome'
    def getNome(self):
        return self.nome  
    
    # Metodo per ottenere il valore dell'attributo 'eta'
    def getEta(self):
        return self.eta
    
    # Metodo per ottenere il valore dell'attributo privato 'stipendio'
    def getStipendio(self):
        return self.__stipendio
    
    # Metodo per impostare un nuovo valore per l'attributo 'nome'
    def setNome(self, val):
        self.nome = val
        
    # Metodo per impostare un nuovo valore per l'attributo 'eta'
    def setEta(self, val):
        self.eta = val
        
    # Metodo per impostare un nuovo valore per l'attributo privato 'stipendio'
    def setStipendio(self, val):
        self.__stipendio = val
      
    # Metodo speciale che definisce la rappresentazione in stringa dell'oggetto
    def __str__(self):
        # Restituisce una stringa con gli attributi nome e età
        return f"\n\nNome: {self.nome}, \nEtà: {self.eta}"

# Creazione di due istanze della classe Insegnante con nome, età e stipendio specificati
i = Insegnante("Dario", 15, 1500)
i2 = Insegnante("Patrizio", 20, 3000)

# Stampa delle istanze i e i2, che utilizza il metodo __str__
print(i, i2)

