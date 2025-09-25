from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    mensaje = "<h1>Hola bienvenido a la calculadora</h1>"
    mensaje += "<h2> Para poder usarla tendras que hacer tendras que hacer lo siguiente</h2>"
    mensaje += "<ol>"
    mensaje += "<li><h3>1.- Sumar http://127.0.0.1:5000/suma/10/20</h3></li>"
    mensaje += "<li><h2>2.- Restar http://127.0.0.1:5000/restar/10/20</h2></li>"
    mensaje += "<li><h2>3.- Multiplicación http://127.0.0.1:5000/multiplicacion/10/20</h2></li>"
    mensaje += "<li><h2>4.- División http://127.0.0.1:5000/division/10/20</h2></li>"
    mensaje += "<li><h2>5.- Maximo http://127.0.0.1:5000/maximo/10/20</h2></li>"
    mensaje += "<li><h2>6.- Minimo http://127.0.0.1:5000/minimo/10/20</h2></li>"
    mensaje += "</ol>"
    mensaje += "secreto http://127.0.0.1:5000/as"
    return mensaje

@app.route("/suma/<v1>/<v2>")
def sumar1(v1,v2):
    s = str(float(v1) + float(v2))
    mensaje = f"<h1>La suma de {v1} y {v2} es {s}"
    return mensaje

@app.route("/restar/<v1>/<v2>")
def restar1(v1,v2):
    s = str(float(v1) - float(v2))
    mensaje = f"<h1>La resta de {v1} y {v2} es {s}"
    return mensaje

@app.route("/multiplicacion/<v1>/<v2>")
def multiplicar1(v1,v2):
    s = str(float(v1) * float(v2))
    mensaje = f"<h1>La multiplicaión de {v1} y {v2} es {s}"
    return mensaje

@app.route("/division/<v1>/<v2>")
def dividir(v1,v2):
    s = str(float(v1) / float(v2))
    mensaje = f"<h1>La división de {v1} y {v2} es {s}"
    return mensaje

@app.route("/maximo/<v1>/<v2>")
def maximo1(v1,v2):
    if v1 < v2:
        mensaje = f"<h1>El maximo de {v1} y {v2} es {v2}"
    else:
        mensaje = f"<h1> El maximo de {v1} y {v2} es {v1}" 
    return mensaje

@app.route("/minimo/<v1>/<v2>")
def minimo1(v1,v2):
    if v1 < v2 :
        mensaje = f"<h1>El minimo de {v1} y {v2} es {v1}"
    else:
        mensaje = f"<h1>El minimo de {v1} y {v2} es {v2}"
    return mensaje

@app.route('/as')
def hola_ailin():
    return '<h1> Hola Ailin </h1>'

if __name__ =='__main__':
    app.run(debug=True)