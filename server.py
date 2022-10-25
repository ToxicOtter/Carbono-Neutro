import os
import geopandas as gpd
from shapely.geometry import shape, Polygon
from shapely import wkt
from flask import Flask, render_template, request
from fiona.drvsupport import supported_drivers
from pyproj import Geod


app = Flask(__name__) #criação de uma instancia da classe, o nome é um indicativo para o Python olhar em busca de arquivos

app.config['UPLOAD_FOLDER'] = r"/home/carbonoFree/.virtualenvs/my-virtualenv/site/files"


@app.route("/", methods=["GET","POST"])
def main():
    #Recebe o arquivo KML do usuario, calcula a area e retorna como parametro na renderização do HTML
    text=0

    if (request.method == "POST"):
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], "outro_teste.kml"))


        #gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'
        supported_drivers['KML'] = 'rw'
        my_map = gpd.read_file(r'/home/carbonoFree/.virtualenvs/my-virtualenv/site/files/outro_teste.kml', driver='KML')
        #text = shape(my_map.loc[0,'geometry']).area


        geod = Geod(ellps="WGS84")
        poly = wkt.loads(str(my_map.loc[0,'geometry']))
        area = abs(geod.geometry_area_perimeter(poly)[0])
        #text = (area * 2.353)/10000
        text = area
        #https://stackoverflow.com/questions/23697374/calculate-polygon-area-in-planar-units-e-g-square-meters-in-shapely

    return render_template("index.html", text=text)

if __name__ == '__main__':
    app.run()