import os
import geopandas as gpd
from shapely.geometry import shape
from flask import Flask, render_template, request #importa a classe Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #criação de uma instancia da classe, o nome é um indicativo para o Python olhar em busca de arquivos
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] - False
#db = SQLAlchemy(app)

#class Upload(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    filename = 

app.config['UPLOAD_FOLDER'] = r"C:\Users\luan_\Documents\Luan\Programação\APS\2S\Carbono_Neutro\arquivo"


@app.route("/", methods=["GET","POST"]) #usado para mostrar ao Flask qual URL vai dar gatilho na função
def main():
    if (request.method == "POST"):
        file = request.files['file']
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], "teste.shp"))
        
        
        poligono = gpd.read_file(r"C:\Users\luan_\Documents\Luan\Programação\APS\2S\Carbono_Neutro\arquivo\Area_teste-polygon.shp")
        #print(poligono)
        print(shape(poligono.loc[0,'geometry']).area)
        
    return render_template("index.html")