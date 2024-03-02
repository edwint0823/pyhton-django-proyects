from flask import Flask, flash, redirect, url_for, render_template, request
from datetime import datetime
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'clave_secreta_flask'

app.config['MYSQL_HOST'] = 'localhost'
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "proyecto_flask"

mysql = MySQL(app)


# context processor
@app.context_processor
def date_now():
    return {'now': datetime.now()}


@app.route('/')
def index():
    edad = 101
    personas = ["Edwin", "Juan", "Maria", "Pedro"]
    return render_template('index.html', dato1="Valor", dato2="Valor 2", personas=personas, edad=edad)


@app.route('/informacion/')
@app.route('/informacion/<string:nombre>')
def info(nombre=None):
    texto = '<h1>otra pagina hola pepe </h1>'
    if nombre is not None:
        texto = f'<h1>otra pagina {nombre} <h1>'
    return render_template('informacion.html', texto=texto)


@app.route('/contacto')
@app.route('/contacto/<redireccion>')
def contacto(redireccion=None):
    if redireccion is not None:
        return redirect(url_for('lenguajes'))
    return render_template('contacto.html')


@app.route('/lenguajes-de-programacion')
def lenguajes():
    return render_template('lenguajes.html')


@app.route('/crear-coche', methods=['GET', 'POST'])
def crear_coche():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']
        cur = mysql.connection.cursor()

        cur.execute(f"INSERT INTO coches VALUES(null,%s, %s, %s, %s)", (marca, modelo, precio, ciudad))
        cur.connection.commit()
        flash('Has creado un coche exitosamente')
        return redirect(url_for('coches_list'))

    return render_template('crear_coche.html')


@app.route('/coches')
def coches_list():
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM coches ORDER BY id DESC")
    coches = cur.fetchall()
    cur.close()
    return (render_template('coches.html', coches=coches))


@app.route('/ver-coche/<coche_id>')
def ver_coche(coche_id):
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM coches WHERE id = %s", coche_id)
    coche = cur.fetchall()
    cur.close()
    return render_template('ver_coche.html', coche=coche[0])


@app.route('/borrar-coche/<coche_id>')
def borrar_coche(coche_id):
    cur = mysql.connection.cursor()
    cur.execute(f"DELETE FROM coches WHERE id = %s", coche_id)
    cur.connection.commit()
    flash('Has borrado un coche exitosamente')
    return redirect(url_for('coches_list'))


@app.route('/editar-coche/<coche_id>', methods=['GET', 'POST'])
def editar_coche(coche_id):
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']

        cur.execute("""
            UPDATE coches 
            SET marca = %s , modelo= %s , precio= %s, ciudad= %s 
            WHERE id = %s
        """, (marca, modelo, precio, ciudad, coche_id))
        cur.connection.commit()
        flash('Has actualizado el coche exitosamente')
        return redirect(url_for('coches_list'))

    cur.execute(f"SELECT * FROM coches WHERE id = %s", coche_id)
    coche = cur.fetchall()
    cur.close()
    return render_template('crear_coche.html', coche=coche[0])


if __name__ == "__main__":
    app.run(debug=True)
