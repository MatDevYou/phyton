class Punto(object):
    """ Classe Punto di esempio
    - Appunti 'Python Primi Passi' - """
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
    def __str__(self): #sarebbe metodo to string
        return "("+str(self.X)+","+str(self.Y)+")"

p1 = Punto(2,3)
print(p1)