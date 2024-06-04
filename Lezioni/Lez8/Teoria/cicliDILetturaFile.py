fh = open("file.txt")
eof = False
while(not eof):
    riga = fh.readline()
    if riga:
        print(riga,end='')
    else:
        eof = True
fh.close()
