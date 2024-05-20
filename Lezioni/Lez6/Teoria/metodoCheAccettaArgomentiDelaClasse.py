class Punto(object):
    """ Classe Punto di esempio
    - Appunti 'Python Primi Passi' - """
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
    def getDistance(self, P):
        return ((self.X - P.X)**2 + (self.Y - P.Y)**2)**0.5
    
p1 = Punto(0,0)
p2 = Punto(0,3)
print(p1.getDistance(p2)) #p1 quanto dista da p2
print(p2.getDistance(p1))