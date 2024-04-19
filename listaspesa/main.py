elementi = []

def switch(menu):
    if menu == "1":
        # Visualizza la lista degli elementi
        print("La lista degli elementi è:", elementi)
    elif menu == "2":
        # Aggiungi un elemento alla lista
        elemento = input("Inserisci l'elemento da aggiungere: ")
        elementi.append(elemento)
        print("Elemento aggiunto con successo!")
    elif menu == "3":
        # Elimina un elemento dalla lista
        if len(elementi) == 0:
            print("La lista è vuota. Non ci sono elementi da eliminare.")
        else:
            print("La lista degli elementi attuale è:", elementi)
            elemento_da_elim = input("Inserisci l'elemento da eliminare: ")
            if elemento_da_elim in elementi:
                elementi.remove(elemento_da_elim)
                print("Elemento eliminato con successo!")
            else:
                print("Elemento non trovato nella lista.")
    else:
        print("Opzione non valida")

a = 0

print("Cosa vuoi fare?")
print("1. Visualizza spesa")
print("2. Aggiungi elemento")
print("3. Elimina elemento")

while a < 4:
    scelta = input("Inserisci il numero corrispondente all'azione desiderata: ")
    switch(scelta)
    a += 1
