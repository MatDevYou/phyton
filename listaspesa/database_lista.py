import mysql.connector
from mysql.connector import Error

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connessione al database MySQL riuscita")
    except Error as err:
        print(f"Errore: '{err}'")

    return connection

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Errore: '{err}'")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query eseguita con successo")
    except Error as err:
        print(f"Errore: '{err}'")

# Connessione al database
connection = create_db_connection("localhost", "root", "Willy2003!", "spesa")

# Visualizza la tabella 'elements'
q_select_elements = """
SELECT *
FROM elements;
"""
results_elements = read_query(connection, q_select_elements)
if results_elements:
    print("Risultati della query:")
    for result in results_elements:
        print(result)
else:
    print("Nessun risultato restituito dalla query")

# Aggiungi un elemento
element_name = input("Inserisci il nome dell'elemento da aggiungere: ")
element_description = input("Inserisci la descrizione dell'elemento: ")
element_price = float(input("Inserisci il prezzo dell'elemento: "))

insert_query = f"""
INSERT INTO elements (name, description, price)
VALUES ('{element_name}', '{element_description}', {element_price});
"""

execute_query(connection, insert_query)

# Elimina un elemento
element_id_to_delete = int(input("Inserisci l'ID dell'elemento da eliminare: "))
delete_query = f"""
DELETE FROM elements
WHERE elements_id = {element_id_to_delete};
"""

execute_query(connection, delete_query)

# Chiudi la connessione al database
connection.close()
