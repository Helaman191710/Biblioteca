#mi pagina web flask 
from flask import *
import pymongo
from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
MONGO_HOST="localhost"
MONGO_PUERTO="27017"
MONGO_URL="mongodb://localhost:27017"
cliente = MongoClient(MONGO_URL)
db = cliente.flask
coleccion=db.libros
app = Flask(__name__)


@app.route('/')#inicio
def pagina1():
    return render_template("pagina_principal.html")

#########################################################################################################################
@app.route('/3')#uestionario de videojuegos 
def pagina3():
    return render_template("cuestionario.html")

registros={}
numero_r=0
titulo = 0
autor= 0
no_pagina =0
fec_estreno=0
libro_fav=0
@app.route('/4',methods =['POST'])#envio de /3 
def pagina4():
    if request.method =='POST':
        global nombre, marca, donde, tiempo, fav, numero_r
        titulo= request.form['titulo']
        autor = request.form['autor']
        no_pagina = request.form['no_pagina']
        fec_estreno = request.form['fec_estreno']
        libro_fav =request.form['libro_fav']

        numero_r = +1
        id_encuesta = (str(numero_r))
        nueva_encuesta={
            "titulo" : titulo,
            "autor": autor,
            "no_pagina": no_pagina,
            "fec_estreno": fec_estreno,
            "libro_fav": libro_fav
        }
        registros.update({id_encuesta : nueva_encuesta})
        coleccion.insert_one(nueva_encuesta)
        print(nueva_encuesta)
        return redirect('http://localhost:5000/')
#################################################################################################
if __name__ == '__main__':
   app.run()