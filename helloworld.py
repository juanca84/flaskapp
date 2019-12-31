from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hola amigos!!!</h1>'

@app.route('/articulos/')
def articulos():
    return '<h1>articulos</h1>'

@app.route('/acercade/')
def acercade():
    return '<h1>acerca de</h1>'

@app.route('/articulos/<id>')
def mostrar_articulo(id):
    return '<h1>mostramos los datos del articulo con id:{}</h1>'.format(id)

@app.errorhandler(404)
def page_not_found(error):
    return '<h2>Página no encontrada</h2>', 404
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
