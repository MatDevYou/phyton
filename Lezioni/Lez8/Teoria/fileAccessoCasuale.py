fh = open("filets.txt","w+")
print("scrivo: \t",fh.write("abcde\n")," bytes")
print("pos: \t\t",fh.tell())
print("scrivo: \t",fh.write("fghi\n")," bytes")
print("pos: \t\t",fh.tell())
print("Nuova pos: \t",fh.seek(2))
print("scrivo: \t",fh.write("X")," bytes")
print("pos: \t\t",fh.tell())
print("leggo: \t\t",fh.readline(1))

