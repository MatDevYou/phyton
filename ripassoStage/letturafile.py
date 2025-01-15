with open("/Applications/phyton/ripasso/testo.txt", "r") as file:
    for riga in file:
        print(riga.strip())
        
frase = input("Inserisci una frase: ")
with open("/Applications/phyton/ripasso/output.txt", "a") as file:
    file.write(frase + "\n")
    print("Frase scritta nel file output correttamente")