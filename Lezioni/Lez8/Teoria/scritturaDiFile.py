righe=list()
righe.append("Prima riga di prova\n")
righe.append("seconda riga \n")
righe.append("terza riga ")
righe.append("-----------\n")
righe.append("Ultima riga\n")

fh = open("Lezioni/Lez8/Teoria/fileout.txt","w")

for riga in righe:
    fh.write(riga)

    
#'r' aperto per la lettura (predefinito)
#'w' aprire per la scrittura, troncando prima il file
#'x' aperto per la creazione esclusiva, errore se il file esiste già
#'a' aprire per la scrittura, aggiungendo alla fine del file se esiste
#'b' modalità binaria
#'t' modalità testo (predefinita)
#'+' aperto per l'aggiornamento (lettura e scrittura