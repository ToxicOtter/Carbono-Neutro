import os
import geopandas as gpd
from shapely.geometry import shape, Polygon
from flask import Flask, render_template, request #importa a classe Flask
from fiona.drvsupport import supported_drivers


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
    text = 0
    if (request.method == "POST"):
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], "outro_teste.kml"))

        #dom = parse(r'C:\Users\luan_\Documents\Luan\Programação\APS\2S\Carbono_Neutro\arquivo\Area teste.kml')
        #entries = []
        #placemarks = dom.getElementsByTagName("Placemark")

        #def subfolders(node):
        #    if node.parentNode == dom.documentElement:
        #        return ""
        #    else:
        #        foldername = node.getElementsByTagName("name")[0].firstChild.data
        #        path = subfolders(node.parentNode) + "/" + foldername
        #        return path

        #for i in placemarks:
        #    longitude = i.getElementsByTagName("longitude")[0].firstChild.data
        #    latitude = i.getElementsByTagName("latitude")[0].firstChild.data
        #    coordinates = i.getElementsByTagName("coordinates")[0].firstChild.data
        #    try:
        #        name = i.getElementsByTagName("name")[0].firstChild.data
        #    except:
        #        name = ""
        #    parent = i.parentNode
        #    foldername = parent.getElementsByTagName("name")[0].firstChild.data
        #    path = subfolders(parent) 
        #    entries.append((name, latitude, longitude, coordinates, foldername, path)) # List of tuples

        #df = pd.DataFrame(entries, columns=('name', 'latitude', 'longitude', 'coordinates', 'folder', 'path'))
        #gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude, crs="EPSG:4326"))
        #gdf = gpd.GeoDataFrame(df, geometry=Polygon(df.coordinates[0]), crs="EPSG:4326")
        #print(f"coordinates: {df['coordinates'][0]}")





        #poligono = gpd.read_file(r"C:\Users\luan_\Documents\Luan\Programação\APS\2S\Carbono_Neutro\arquivo\Area_teste-polygon.shp")
        #print(f"poligono: {poligono.geometry[0]}")
        #print(shape(poligono.loc[0,'geometry']).area)
        


        #gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'
        supported_drivers['KML'] = 'rw'
        my_map = gpd.read_file(r'C:\Users\luan_\Documents\Luan\Programação\APS\2S\Carbono_Neutro\arquivo\outro_teste.kml', driver='KML')
        #print(shape(my_map.loc[0,'geometry']).area)
        text = shape(my_map.loc[0,'geometry']).area

    print(text)
    return render_template("index.html", text=text)