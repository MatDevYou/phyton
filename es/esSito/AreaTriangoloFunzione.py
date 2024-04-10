import math

l1 = round(float(input("Inserisci lato 1: ")), 2)
l3 = round(float(input("Inserisci lato 2: ")), 2)
base = round(float(input("Inserisci base: ")), 2)

def areaTriangolo(b, h):
    area = b * altezzaCalcolata / 2
    return area

def semiPerimetro(l1, l2, l3):
    semi = (l1 + l2 + l3) / 2
    return semi

def areaTriangoloScaleno(b, h):
    area = b * altezzaScaleno / 2
    return area

def areaTriangoloIsoscele(b, h):
    area = b * altezzaIscoscele / 2
    return area

sp = semiPerimetro(l1, base, l3)
erone = math.sqrt(sp * (sp - l1) * (sp - base) * (sp - l3))

Cmin = base / 2
ipotenusa = l3
perimetro = l1 * base * l3
altezzaCalcolata = round(float(math.sqrt((ipotenusa*ipotenusa) - (Cmin*Cmin))), 2)
area = round(float(areaTriangolo(base, altezzaCalcolata)), 2)


if l1 == base == l3:
    print("TRIANGOLO EQUILATERO")
    print("Perimetro: ",perimetro)
    print("Altezza: ", (altezzaCalcolata))
    print("Area Triangolo equilatero: ", area)
elif l1 != base and base != l3 and l1 != l3:
    x = base - l1
    Cmin = x
    altezzaScaleno = round(float(math.sqrt((ipotenusa*ipotenusa) - (x*x))), 2)
    area = round(float(areaTriangoloScaleno(base, altezzaScaleno)), 2)
    print("TRIANGOLO SCALENO")
    print("Perimetro: ",perimetro)
    print("Altezza: ", (altezzaScaleno))
    print("Area Triangolo scaleno: ", area)
else:
    y = base / 2
    Cmin = y
    altezzaIscoscele = round(float(math.sqrt((ipotenusa*ipotenusa) - (y*y))), 2)
    area = round(float(areaTriangoloIsoscele(base, altezzaIscoscele)), 2)
    print("TRIANGOLO ISOSCELE")
    print("Altezza: ", (altezzaIscoscele))
    print("Area Triangolo isocele: ", area)

#ipotenusa = math.sqrt((l1*l1) + (Cmin*Cmin)) #solo in caso sia scaleno 

#print("Ipotenusa triangolo:", round(ipotenusa, 2))
#print("Altezza:", round(altezzaCalcolata, 2))



