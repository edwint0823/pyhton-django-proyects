import sqlite3

# conexion

conexion = sqlite3.connect('pruebas.db')

# cursor
cursor = conexion.cursor()
# crear tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
   id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
   titulo VARCHAR(255) NOT NULL, 
   descripcion TEXT, 
   precio int(255)
);""")
# GUARDAR CAMBIOS
conexion.commit()

# Borrar registros
# cursor.execute("DELETE FROM produtos")

# Insertar datos
# cursor.execute("INSERT INTO productos VALUES (null,'Producto 1', 'Descripción del producto', 200)")
# conexion.commit()

# insertar varias registros
productos_insert = [
    ("Portatil", "Portatil lenovo", 800),
    ("Smartphone", "marca samsung", 1800),
    ("Silla", "ergonomica de oficina", 700),
    ("Cortina", "de color verde", 700)
]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos_insert)
conexion.commit()

# Update
cursor.execute("UPDATE productos SET precio=? WHERE precio = 800", [2000])
# listar
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()
for producto in productos:
    print(f"id {producto[0]}")
    print(f"Titulo {producto[1]}")
    print(f"Descripción {producto[2]}")
    print(f"Precio {producto[3]}")
    print("\n")

# primir registro
cursor.execute("SELECT * FROM productos;")
producto = cursor.fetchone()
print(producto)

# cerrar
conexion.close()
