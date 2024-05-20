class Punto(object):
    """ Classe Punto di esempio
    - Appunti 'Python Primi Passi' - """
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
    def translatePoint(self, t):
        return Punto(self.X + t,self.Y + t)
    def __str__(self):
        return "("+str(self.X)+","+str(self.Y)+")"
    
p1 = Punto(2,3)
p2=p1.translatePoint(2)
print("Punto iniziale: ",p1)
print("Punto traslato: ",p2)
print(type(p2))