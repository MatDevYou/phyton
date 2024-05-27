# Utilizzando la classe Cerchio vista a lezione ( cfr. 8.4.1 Python Primi Passi). Implementare un metodo che permetta di comprendere la posizione di un cerchio rispetto a un altro. In altre parole si vuole capire se un cerchio è secante, tangente o esterno ad un altro cerchio.


class Punto(object):
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def stampa(self):
        return str(self.X) + " " + str(self.Y)

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def setX(self, val):
        self.X = val

    def setY(self, val):
        self.Y = val

    def __str__(self):
        return "(" + str(self.X) + "," + str(self.Y) + ")"

    def getDistance(self, P):
        return ((self.X - P.X) ** 2 + (self.Y - P.Y) ** 2) ** 0.5

    def translatePoint(self, t):
        return Punto(self.X + t, self.Y + t)


class Cerchio(Punto):
    def __init__(self, centro, raggio):
        self.centro = centro
        self.raggio = raggio

    def getCentro(self):
        return self.centro

    def setCentro(self, punto):
        self.centro = punto

    def getRaggio(self):
        return self.raggio

    def setRaggio(self, val):
        self.raggio = val

    def __str__(self):
        return "C= " + str(self.centro) + " r= " + str(self.raggio)

    def getSuperficie(self):
        pigreco = 3.1415
        return pigreco * self.raggio**2

    def posizione(self, cerchio2):
        distanzaCentro = self.centro.getDistance(cerchio2.getCentro())
        sommaRaggi = self.raggio + cerchio2.getRaggio()
        differenzaRaggi = abs(self.raggio - cerchio2.getRaggio())

        if distanzaCentro > sommaRaggi:
            print("esterno")
        elif distanzaCentro == sommaRaggi:
            print("tangente esternamente")
        elif differenzaRaggi < distanzaCentro < sommaRaggi:
            print("secante")
        elif distanzaCentro == differenzaRaggi:
            print("tangente internamente")
        elif distanzaCentro < differenzaRaggi:
            print("interno")
        else:
            print("concentrici")


c1 = Cerchio(Punto(0, 0), 5)
c2 = Cerchio(Punto(10, 0), 3)
c3 = Cerchio(Punto(5, 0), 2)
c4 = Cerchio(Punto(7, 0), 3)

print(c1.posizione(c2))  # esterno
print(c1.posizione(c3))  # secante
print(c1.posizione(c4))  # tangente esternamente
