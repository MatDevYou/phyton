fh = open("file.txt")
for riga in fh:
    print(riga, end='')
fh.close()