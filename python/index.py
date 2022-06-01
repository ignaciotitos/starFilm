from flask import Flask, render_template, request
#from application import *
from scrapper_filmAffinity import movie, weee

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template("inicio.html")

@app.route('/busqueda', methods=['POST'])
def busqueda():
    id = request.form.get('Buscador')
    y = weee(id)
    #print(y)
    return 'Hola ' + y


if __name__ == '__main__':
    app.run()


