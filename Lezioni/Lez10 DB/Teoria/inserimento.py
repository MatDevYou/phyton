import MySQLdb
# Open database connection
db = MySQLdb.connect("localhost","utente","password","PYTHONDB" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO IMPIEGATO(ID, NOME,
COGNOME, ETA, SESSO, STIPENDIO)
VALUES (1,'Paolino', 'Paperino', 20, 'M', 2000)"""
try:
# Execute the SQL command
print(cursor.execute(sql))
# Commit your changes in the database
db.commit()
except:
# Rollback in case there is any error
print("ERRORE, effettuo il ROLLBACK!")
db.rollback()

db.close()