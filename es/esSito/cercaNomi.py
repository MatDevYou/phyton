lista = ['Matteo', 'Gaia', 'Giacomo','Mattia','Mario','Giorgio','Lorenzo']

el = input("cerca un nome: ")
trovato = False

for nome in lista:
    if nome == el:
        trovato = True
        break
if trovato:
    print(f"{el} e' presente nella lista all'indice {lista.index(el)}")
else:
    print(f"{el} non e' nella lista")