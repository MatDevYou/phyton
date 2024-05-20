class Punto(object):
    """ Classe Punto di esempio
    - Appunti 'Python Primi Passi' - """
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
    def stampa(self):
        return str(self.X)+" "+str(self.Y)
    
p1 = Punto(2,3)
print(p1.__dict__)
p1.altroAttributo=1
print(p1.__dict__)
del(p1.Y)
print(p1.__dict__)
p2=Punto(4,2)
print(p2.__dict__)