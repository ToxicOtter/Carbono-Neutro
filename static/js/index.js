const res = document.getElementsByClassName("results");


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

