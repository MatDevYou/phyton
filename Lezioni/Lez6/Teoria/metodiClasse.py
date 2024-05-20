class Punto(object):
    """ Classe Punto di esempio
    - Appunti 'Python Primi Passi' - """
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
    def stampa(self):
        return str(self.X)+" "+str(self.Y)
    def getX(self):
        return self.X
    def getY(self):
        return self.Y
    def setX(self,val):
        self.X = val
    def setY(self,val):
        self.Y = val

p1 = Punto(2,3)
print(p1.X, p1.Y)
print(p1.getX(),p1.getY())
p1.setX(4)
p1.setY(1)
print(p1.X, p1.Y)