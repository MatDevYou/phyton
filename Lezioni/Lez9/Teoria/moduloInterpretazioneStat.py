import stat

stat.S_ISDIR( mode )
#Restituisce un valore diverso da zero se la modalità proviene da una directory.

stat.S_ISREG( mode )
#Restituisce un valore diverso da zero se la modalità proviene da un file normale.

stat.S_ISLNK( mode )
#Restituisce un valore diverso da zero se la modalità proviene da un collegamento
simbolico.

stat.S_ISSOCK( mode )
#Restituisce un valore diverso da zero se la modalità proviene da un socket.

stat.S_IMODE( mode )