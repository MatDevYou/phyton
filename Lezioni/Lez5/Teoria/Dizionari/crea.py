#I dizionari sono una struttura informativa non sequenziale, cioè non è possibile stabilire un‘
#ordine tra gli oggetti che memorizza al suo interno 
diz1 = {}
print(diz1)
diz2 = {'pippo':'0113456732', 2: 'numero',
False: 'paperino',5:2 }
print(diz2)
diz3 = {'pippo':'0113456732', 'pippo': 'numero'}#stampa ultimo, lo tratta com eaggiornamento
print(diz3)

print(len(diz1))
print(len(diz2))
print(len(diz3))