import os
from dotenv import load_dotenv

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_mysqldb import MySQL

# definir como archivo de arranque
app = Flask(__name__)

#cargar archivo .env
load_dotenv()

host_mysql = os.getenv('HOST_SQL')
user_mysql = os.getenv('USER_MYSQL')
password_mysql = os.getenv('PASSWORD_MYSQL')
db_mysql = os.getenv('DB_MYSQL')

# Mysql connection
# conexion remota

app.config['MYSQL_HOST']=host_mysql
app.config['MYSQL_USER']=user_mysql
app.config['MYSQL_PASSWORD']=password_mysql
app.config['MYSQL_DB']=db_mysql
mysql = MySQL(app)

# settings
app.secret_key = 'mysecretkey'

#-----Definiendo rutas --------
# --------------------- pagina principal ------------------
@app.route('/')
def home():
    return render_template('home.html')

# --------------------- modulo de registro ------------------

@app.route('/registro')
def registro():
    # obtener registros de base de datos
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tecnicos')
    data = cur.fetchall()
    # enviar los datos al template
    return render_template('registro.html', tecnicos=data)

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
        #ejecutar consulta
        cur = mysql.connection.cursor()
        cur.execute(
            'INSERT INTO tecnicos (ce_tec, nom_tec, car_tec, cor_tec, equ_tec) VALUES (%s,%s,%s,%s,%s)', (id, nombre, cargo, email, equipo))
        mysql.connection.commit()
        cur.close()
        # enviar mensaje a traves de flash al usuario
        flash('Tecnico registrado Satisfactoriamente')
        # redireccionar a la pagina de registro 
        # mostrando los nuevos datos
        return redirect(url_for('registro'))

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
        return redirect(url_for('registro'))

    except:
        flash('ohh, ha ocurrido un error, prueba borrando las ordenes activas')
        return redirect(url_for('registro'))

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

    return render_template('edit-registro.html', tecnico=data[0])

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
        return redirect(url_for('registro'))

# --------------------- modulo de equipos ------------------

@app.route('/equipos')
def equipos():
    return render_template('equipos.html')

# --------------------- moudulo de mantenimiento ------------------
# la funcion obtiene los registros y los manda al template 
# mantenimiento a traves de data
@app.route('/mantenimiento')
def mantenimiento():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM orden_trabajo')
    data = cur.fetchall()
    return render_template('mantenimiento.html', ordenes=data)

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
