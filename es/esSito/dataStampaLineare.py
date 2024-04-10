giorno = 0
mese = 0
anno = 0

print("inserisci giorno, mese, anno")
giorno = int(input("giorno: "))
mese = int(input("mese: "))
anno = int(input("anno: "))



def switch(mese):
    if mese == 1:
        return "gennaio"
    elif mese == 2:
        return "febbraio"
    elif mese == 3:
        return "marzo"
    elif mese == 4:
        return "aprile"
    elif mese == 5:
        return "maggio"
    elif mese == 6:
        return "giugno"
    elif mese == 7:
        return "luglio"
    elif mese == 8:
        return "agosto"
    elif mese == 9:
        return "settempre"
    elif mese == 10:
        return "ottobre"
    elif mese == 11:
        return "novembre"
    elif mese == 12:
        return "dicembre"

risultato = switch(mese)
print(giorno,risultato, anno)