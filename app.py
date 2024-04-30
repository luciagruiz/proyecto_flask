from flask import Flask, render_template, abort, redirect, request, url_for
import json
import os

app = Flask(__name__)
port = os.getenv("PORT")

with open("static/data/nba.json") as n:
    datos=json.load(n)

@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/equipos', methods=['GET', 'POST'])
def equipos():
    if request.method == 'POST':
        busqueda = request.form.get('busqueda', '').lower()
        if busqueda:
            equipos_encontrados = [equipo for equipo in datos if equipo['teamName'].lower().startswith(busqueda)]
        else:
            equipos_encontrados = datos
        return redirect(url_for('listaequipos', equipos=json.dumps(equipos_encontrados)))
    return render_template("equipos.html")

@app.route('/listaequipos', methods=['GET', 'POST'])
def listaequipos():
    equipos = json.loads(request.args.get('equipos'))
    return render_template("listaequipos.html", equipos=equipos)

@app.route('/equipo/<int:id>')
@app.route('/equipo')
def equipo(id=None):
    if id is None:
        id = request.args.get('id')
    equipo_encontrado = next((equipo for equipo in datos if equipo['teamId'] == id), None)
    if equipo_encontrado:
        return render_template("equipo.html", equipo=equipo_encontrado)
    abort(404)

if __name__ == "__main__":
    app.run("0.0.0.0", port, debug=True)