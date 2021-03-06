import os
from dotenv import load_dotenv

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_mysqldb import MySQL

# definir como archivo de arranque
app = Flask(__name__)

# cargar archivo .env
load_dotenv()

host_mysql = os.getenv('HOST_SQL')
user_mysql = os.getenv('USER_MYSQL')
password_mysql = os.getenv('PASSWORD_MYSQL')
db_mysql = os.getenv('DB_MYSQL')

# Mysql connection
# conexion remota

app.config['MYSQL_HOST'] = host_mysql
app.config['MYSQL_USER'] = user_mysql
app.config['MYSQL_PASSWORD'] = password_mysql
app.config['MYSQL_DB'] = db_mysql
mysql = MySQL(app)

# settings
app.secret_key = 'mysecretkey'

# -----Definiendo rutas --------
# --------------------- pagina principal ------------------


@app.route('/')
def home():
    return render_template('home.html')

# --------------------- modulo de registro ------------------


@app.route('/registro')
def registro():

    # enviar los datos al template
    return render_template('registro/form-registro.html')

# recibir los datos de la pagina de registro
# e insertarlo en la base de datos


@app.route('/registrar_tecnico', methods=['POST'])
def registrar_tecnico():
    # obtener los datos del formulario
    # a traves de los name
    if request.method == 'POST':
        id = request.form['cedula']
        nombre = request.form['nombres']
        cargo = request.form['cargo']
        email = request.form['correo']
        equipo = request.form['equipo']
        # ejecutar consulta
        cur = mysql.connection.cursor()
        cur.execute(
            'INSERT INTO tecnicos (ce_tec, nom_tec, car_tec, cor_tec, equ_tec) VALUES (%s,%s,%s,%s,%s)', (id, nombre, cargo, email, equipo))
        mysql.connection.commit()
        cur.close()
        # enviar mensaje a traves de flash al usuario
        flash('Tecnico registrado Satisfactoriamente')
        # redireccionar a la pagina de registro
        # mostrando los nuevos datos
        return redirect(url_for('tecnicos'))

# Eliminar un registro de la tabla tecnicos


@app.route('/delete/<string:ce_tec>')
def delete_tecnico(ce_tec):
    # se inserta un try porque ocurre un error
    # debido a que existe una relacion de llave foranea
    # con la tabla de ordenes de trabajo
    try:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM tecnicos WHERE ce_tec  = {0}'.format(ce_tec))
        mysql.connection.commit()
        flash('Tecnico eliminado Satisfactoriamente')
        return redirect(url_for('tecnicos'))

    except:
        flash('ohh, ha ocurrido un error, prueba borrando las ordenes activas')
        return redirect(url_for('tecnicos'))

# obtener los datos de una fila de la tabla tecnicos
# los datos son enviados a traves del enlace editar.
# se obiene el id del dato a editar


@app.route('/edit-tecnico/<string:ce_tec>')
def obtener_registro_tecnico(ce_tec):
    # se busca el registro en la bd y se lo envia al template update
    # con los datos.
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tecnicos WHERE ce_tec = {0}'.format(ce_tec))
    data = cur.fetchall()

    return render_template('registro/edit-registro.html', tecnico=data[0])

# recibe la redireccion con los datos a traves del metodo post


@app.route('/update-tecnico/<string:ce_tec>', methods=['POST'])
def update_tecnico(ce_tec):
    if request.method == 'POST':
        id = request.form['cedula']
        nombre = request.form['nombres']
        cargo = request.form['cargo']
        email = request.form['correo']
        equipo = request.form['equipo']

        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE tecnicos
            SET nom_tec=%s,
                car_tec=%s, 
                cor_tec=%s, 
                equ_tec=%s
            WHERE ce_tec=%s
         """, (nombre, cargo, email, equipo, id))
        mysql.connection.commit()
        cur.close()

        flash('Datos actualizados de manera correcta')
        # se redirecciona al template registro para mostrar los cambios.
        return redirect(url_for('tecnicos'))

@app.route('/tecnicos')
def tecnicos():
    # obtener registros de base de datos
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tecnicos')
    data = cur.fetchall()
    return render_template('registro/tabla-tecnicos.html', tecnicos=data)

# --------------------- modulo de equipos ------------------


@app.route('/equipos')
def equipos():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM equipos')
    data = cur.fetchall()
    return render_template('equipos/tabla-equipos.html', equipos=data)

@app.route('/registrar-equipo')
def registrar_equipo():
    return render_template('equipos/formulario-equipos.html')

# --------------------- Eliminar equipos ------------------


@app.route('/delete-equipo/<string:id_equ>')
def delete_equipo(id_equ):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM equipos WHERE id_equ  = {0}'.format(id_equ))
    mysql.connection.commit()
    flash('Equipo eliminado de manera correcta')
    # se redirige al template para ver los cambios
    return redirect(url_for('equipos'))

# --------------------- moudulo de mantenimiento ------------------
# la funcion obtiene los registros y los manda al template
# mantenimiento a traves de data


@app.route('/mantenimiento')
def mantenimiento():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM orden_trabajo')
    data = cur.fetchall()
    return render_template('mantenimiento/tabla-mantenimiento.html', ordenes=data)

# se ejecuta la consulta de eliminacion solicitada
# a traves del boton del template


@app.route('/delete-orden/<string:id_ord>')
def delete_orden(id_ord):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM orden_trabajo WHERE id_ord  = {0}'.format(id_ord))
    mysql.connection.commit()
    flash('Orden eliminada de manera correcta')
    # se redirige al template para ver los camibios
    return redirect(url_for('mantenimiento'))


if __name__ == '__main__':
    app.run(debug=True)
