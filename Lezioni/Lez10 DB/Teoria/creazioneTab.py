import MySQLdb
# Open database connection
db = MySQLdb.connect("localhost","utente","password","PYTHONDB" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
print(cursor)
# Drop table if it already exist using execute() method.
print(cursor.execute("DROP TABLE IF EXISTS IMPIEGATO"))

# Create table
sql = """CREATE TABLE IMPIEGATO (
ID INT(3) NOT NULL,
NOME CHAR(20) NOT NULL,
COGNOME CHAR(20),
ETA INT,
SESSO CHAR(1),
STIPENDIO FLOAT )"""
print(cursor.execute(sql))

# Alter table
sql = """ALTER TABLE IMPIEGATO
ADD PRIMARY KEY (ID)
"""
print(cursor.execute(sql))
# disconnect from server
db.close()