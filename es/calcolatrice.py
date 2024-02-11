print("Inserisci i numeri interi: ")

n = int(input("n: "))
m = int(input("m: "))

print("Inserisci l'operazione da eseguire")
print("Digita uno dei seguenti simboli: +, -, *, /, %")
operazione = input("Scelta: ")

def switch(operazione, n, m):
    if operazione == "+":
        return n + m
    elif operazione == "-":
        return n - m
    elif operazione == "*":
        return n * m
    elif operazione == "/":
        if m != 0:
            return n / m
        else:
            return "Impossibile dividere per zero"
    elif operazione == "%":
        if m != 0:
            return n % m
        else:
            return "Impossibile dividere per zero"
    else:
        return "Operazione non valida"

risultato = switch(operazione, n, m)
print("Risultato:", risultato)

