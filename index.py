from flask import Flask, render_template

# definir como archivo de arranque
app = Flask(__name__)

# crear una ruta de la pagina principal


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/equipos')
def equipos():
    return render_template('equipos.html')

@app.route('/mantenimiento')
def mantenimiento():
    return render_template('mantenimiento.html')


if __name__ == '__main__':
    app.run(debug=True) 