'''
Permette di ottenere lo stato di un file o un descrittore di file.
Esegue l'equivalente di una chiamata alla funzione di sistema stat() sul percorso
specificato. Il percorso può essere specificato come stringa o come descrittore di file
aperto.
'''

import os
file = "/home/massimo/dir1/file1"
statinfo = os.stat(file)
print(statinfo)
print(type(statinfo))
print(dir(statinfo))
print(statinfo.st_size)