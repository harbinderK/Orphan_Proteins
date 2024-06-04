import psycopg2
import sys
inFile = sys.argv[1]
with open(inFile, 'r') as file:
    i = next(file,0)
    while i :
	#print(i.rstrip())
        try:
            connection = psycopg2.connect(user = "postgres", password = "your_password", host = "0.0.0.0", database = "network")
    # update the user, password and host address where STRING database is installed.
            cursor = connection.cursor()
            postgresql_select = "SELECT node_id_a, node_id_b, combined_score \n from network.node_node_links where node_id_a ="+i+" and combined_score > '699' ;  "
	    cursor.execute(postgresql_select)
            record = cursor.fetchall()
            for row in record:
                print row[0], row[1], row [2] 
        finally:
   # closing database connection.
      #  if(connection):
            cursor.close()
            connection.close()
        i = next(file,0)
