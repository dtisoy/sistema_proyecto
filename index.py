from flask import Flask, render_template, redirect, url_for, request, flash

from flask_mysqldb import MySQL

# definir como archivo de arranque
app = Flask(__name__)

# Mysql connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'usuario1'
app.config['MYSQL_DB'] = 'proyecto_SistemaYRedes'
mysql = MySQL(app)

# settings
app.secret_key = 'mysecretkey'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/registro')
def registro():
    # obtener registros de base de datos
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tecnicos')
    data = cur.fetchall()
    return render_template('registro.html', tecnicos=data)


@app.route('/registrar_tecnico', methods=['POST'])
def registrar_tecnico():
    if request.method == 'POST':
        id = request.form['cedula']
        nombre = request.form['nombres']
        cargo = request.form['cargo']
        email = request.form['correo']
        equipo = request.form['equipo']

        cur = mysql.connection.cursor()
        cur.execute(
            'INSERT INTO tecnicos (ce_tec, nom_tec, car_tec, cor_tec, equ_tec) VALUES (%s,%s,%s,%s,%s)', (id, nombre, cargo, email, equipo))
        mysql.connection.commit()
        cur.close()
        flash('Tecnico registrado Satisfactoriamente')
        return redirect(url_for('registro'))

# configurando una ruta que reciba un parametro de la base de datos


@app.route('/delete/<string:ce_tec>')
def delete_tecnico(ce_tec):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM tecnicos WHERE ce_tec  = {0}'.format(ce_tec))
    mysql.connection.commit()
    return redirect(url_for('registro'))


@app.route('/equipos')
def equipos():
    return render_template('equipos.html')


@app.route('/mantenimiento')
def mantenimiento():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM orden_trabajo')
    data = cur.fetchall()
    return render_template('mantenimiento.html', ordenes=data)


@app.route('/delete-orden/<string:id_ord>')
def delete_orden(id_ord):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM orden_trabajo WHERE id_ord  = {0}'.format(id_ord))
    mysql.connection.commit()
    return redirect(url_for('mantenimiento'))


if __name__ == '__main__':
    app.run(debug=True)
