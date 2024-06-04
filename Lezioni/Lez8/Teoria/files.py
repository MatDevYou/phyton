fh = open("file.txt","r")

print(fh)

riga=fh.readline()
riga=fh.readline(10) #leggiamo 10 caratteri

while(riga!=''):
    print(riga,end='')
    riga=fh.readline()