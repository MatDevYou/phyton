'''
Autore: Matteo Meringolo
Data: 27/05/2024

Titolo:Si definisca una classe Persona che abbia i seguenti attributi:
● nome
● indirizzo
● età
Tale classe contiene i seguenti metodi: il costruttore, l’overriding del metodo __str__ e tutti i
metodi getter e setter degli attributi.
Si vogliono derivare dalla classe Persona le seguenti classi:
● Studente
● Lavoratore
La prima deve avere gli attributi aggiuntivi:
● Scuola
● Media voti
La seconda deve avere gli attributi aggiuntivi:
● Azienda
● Stipendio
Aggiungere tutti i metodi getter e setter relativi agli attributi aggiuntivi.
Inoltre effettuare l’overriding dei costruttori e del metodo str inserendo gli attributi
aggiuntivi.
Provare le tre classi instanziando almeno un oggetto per classe e provando qualche
metodo.


'''

class Persona(object):
    # Metodo di inizializzazione della classe, chiamato quando si crea un'istanza della classe
    def __init__(self, nome, eta, indirizzo):
        # Inizializzazione degli attributi dell'oggetto
        self.__nome = nome  # Attributo pubblico per il nome
        self.__eta = eta  # Attributo pubblico per l'età
        self.__indirizzo = indirizzo  # Attributo privato per lo stipendio
        
    # Metodo per ottenere il valore dell'attributo 'nome'
    def getNome(self):
        return self.__nome  
    
    # Metodo per ottenere il valore dell'attributo 'eta'
    def getEta(self):
        return self.__eta
    
    # Metodo per ottenere il valore dell'attributo privato 'stipendio'
    def getIndirizzo(self):
        return self.__indirizzo
    
    # Metodo per impostare un nuovo valore per l'attributo 'nome'
    def setNome(self, val):
        self.__nome = val
        
    # Metodo per impostare un nuovo valore per l'attributo 'eta'
    def setEta(self, val):
        self.__eta = val
        
    # Metodo per impostare un nuovo valore per l'attributo privato 'stipendio'
    def setIndirizzo(self, val):
        self.__indirizzo = val
      
    # Metodo speciale che definisce la rappresentazione in stringa dell'oggetto
    def __str__(self):
        # Restituisce una stringa con gli attributi nome e età
        return f"\n\nNome: {self.nome}, \nEtà: {self.eta}, \nIndirizzo: {self.__indirizzo}"
    
class Studente(Persona):
    def __init__(self, nome, eta, indirizzo, scuola, mediavoti):
        super().__init__(nome, eta, indirizzo)  # Chiamata al costruttore della superclasse
        self.__scuola = scuola  # Attributo pubblico per la scuola
        self.__mediavoti = mediavoti  # Attributo pubblico per la media dei voti
        
    def getScuola(self):
        return self.__scuola 
    
    def getMediaVoti(self):
        return self.__mediavoti
    
    def setScuola(self,val):
        self.__scuola = val
        
    def setMediaVoti(self,val):
        self.__mediavoti = val
    
    # Metodo speciale che definisce la rappresentazione in stringa dell'oggetto
    def __str__(self):
        # Restituisce una stringa con gli attributi della superclasse e quelli della classe Studente
        return f"{super().__str__()}, Scuola: {self.scuola}, Media Voti: {self.mediavoti}"