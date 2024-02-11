giorno = int(input("inserisci giorno: "))
mese = int(input("inserisci mese: "))
anno = int(input("inserisci anno: "))

if giorno > 31 or mese > 12 or mese < 1 or giorno < 1:
    print("Data Errata!")
elif mese == 2 and (anno % 4 == 0 and giorno <= 29) or (anno % 400 == 0 ) or (mese == 4 or mese == 6 or mese == 9 or mese == 11) and giorno <= 30 or (mese == 1 or mese == 3 or mese == 5 or mese == 7 or mese == 8 or mese == 10 or mese == 12 and giorno <= 31):
    print(giorno, "/", mese,"/", anno)
else:
    print("Data Errata!")
