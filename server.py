import os
import geopandas as gpd
from shapely.geometry import shape, Polygon
from shapely import wkt
from flask import Flask, render_template, request, url_for
from fiona.drvsupport import supported_drivers
from pyproj import Geod

gasto_final = [0]
cred_final = [0]

app = Flask(__name__) #criação de uma instancia da classe, o nome é um indicativo para o Python olhar em busca de arquivos

app.config['UPLOAD_FOLDER'] = r"/home/carbonoFree/.virtualenvs/my-virtualenv/site/files"


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/personal",methods=["GET","POST"])
def personal():
    return render_template('personal.html')

@app.route("/para-empresa", methods=["GET","POST"])
def company():
    return render_template("company.html")
    #Recebe o arquivo KML do usuario, calcula a area e retorna como parametro na renderização do HTML
    """ text=0
    gasto = round(gasto_final[0],2)
    cred = round(cred_final[0],2)

    if (request.method == "POST"):
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], "outro_teste.kml"))


        supported_drivers['KML'] = 'rw'
        my_map = gpd.read_file(r'/home/carbonoFree/.virtualenvs/my-virtualenv/site/files/outro_teste.kml', driver='KML')


        geod = Geod(ellps="WGS84")
        poly = wkt.loads(str(my_map.loc[0,'geometry']))
        area = abs(geod.geometry_area_perimeter(poly)[0])
        text = area """
    

@app.route("/personal-res",methods=["GET","POST"])
def personalRes():
    #Recebe o arquivo KML do usuario, calcula a area e retorna como parametro na renderização do HTML
    text=0
    gasto = round(gasto_final[0],2)
    cred = round(cred_final[0],2)

    if (request.method == "POST"):
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], "outro_teste.kml"))


        supported_drivers['KML'] = 'rw'
        my_map = gpd.read_file(r'/home/carbonoFree/.virtualenvs/my-virtualenv/site/files/outro_teste.kml', driver='KML')


        geod = Geod(ellps="WGS84")
        poly = wkt.loads(str(my_map.loc[0,'geometry']))
        area = abs(geod.geometry_area_perimeter(poly)[0])
        text = area
    return render_template("personal.html",text=text,gasto=round(gasto,2), cred=round(cred,2))

###################### to solve problem with browser cache #########################
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.route("/empresa",methods=["POST"])
def empresa():
    gasto = 0
    cred = 0
    for i in range(0,len(request.json['combs_est'])):
        tipo = request.json['combs_est'][str(i)][0]
        qtd = int(request.json['combs_est'][str(i)][1])

        match tipo:
            case "acetileno":
                gasto += float(qtd)*(3/1000) # gasto = total kg co2 gerado pela queima de 1kg de acetileno
            case "alcatrão":
                gasto += float(qtd) * (2.888/ 1000) # gasto= total kg co2 gerado pela queima de 1m3 de alcatrao
            case "asfaltos":
                gasto += float(qtd) * (3.389/ 1000)  # gasto = total kg co2 gerado pela queima de 1m3 de alcatrao
            case "carvão_metalúrgico":
                gasto += float(qtd) * (2543/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "coque_petroleo":
                gasto += float(qtd) * (3.563/ 1000)  # gasto = total kg co2 gerado pela queima de 1m3
            case "etano":
                gasto += float(qtd) * (2.858/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "gas_refinaria":
                gasto += float(qtd) * (2.850/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "gas_natural_Seco":
                gasto += float(qtd) * (2.07/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "gas_natural_umido":
                gasto += float(qtd) * (2.333/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "gas_aut_pura":
                gasto += float(qtd) * (2.24/ 1000)  # gasto = total kg co2 gerado pela queima de 1l
            case "gas_aviao":
                gasto += float(qtd) * (2.26/ 1000)  # gasto = total kg co2 gerado pela queima de 1l
            case "Liq_gas_natural":
                gasto += float(qtd) * (2.836/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "lubrificantes":
                gasto += float(qtd) * (2.72/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "nafta":
                gasto += float(qtd) * (2.291/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "oleo_diesel":
                gasto += float(qtd) * (2.63/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "oleo_combustivel":
                gasto += float(qtd) * (3.11/ 1000)  # gasto = total kg co2 gerado pela queima de 1l
            case "oleol_residual":
                gasto += float(qtd) * (2.947/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "petroloe_bruto":
                gasto += float(qtd) * (2.931/ 1000)  # gasto = total kg co2 gerado pela queima de 1m3
            case "querosene_aviação":
                gasto += float(qtd) * (3.113/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "res_industriais":
                gasto += float(qtd) * (143.000/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "etanol":
                gasto += float(qtd) * (1.58/ 1000)  # gasto = total kg co2 gerado pela queima de 1l
            case "biodiesel_b100":
                gasto += float(qtd) * (2.46/ 1000)  # gasto = total kg co2 gerado pela queima de 1l
            case "biogas":
                gasto += float(qtd) * (2.754/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "carvão_vegetal":
                gasto += float(qtd) * (2.886/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "lenha":
                gasto += float(qtd) * (1.817/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "residuos":
                gasto += float(qtd) * (1.161/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
    for i in range(0,len(request.json['combs_est'])):
        tipo = request.json['combs_est'][str(i)][0]
        qtd = int(request.json['combs_est'][str(i)][1])
    for j in range(0,len(request.json['combs_mvl'])):
        mov = request.json['combs_mvl'][str(i)][0]
        qtd_mov = int(request.json['combs_mvl'][str(i)][1])
        match mov:
            case "gas_aut_pura":
                gasto += float(qtd_mov) * (2.24/ 1000)  # gasto = total kg co2 gerado pela queima de 1l
            case "etanol":
                gasto += float(qtd_mov) * (1.58/ 1000)  # gasto = total kg co2 gerado pela queima de 1l
            case "biodiesel_b100":
                gasto += float(qtd_mov) * (2.46/ 1000)  # gasto = total kg co2 gerado pela queima de 1l
            case "glp":
                gasto += float(qtd_mov) * (2.754/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "gnv":
                gasto += float(qtd_mov) * (2.886/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton
            case "diesel":
                gasto += float(qtd_mov) * (1.817/ 1000)  # gasto = total kg co2 gerado pela queima de 1ton

    gasto += float(request.json["co2"])*(1/ 1000)
    gasto += float(request.json["hfc_23"])*(12400/ 1000)
    gasto += float(request.json["n2o"])*(265/ 1000)
    gasto += float(request.json["ch4"])*(28/ 1000)
    
    gasto += float(request.json["ener_jan"])*0.1164
    gasto += float(request.json["ener_fev"])*0.08200
    gasto += float(request.json["ener_mar"])*0.0673
    gasto += float(request.json["ener_abr"])*0.0764
    gasto += float(request.json["ener_mai"])*0.0883
    gasto += float(request.json["ener_jun"])*0.1491
    gasto += float(request.json["ener_jul"])*0.1634
    gasto += float(request.json["ener_ago"])*0.1743
    gasto += float(request.json["ener_set"])*0.1699
    gasto += float(request.json["ener_out"])*0.1786
    gasto += float(request.json["ener_nov"])*0.1484
    gasto += float(request.json["ener_dez"])*0.1029
    
    gasto = round(gasto,2)
    gasto_final.clear()
    gasto_final.append(gasto)
    arvore = int(gasto / 0.165105)
    cred = gasto * 68.745
    cred_final.clear()
    cred_final.append(cred)

    
    return {
        "gasto": gasto,
        "cred": round(cred,2),
        "arvore": arvore
    }

@app.route("/pessoa",methods=["GET","POST"])
def pessoa():
    cred = 0
    gasto = 0
    med_elet = (0.1164 + 0.08200 + 0.0673 + 0.0764 + 0.0883 + 0.1491 + 0.1634 + 0.1743 + 0.1699 + 0.1786 + 0.1484 + 0.1029)/12

    if (request.method == "POST"):
        gasto += float(request.json["aviao"]) * 0.17
        gasto += float(request.json["botija"])*0.455
        gasto += float(request.json["condicionado"])*0.5
        gasto += (float(request.json["eletricidade"])*med_elet*12)/1000

        if (request.json['recicla'] == "sim"):
            gasto += 0.06
        else:
            gasto += 0.23 


    gasto_final.clear()
    gasto_final.append(gasto)
    arvore = int(gasto / 0.165105)
    cred = gasto * 68.745
    cred_final.clear()
    cred_final.append(cred)

    return {
        "gasto": gasto,
        "cred": round(cred,2),
        "arvore": arvore
    }

if __name__ == '__main__':
    app.run()