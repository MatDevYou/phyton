import MySQLdb
# Open database connection
db = MySQLdb.connect("localhost","utente","password","PYTHONDB" )

print(db)
# disconnect from server
db.close()