# Il programma legge tre numeri e dice se possono essere le lunghezze dei lati di un triangolo 
# (perché un triangolo possa essere tale la somma di ogni coppia lati deve essere maggiore dell’altro)

l1 = float(input("Inserisci lunghezza lato 1: "))
l2 = float(input("Inserisci lunghezza lato 2: "))
l3 = float(input("Inserisci lunghezza lato 3: "))

if l1 + l2 > l3:
    if l1 + l3 > l2:
        if l2 + l3 > l1:
            print("la lunghezza potrebbe essere un lato del triangolo")
        else:
            print("la lunghezza potrebbe essere un lato del triangolo")
    else:
        print("la lunghezza potrebbe essere un lato del triangolo")
else: 
    print("la lunghezza potrebbe essere un lato del triangolo")
    
    