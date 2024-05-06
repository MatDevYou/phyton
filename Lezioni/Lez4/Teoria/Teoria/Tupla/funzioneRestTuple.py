def rettangolo(base, altezza):
    return base*altezza, 2*base+2*altezza

a=2
b=3
print(rettangolo(a,b))
area,perimetro = rettangolo(4,6)
print("area= ",area," perimetro= ",perimetro)
