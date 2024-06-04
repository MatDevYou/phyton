fh = open("file.txt")
righe = fh.read() #legge tutte le righe del file
print(righe)
fh.close()


#######################################################################
fh = open("file.txt")                                                 #
righe = fh.readlines() #mi lege tutto file e mi restituisce una lista #
print(righe)                                                          #
fh.close()                                                            #
#######################################################################

fh = open("file.txt")
righe = fh.readlines(14) #si blocca alla riga che arriva il 14 carattere
print(righe)
fh.close()