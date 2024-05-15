'''

Autore: Matteo Meringolo
Data: 13/05/2024
Titolo:Scrivete un programma Python per creare un dizionario da una stringa. Le lettere della
stringa rappresentano le chiavi, i valori rappresentano le occorrenze della chiave nella
stringa
Esempio
stringa = “ciao mamma”'
Dizionario: {'c': 1, 'i': 1, 'a': 3, ‘o’: 1, ‘ ‘:1,'m': 3}

'''

# Inizializzo la stringa di esempio
str = "ciao mamma"

# Creo un dizionario vuoto per memorizzare le occorrenze delle lettere
diz = {}

# Itero attraverso ogni carattere nella stringa
for carattere in str:
    # Se il carattere è già una chiave nel dizionario, incrementa il suo valore di 1
    if carattere in diz:
        diz[carattere] += 1
    # Se il carattere non è ancora una chiave nel dizionario, aggiungilo con valore 1
    else:
        diz[carattere] = 1

# Stampo il dizionario risultante
print(diz)


