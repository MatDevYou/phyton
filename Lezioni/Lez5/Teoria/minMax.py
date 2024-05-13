lista = [1, 2, 3, 4]
tupla = (1, 2, 3, 4)
stringa = "abcd"
str2 = "xyz"
str3 = "lm"
vuota = []
print(min(lista),max(lista))
print(min(tupla),max(tupla))
print(min(stringa),max(stringa))
print(min(stringa,str2,str3),max(stringa,str2,str3))
print(min(stringa,str2,str3,key=len),max(stringa,str2,str3,key=len))
print(max(vuota,default=1))
print(max(vuota))
