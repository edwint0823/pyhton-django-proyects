import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)
#
cursor = database.cursor(buffered=True)
""" 
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)
"""
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS vehiculos(
        id integer auto_increment not null,
        marcha varchar(40) not null,
        modelo varchar(40) not null,
        precio float(10,2) not null,
        CONSTRAINT pk_vehiculo PRIMARY KEY (id)
    )
    """
)
""" 
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
"""
# cursor.execute("INSERT INTO vehiculos VALUES (null, 'Opel', 'Astra', 18500)")
# database.commit()

coches = [
    ('Seat', 'Ibiza', 50000),
    ('Renault', 'Clio', 15000),
    ('Citroen', 'Saxo', 2000),
    ('Mercedes', 'Clase C', 35000),
]
#
# cursor.executemany("INSERT INTO vehiculos VALUES (null,%s, %s, %s)", coches)
# database.commit()

cursor.execute("SELECT * FROM vehiculos WHERE precio >= 15000")
result = cursor.fetchall()
for coche in result:
    print(coche)

# cursor.execute("DELETE FROM vehiculos")
# database.commit()
# print(cursor.rowcount, "records found")

# cursor.execute("UPDATE vehiculos SET precio=? WHERE precio = 15000", [2000])
# database.commit()
# print(cursor.rowcount, "records found")
database.close()
