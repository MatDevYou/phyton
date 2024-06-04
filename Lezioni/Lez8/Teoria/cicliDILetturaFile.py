fh = open("file.txt")
eof = False
while(not eof):
    riga = fh.readline()
    if riga:
        print(riga,end='')
    else:
        eof = True
fh.close()

#########################
#altra notazione 

fh = open("file.txt")
riga = fh.readline()
while riga:
    print(riga,end='')
    riga = fh.readline()
fh.close()