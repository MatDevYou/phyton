
import database_lista

# Definizione della funzione switch
def switch(menu):
    if menu == "1":
        database_lista.visualizza_spesa()
    elif menu == "2":
        count = int(input("Indica quanti elementi hai comprato: "))
        for i in range(count):
            elemento = input("Inserisci l'elemento da aggiungere: ")
            database_lista.aggiungi_elemento(elemento)
        print("Elemento aggiunto con successo!")
    elif menu == "3":
        elemento_da_elim = input("Inserisci l'elemento da eliminare: ")
        database_lista.elimina_elemento(elemento_da_elim)
        database_lista.conn.commit()
        print("Elemento eliminato con successo!")
    else:
        print("Opzione non valida")

# Menu
print("Cosa vuoi fare?")
print("1. Visualizza spesa")
print("2. Aggiungi elemento")
print("3. Elimina elemento")

# Loop per il menu
while True:
    scelta = input("Inserisci il numero corrispondente all'azione desiderata (o 'q' per uscire): ")
    if scelta == 'q':
        break
    switch(scelta)

# Chiusura della connessione al database
database_lista.conn.close()
