from flask import Flask
#from application import *

app = Flask(__name__)

welcome = """
<!DOCTYPE html>
    <html lang="es">
        <head>
            <meta charset="utf-8">
            <title>StarFilm</title>
            <meta name="Autores" content="Jaime Carrasco, Marta Nieto y Ignacio Titos">
        </head>
        <body>
            <header>
                <h1>StarFilm Comparator</h1>
            </header>
            <main>
                <form action="procesar.py" method="post">
                    <label for="Buscador">Película:</label>
                    <input type="text" id="Buscador" name="buscador"/><br/>
                </form>
            </main>
        </body>
    </html>
"""

@app.route('/')
def principal():
    return welcome

if __name__ == '__main__':
    app.run()


