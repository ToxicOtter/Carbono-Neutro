import os
import geopandas as gpd
from shapely.geometry import shape, Polygon
from shapely import wkt
from flask import Flask, render_template, request
from fiona.drvsupport import supported_drivers
from pyproj import Geod


app = Flask(__name__) #criação de uma instancia da classe, o nome é um indicativo para o Python olhar em busca de arquivos

app.config['UPLOAD_FOLDER'] = r"/home/carbonoFree/.virtualenvs/my-virtualenv/site/files"


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/para-empresa", methods=["GET","POST"])
def company():
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
    return render_template("company.html",text=text)

@app.route("/combustivel",methods=["GET","POST"])
def combustivel():
    gasto = 0
    tipo_combs = request.form["tipo_combustivel"]
    cons = float(request.form["qtd_combs"])

    if (request.method == "POST"):
        match tipo_combs:
            case "acetileno":
                gasto = cons*(3/1000) # gasto = total kg co2 gerado pela queima de 1kg de acetileno
            case "alcatrão":
                gasto = cons * (2.888/ 1000) # gasto= total kg co2 gerado pela queima de 1m3 de alcatrao
            case "asfaltos":
                gasto = cons * (3.389/ 1000)  # gasto = total kg co2 gerado pela queima de 1m3 de alcatrao
            case "carvão_metalúrgico":
                gasto = cons * (2.543/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "coque_petroleo":
                gasto = cons * (3.563/ 1000)  # gasto = total kg co2 gerado pela queima de 1m3
            case "etano":
                gasto = cons * (2.858/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "gas_refinaria":
                gasto = cons * (2.850/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "gas_natural_Seco":
                gasto = cons * (2.07/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "gas_natural_umido":
                gasto = cons * (2.333/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "gas_aut_pura":
                gasto = cons * (2.24/ 1000)  # gasto = total kg co2 gerado pela queima de 1l
            case "gas_aviao":
                gasto = cons * (2.26/ 1000)  # gasto = total kg co2 gerado pela queima de 1l
            case "Liq_gas_natural":
                gasto = cons * (2.836/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "lubrificantes":
                gasto = cons * (2.72/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "nafta":
                gasto = cons * (2.291/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "oleo_diesel":
                gasto = cons * (2.63/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "oleo_combustivel":
                gasto = cons * (3.11/ 1000)  # gasto = total kg co2 gerado pela queima de 1l
            case "oleol_residual":
                gasto = cons * (2.947/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "petroloe_bruto":
                gasto = cons * (2.931/ 1000)  # gasto = total kg co2 gerado pela queima de 1m3
            case "querosene_aviação":
                gasto = cons * (3.113/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "res_industriais":
                gasto = cons * (143.000/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "etanol":
                gasto = cons * (1.58/ 1000)  # gasto = total kg co2 gerado pela queima de 1l
            case "biodiesel_b100":
                gasto = cons * (2.46/ 1000)  # gasto = total kg co2 gerado pela queima de 1l
            case "biogas":
                gasto = cons * (2.754/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "carvão_vegetal":
                gasto = cons * (2.886/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "lenha":
                gasto = cons * (1.817/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "residuos":
                gasto = cons * (1.161/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton

        gasto += float(request.form["co2"])*(1/ 1000)
        gasto += float(request.form["hfc_23"])*(12400/ 1000)
        gasto += float(request.form["n2o"])*(265/ 1000)
        gasto += float(request.form["ch4"])*(28/ 1000)
        
        gasto += float(request.form["ener_jan"])*0.1164
        gasto += float(request.form["ener_fev"])*0.08200
        gasto += float(request.form["ener_mar"])*0.0673
        gasto += float(request.form["ener_abr"])*0.0764
        gasto += float(request.form["ener_mai"])*0.0883
        gasto += float(request.form["ener_jun"])*0.1491
        gasto += float(request.form["ener_jul"])*0.1634
        gasto += float(request.form["ener_ago"])*0.1743
        gasto += float(request.form["ener_set"])*0.1699
        gasto += float(request.form["ener_out"])*0.1786
        gasto += float(request.form["ener_nov"])*0.1484
        gasto += float(request.form["ener_dez"])*0.1029

    
        gasto = round(gasto,2)
    arvore = int(gasto / 0.165105)
    return render_template("company.html", gasto=gasto, arvore=arvore)


if __name__ == '__main__':
    app.run()