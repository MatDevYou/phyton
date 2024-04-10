def mostra_tabella(tabella):
    for riga in tabella:
        print("|".join(riga))
        print("-" * 5)

def controlla_vittoria(tabella, segno):
    for riga in tabella:
        if all(cell == segno for cell in riga):
            return True
    for colonna in range(3):
        if all(tabella[riga][colonna] == segno for riga in range(3)):
            return True
    if tabella[0][0] == tabella[1][1] == tabella[2][2] == segno:
        return True
    if tabella[0][2] == tabella[1][1] == tabella[2][0] == segno:
        return True
    return False

def tris():
    tabella = [[" " for _ in range(3)] for _ in range(3)]
    giocatori = ["X", "O"]
    turno = 0

    while True:
        mostra_tabella(tabella)
        giocatore_corrente = giocatori[turno % 2]
        print(f"Turno del giocatore {giocatore_corrente}")

        while True:
            riga = int(input("Inserisci la riga (da 1 a 3): ")) - 1
            colonna = int(input("Inserisci la colonna (da 1 a 3): ")) - 1
            if 0 <= riga < 3 and 0 <= colonna < 3 and tabella[riga][colonna] == " ":
                tabella[riga][colonna] = giocatore_corrente
                break
            else:
                print("Mossa non valida. Riprova.")

        if controlla_vittoria(tabella, giocatore_corrente):
            mostra_tabella(tabella)
            print(f"Il giocatore {giocatore_corrente} ha vinto!")
            break
        elif all(tabella[riga][colonna] != " " for riga in range(3) for colonna in range(3)):
            mostra_tabella(tabella)
            print("La partita è finita in pareggio!")
            break

        turno += 1

if __name__ == "__main__":
    tris()
