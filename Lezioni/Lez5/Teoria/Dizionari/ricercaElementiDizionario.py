diz ={'k1':'v1', 'k2':'v2','k3':'v3'}
print('k1' in diz)
print('k7' in diz)
print('v1' in diz) #accetta le chiavi non i valori per quello da false
print('v7' in diz)
print('k1' and 'k2' in diz)
print(diz.get('k1'))#restituisce valore chiave k1 ma non la toglie
print(diz.get('k7'))
print(diz.get('k7',0))