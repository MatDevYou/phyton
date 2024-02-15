def geometra():
    print("""
    BENVENUTO ALLA FUNZIONE GEOMETRA!
    In fase di selezione, a ciascun possibile calcolo corrisponde un valore numerico:
    - Area Quadrato: 1
    - Area Rettangolo: 2
    - Area Triangolo: 3
    - Area Cerchio: 4
    """)

geometra()

print("Scegli quale area vuoi calcolare: ")
scelta = int(input(">>>"))
if scelta == 1:
    print("Hai scelto il quadrato")
    lato = float(input("Inserisci il valore del lato del quadrato "))
    print(f"L'area del quadrato, avente lato {lato} e': {lato * lato}")
elif scelta == 2:
    print("Hai scelto il rettangolo")
    base = float(input("Inserisci il valore della base: "))
    altezza = float(input("Inserisci il valore dell'altezza: "))
    print(f"L'Area del Rettangolo, avente base {base} e altezza {altezza} e': {base * altezza}")
elif scelta == 3:
    print("Hai scelto triangolo")
    base = float(input("Inserisci il valore della base: "))
    altezza = float(input("Inserisci il valore dell'altezza: "))
    print(f"L'Area del Rettangolo, avente base {base} e altezza {altezza} e': {(base * altezza) / 2}")
elif scelta == 4:
    print("Hai scelto il cerchio")
    raggio = float(input("inserisci il raggio: "))
    print(f"L'Area del Cerchio, avente il raggio {raggio} e': {(raggio * raggio) * 3.14}")
else:
    print("Nessun calcolo disponibile per la scelta che hai fatto")