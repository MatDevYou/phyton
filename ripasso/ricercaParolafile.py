parola = input("Inserisci una parola: ")
conteggio = 0

with open("/Applications/phyton/ripasso/testo.txt", "r") as file:
    for riga in file:
        parole = riga.strip().split()
        conteggio += parole.count(parola)

print(f"La parola '{parola}' è presente {conteggio} volte nel file.")