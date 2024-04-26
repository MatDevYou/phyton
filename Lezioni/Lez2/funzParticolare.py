def media(*pippo):
    somma=0
    for val in pippo:
        somma+=val
    
    return somma/len(pippo)

print("Media 1 = ", media(1,2,3))
print("Media 2 = ", media(1,2,3,4,5,6))
print("Media 3 = ", media())

def media(a : int, b: int, c: int) -> float:
    somma=a + b + c
    
    return somma/3


print("Media 1 = ", media(1,2,3))
print("Media 2 = ", media(1,2,3,4,5,6))
print("Media 3 = ", media())
