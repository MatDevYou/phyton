lista = [5, 3, 8, 9, 7]
risultatoSomma = 0
risultatoMolt = 1

for numero in lista:
    risultatoSomma += numero
    risultatoMolt *= numero
print("La somma totale di quest'array e': " + str(risultatoSomma))
print("La moltiplicazione totale di quest'array e': " + str(risultatoMolt))

