class Cerchio(object):
    def __init__(self,centro,raggio):
        self.centro = centro
        self.raggio = raggio
    def getCentro(self):
        return self.centro
    def setCentro(self,punto):
        self.centro = punto
    def getRaggio(self):
        return self.raggio
    def setRaggio(self,val):
        self.raggio = val
    def __str__(self):
        return "C= "+str(self.centro)+" r= "+str(self.raggio)
    def getSuperficie(self):
        pigreco=3.1415
        return pigreco*self.raggio**2

class Punto(object):
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
    def __str__(self):
        return "("+str(self.X)+","+str(self.Y)+")"
    def getDistance(self, P):
        return ((self.X - P.X)**2 + (self.Y - P.Y)**2)**0.5
    def translatePoint(self, t):
        return Punto(self.X + t,self.Y + t)

class Cilindro(Cerchio):
    def __init__(self,centro,raggio,altezza):
        super().__init__(centro,raggio)
        self.altezza = altezza
        
    def getAltezza(self):
        return self.altezza
    
    def setAltezza(self,val):
        self.altezza = val
        
    def __str__(self):
        return "Cilindro: "+super().__str__()+" h= "+str(self.altezza)
  
    def getSuperficie(self):
        pigreco=3.1415
        return 2*pigreco*self.raggio*self.altezza + 2*super().getSuperficie()
    
    def getVolume(self):
        return super().getSuperficie()*self.altezza


c1=Cilindro(Punto(2,2),1,2)
print(c1)
print(c1.raggio)
print(c1.getCentro())
print(c1.getSuperficie())
print(c1.getVolume())
