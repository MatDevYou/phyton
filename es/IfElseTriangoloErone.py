import math

l1 = int(input("inserisci lato 1: "))
l2 = int(input("inserisci lato 2: "))
l3 = int(input("inserisci lato 3: "))

semi = (l1 + l2 + l3) / 2
area = math.sqrt(semi * (semi - l1) * (semi - l2) * (semi - l3))

if area > 0:
    if l1 == l2 == l3:
        print("triangolo equilatero")
    elif l1 != l2 and l2 != l3 and l1 != l3:
        print("triangolo scaleno")
    else:
        print("triangolo isoscele")
else:
    print("Impossibile formare un triangolo con i lati dati.")
