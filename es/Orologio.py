secondi = int(input("inserisci i secondi: "))

ore = int(secondi / 3600)
y = secondi-ore * 3600
minuti = int(y / 60)
restoMinuti = y - minuti * 60

print(format(ore,"02"), ":",format(minuti,"02"),":",secondi)