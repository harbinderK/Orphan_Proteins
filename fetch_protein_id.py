import psycopg2
import sys
inFile = sys.argv[1]
with open(inFile, 'r') as file:
    i = next(file,0)
    while i :
        try:
            connection = psycopg2.connect(user = "postgres", password = "your_password", host = "0.0.0.0", database = "items")
    # update the user, password and host address where STRING database is installed.
            cursor = connection.cursor()
            postgresql_select = "SELECT protein_id from items.proteins where protein_external_id = "+i+";"
            cursor.execute(postgresql_select)
            record = cursor.fetchall()
            for row in record:
	        print row[0] 
        finally:
    #closing database connection.
            cursor.close()
            connection.close()
    	i = next(file,0)
