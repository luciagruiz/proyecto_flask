from flask import Flask, render_template, abort, redirect, request
import json
import os

app = Flask(__name__)
port = os.getenv("PORT")

with open("static/data/nba.json") as n:
    datos=json.load(n)

@app.route('/')
def inicio():
    return render_template("index.html")


app.run("0.0.0.0",port,debug=True)