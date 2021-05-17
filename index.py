from flask import Flask, render_template, redirect, url_for, request, flash

from flask_mysqldb import MySQL

# definir como archivo de arranque
app = Flask(__name__)

# Mysql connection
app.config['MYSQL_HOST'] = 'bonnnebwnn4sjw9twogv-mysql.services.clever-cloud.com'
app.config['MYSQL_USER'] = 'u13fjv8g9janha01'
app.config['MYSQL_PASSWORD'] = 'uz5RG7JhIYudobtbZ217'
app.config['MYSQL_DB'] = 'bonnnebwnn4sjw9twogv'
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
    try:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM tecnicos WHERE ce_tec  = {0}'.format(ce_tec))
        mysql.connection.commit()
        flash('Tecnico eliminado Satisfactoriamente')
        return redirect(url_for('registro'))

    except:
        flash('ohh, ha ocurrido un error, prueba borrando las ordenes activas')
        return redirect(url_for('registro'))


@app.route('/edit-tecnico/<string:ce_tec>')
def obtener_registro_tecnico(ce_tec):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tecnicos WHERE ce_tec = {0}'.format(ce_tec))
    data = cur.fetchall()

    return render_template('edit-registro.html', tecnico=data[0])


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
        return redirect(url_for('registro'))

# Equipos


@app.route('/equipos')
def equipos():
    return render_template('equipos.html')

# mantenimiento


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
    flash('Orden eliminada de manera correcta')
    return redirect(url_for('mantenimiento'))


if __name__ == '__main__':
    app.run()
