import random

def scegli_parola():
    animali = ["stambecco", "gabbiano", "formichiere", "lupo delle nevi", "pesce palla", "koala", "donnola", "puzzola", "pesce spada", "tonno", "pidocchio", "sanguisuga", "lumaca"]
    return random.choice(animali)

def mostra_parola(parola, lettere_indovinate):
    parola_nascosta = ""
    for lettera in parola:
        if lettera in lettere_indovinate:
            parola_nascosta += lettera + " "
        else:
            parola_nascosta += "_ "
    return parola_nascosta

def gioca():
    nome = input("Ciao! Come ti chiami? ")

    print("\nBenvenuto,", nome, "al Gioco dell'Impiccato sugli Animali!\n")

    while True:
        parola_da_indovinare = scegli_parola()
        lettere_indovinate = []
        tentativi_rimasti = 8

        print("INDOVINA LA PAROLA SEGRETA.\n")

        while tentativi_rimasti > 0:
            print("Parola da indovinare:", mostra_parola(parola_da_indovinare, lettere_indovinate))
            print("Tentativi rimasti:", tentativi_rimasti)
            print()

            lettera_utente = input("Indovina una lettera: ").lower()

            if lettera_utente in lettere_indovinate:
                print("Hai già indovinato questa lettera!")
            elif lettera_utente in parola_da_indovinare:
                print("Bravo! Hai indovinato una lettera.")
                lettere_indovinate.append(lettera_utente)
            else:
                print("Oops! Questa lettera non fa parte della parola segreta.")
                print()
                tentativi_rimasti -= 1

            if mostra_parola(parola_da_indovinare, lettere_indovinate).replace(" ", "") == parola_da_indovinare:
                print("Complimenti! Hai indovinato la parola:", parola_da_indovinare)
                break

        if tentativi_rimasti == 0:
            print("Mi dispiace, hai esaurito i tentativi. La parola segreta era:", parola_da_indovinare)

        scelta = input("Vuoi giocare di nuovo? (sì/no): ").lower().strip()
        if scelta == "no":
            break

gioca()
