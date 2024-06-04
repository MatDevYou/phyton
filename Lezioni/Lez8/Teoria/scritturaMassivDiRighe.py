righe=list()
righe.append("Prima riga di prova\n")
righe.append("seconda riga \n")
righe.append("terza riga ")
righe.append("-----------\n")
righe.append("Ultima riga\n")
fh = open("fileout.txt","w")
print(fh.writelines(righe)) #ci scrive tutte le righe