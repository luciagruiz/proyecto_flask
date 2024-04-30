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
    # Obtener la cadena de búsqueda y el criterio de búsqueda desde el formulario
    busqueda = request.form.get('busqueda', '').lower()
    criterio = request.form.get('criterio', '')

    equipos_encontrados = []

    # Filtrar equipos según la búsqueda y el criterio
    if busqueda and criterio:
        equipos_encontrados = [equipo for equipo in datos if equipo['teamName'].lower().startswith(busqueda) and equipo['conference'] == criterio]
    elif busqueda:
        equipos_encontrados = [equipo for equipo in datos if equipo['teamName'].lower().startswith(busqueda)]
    elif criterio:
        equipos_encontrados = [equipo for equipo in datos if equipo['conference'] == criterio]
    
    # Verificar si no se encontraron equipos
    if not equipos_encontrados:
        mensaje = "No se encontraron equipos que coincidan con los criterios de búsqueda."
    else:
        mensaje = None

    # Si se envió un formulario, mostrar la lista de equipos encontrados
    if request.method == 'POST':
        return render_template("equipos.html", equipos=equipos_encontrados, busqueda=busqueda, criterio=criterio, mensaje=mensaje)

    # Si es una solicitud GET, mostrar el formulario vacío
    return render_template("equipos.html", equipos=datos, mensaje=mensaje)



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
    else:
        mensaje = "El equipo no fue encontrado."
        return render_template("error404.html", mensaje=mensaje), 404

if __name__ == "__main__":
    app.run("0.0.0.0", port, debug=True)