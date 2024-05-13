diz ={'k1':'v1', 'k2':'v2','k3':'v3'}
print(diz['k2'])
for chiave in diz:
    print(chiave,":",diz[chiave])
print("-------")

for chiave, valore in diz.items():
    print(chiave,":",valore)