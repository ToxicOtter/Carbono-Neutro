$("#calcule").submit(function(e) {
    e.preventDefault();
});

function enviarDadosEmpresa(){
    let form = document.forms.calcule;
    let formData = new FormData(form);

    let combEstNome = formData.getAll('tipo_combustivel');
    let combEstValor = formData.getAll('qtd_combs');

    let combMvlNome = formData.getAll('combs_mov');
    let combMvlValor = formData.getAll('qtd_mov');

    let combEstacionario = {};
    let combMovel = {};

    for (let i=0;i<combEstNome.length;i++){
        combEstacionario[i] = [combEstNome[i],combEstValor[i]];
    };

    for (let i=0;i<combMvlNome.length;i++){
        combMovel[i] = [combMvlNome[i],combMvlValor[i]];
    };

    let dados = {
        "combs_est": combEstacionario,
        "combs_mvl": combMovel,
        "co2": formData.get('co2'),
        "hfc_23": formData.get('hfc_23'),
        "n2o": formData.get('n2o'),
        "ch4": formData.get('ch4'),
        "ener_jan": formData.get("ener_jan"),
        "ener_fev": formData.get("ener_fev"),
        "ener_mar": formData.get("ener_mar"),
        "ener_abr": formData.get("ener_abr"),
        "ener_mai": formData.get("ener_mai"),
        "ener_jun": formData.get("ener_jun"),
        "ener_jul": formData.get("ener_jul"),
        "ener_ago": formData.get("ener_ago"),
        "ener_set": formData.get("ener_set"),
        "ener_out": formData.get("ener_out"),
        "ener_nov": formData.get("ener_nov"),
        "ener_dez": formData.get("ener_dez")
    };

    $.ajax ({
        type: "POST",
        url: "/empresa",
        data: JSON.stringify(dados),
        contentType: "application/json",
        success: function(resp){
            resEmpresa(resp);
        }
    });
};

function resEmpresa(data){
    let divRes = document.getElementById("results");
    let cred = document.getElementById("cred");
    let arvore = document.getElementById("arvore");
    let gasto = document.getElementById("gasto");

    cred.innerHTML = String(data['cred'])+"R$";
    arvore.innerHTML = data['arvore'];
    gasto.innerHTML = data['gasto'];

    divRes.style.visibility = "visible"
};

function enviarDadosPessoa(){
    let formP = document.forms.calcule;
    let formPData = new FormData(formP);

    let dadosP = {
        "aviao": formPData.get("aviao"),
        "botija": formPData.get("botija"),
        "condicionado": formPData.get("condicionado"),
        "eletricidade": formPData.get("eletricidade"),
        "combs_mov": formPData.get("combs_mov"),
        "qtd_mov": formPData.get("qtd_mov"),
        "recicla": formPData.get("recicla")
    };

    $.ajax ({
        type: "POST",
        url: "/pessoa",
        data: JSON.stringify(dadosP),
        contentType: "application/json",
        success: function(resp){
            resPessoa(resp);
        }
    });
};

function resPessoa(data){
    let divRes = document.getElementById("results");
    let cred = document.getElementById("cred");
    let arvore = document.getElementById("arvore");
    let gasto = document.getElementById("gasto");
    let gasto2 = document.getElementById("gasto2");

    cred.innerHTML = String(data['cred'])+"R$";
    arvore.innerHTML = data['arvore'];
    gasto.innerHTML = data['gasto'];
    gasto2.innerHTML = data['gasto'];

    divRes.style.visibility = "visible"
};


function adicionar(){
    const pai = document.getElementById("incluir");
    const div = document.createElement("div");
    div.classList = "scope1";
    const selectElements = ["acetileno", "alcatrão", "asfaltos","carvão_metalúrgico","coque_petroleo","etano","gas_refinaria","gas_natural_Seco","gas_natural_umido","gas_aut_pura","gas_aviao","Liq_gas_natural","lubrificantes","nafta","oleo_diesel","oleo_combustivel","oleol_residual","petroloe_bruto","querosene_aviação","res_industriais","etanol","biodiesel_b100","biogas","carvão_vegetal","lenha","residuos"];
    const selectNames = ["Acetileno","Alcatrão","Asfaltos","Carvão metalúrgico","Coque petroleo","Etano","Gás refinaria","Gás natural seco","Gás natural úmido","Gás aut pura","Gás avião","Liq gás natural","Lubrificantes","Nafta","Oleo diesel","Oleo combustivel","Oleo residual","Petróleo bruto","Querosene aviação","Resíduos industriais","Etanol","Biodiesel B100","Biogás","Carvão vegetal","Lenha","Resíduos"];

    const lista = document.createElement("select");
    lista.required = "required";
    lista.name = "tipo_combustivel";
    

    for(var i = 0; i < selectElements.length;i++){
        var option = document.createElement("option");
        option.value = selectElements[i];
        option.text = selectNames[i];
        lista.appendChild(option);
    }

    const qtd = document.createElement("input");
    qtd.type = "number";
    qtd.name = "qtd_combs"; 
    qtd.step=".01";
    qtd.min="0"; 
    qtd.required="required";

    const del = document.createElement("button");
    del.type = "button";
    del.innerHTML = "Delete";
    del.classList = "dlt_btn"
    del.onclick = function excluir(){
        this.parentNode.remove();
    }

    const lbl1 = document.createElement("label");
    const lbl2 = document.createElement("label");

    lbl1.for = "tipo_combustivel";
    lbl1.innerHTML = "Tipo de combustivel";
    lbl2.for = "qtd_combs";
    lbl2.innerHTML = "Quantidade consumida";

    div.appendChild(lbl1);
    div.appendChild(lista);
    div.appendChild(document.createElement("br"));
    div.appendChild(lbl2);
    div.appendChild(qtd);
    div.appendChild(document.createElement("br"));
    div.appendChild(del);
    pai.appendChild(div);
}

function adicionarMovel(){
    const pai = document.getElementById("incluirMovel");
    const div = document.createElement("div");
    div.classList = "scope1";
    const selectElements = ["gas_aut_com", "etanol", "biodiesel_b100","glp","gnv","diesel"];
    const selectNames = ["Gasolina automotiva (comercial)","Etanol","Biodiesel B100","Gás Liquefeito de Petróleo","Gás Natural Veicular","Óleo Diesel (comercial)"]

    const lista = document.createElement("select");
    lista.required = "required";
    lista.name = "combs_mov";
    

    for(var i = 0; i < selectElements.length;i++){
        var option = document.createElement("option");
        option.value = selectElements[i];
        option.text = selectNames[i];
        lista.appendChild(option);
    }

    const qtd = document.createElement("input");
    qtd.type = "number";
    qtd.name = "qtd_mov"; 
    qtd.step=".01";
    qtd.min="0"; 
    qtd.required="required";

    const del = document.createElement("button");
    del.type = "button";
    del.innerHTML = "Delete";
    del.classList = "dlt_btn"
    del.onclick = function excluir(){
        this.parentNode.remove();
    }

    const lbl1 = document.createElement("label");
    const lbl2 = document.createElement("label");

    lbl1.for = "combs_mov";
    lbl1.innerHTML = "Tipo de combustivel";
    lbl2.for = "qtd_mov";
    lbl2.innerHTML = "Quantidade consumida";

    div.appendChild(lbl1);
    div.appendChild(lista);
    div.appendChild(document.createElement("br"));
    div.appendChild(lbl2);
    div.appendChild(qtd);
    div.appendChild(document.createElement("br"));
    div.appendChild(del);
    pai.appendChild(div);
}

