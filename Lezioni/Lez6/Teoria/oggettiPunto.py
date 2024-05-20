class Punto(object):
    """ Classe Punto di esempio
    - Appunti 'Python Primi Passi' - """
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
    def stampa(self):
        return str(self.X)+" "+str(self.Y)

p1 = Punto(2,3)
print(p1.__doc__)
print(p1)
print(p1.X, p1.Y)
print(p1.stampa())
