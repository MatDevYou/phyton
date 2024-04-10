def calcolo (operazione , n , m):
    if operazione == "+":
        print("Risulatato della somma e: ", n + m)
    if operazione == "-":
        print("Risulatato della differenza e: ", n - m)
    if operazione == "*":
        print("Risulatato della moltiplicazione e: ", n * m)
    if operazione == "/":
        if m != 0:
            print("Risulatato della divisione e: ", n / m)
    else:
            print("operazione impossibile")
    if operazione == "%":
        if m != 0:
            print("Risulatato del resto e: ", n % m)
        else: 
            print("impossibile dividere")
        
print("Inserisci due numeri interi:")
n = int(input("n: "))
m = int(input("m: "))

print("Inserisci l'operazione da eseguire")
print("Digita uno dei seguenti simboli: +, -, *, /, %")
operazione = input("Scelta: ")

calcolo(operazione, n, m)