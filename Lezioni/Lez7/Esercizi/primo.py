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

class Persona:
    def __init__(self, nome, eta, indirizzo):
        self.__nome = nome
        self.__eta = eta
        self.__indirizzo = indirizzo
        
    def getNome(self):
        return self.__nome  
    
    def getEta(self):
        return self.__eta
    
    def getIndirizzo(self):
        return self.__indirizzo
    
    def setNome(self, val):
        self.__nome = val
        
    def setEta(self, val):
        self.__eta = val
        
    def setIndirizzo(self, val):
        self.__indirizzo = val
      
    def __str__(self):
        return f"Nome: {self.__nome}, Età: {self.__eta}, Indirizzo: {self.__indirizzo}"
    
class Studente(Persona):
    def __init__(self, nome, eta, indirizzo, scuola, mediavoti):
        super().__init__(nome, eta, indirizzo)
        self.__scuola = scuola
        self.__mediavoti = mediavoti
        
    def getScuola(self):
        return self.__scuola 
    
    def getMediaVoti(self):
        return self.__mediavoti
    
    def setScuola(self, val):
        self.__scuola = val
        
    def setMediaVoti(self, val):
        self.__mediavoti = val
    
    def __str__(self):
        return f"{super().__str__()}, Scuola: {self.__scuola}, Media Voti: {self.__mediavoti}"
    
class Lavoratore(Persona):
    def __init__(self, nome, eta, indirizzo, azienda, stipendio):
        super().__init__(nome, eta, indirizzo)
        self.__azienda = azienda
        self.__stipendio = stipendio
        
    def getAzienda(self):
        return self.__azienda 
    
    def getStipendio(self):
        return self.__stipendio
    
    def setAzienda(self, val):
        self.__azienda = val
        
    def setStipendio(self, val):
        self.__stipendio = val
        
    def __str__(self):
        return f"{super().__str__()}, Azienda: {self.__azienda}, Stipendio: {self.__stipendio}"   

# Test delle classi
persona = Persona("Mario Rossi", 40, "Via Roma 10, Milano")
studente = Studente("Luca Bianchi", 20, "Via Milano 5, Roma", "Università di Roma", 28)
lavoratore = Lavoratore("Giulia Verdi", 35, "Corso Torino 20, Torino", "Azienda Tech", 3000)

# Prova dei metodi
print(persona)
print(studente)
print(lavoratore)

# Modifica degli attributi
persona.setNome("Mario Rossi Jr.")
persona.setEta(41)
persona.setIndirizzo("Via Roma 15, Milano")

studente.setScuola("Politecnico di Milano")
studente.setMediaVoti(30)

lavoratore.setAzienda("Azienda Software")
lavoratore.setStipendio(3500)

# Verifica delle modifiche
print("\nDopo le modifiche:")
print(persona)
print(studente)
print(lavoratore)
