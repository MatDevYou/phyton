class Studente(object):
    def __init__(self,nome,eta):
        self._nome = nome # attributo di istanza
        self._eta = eta # attributo di istanza
    def giorniEta(self):
        return self._eta * 365
    
studente1 = Studente("Carlo",20)
print(studente1.nome) #e aggiungo _ lo stampa ma noi non dobbiamo farlo