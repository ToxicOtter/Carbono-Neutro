nome_idade = []

def cadastro ():
    lista_sup=[]
    print("--------------------------------------------------------------------------")
    lista_sup.append(str.capitalize(input("Insira o primeiro nome da pessoa: ")))
    lista_sup.append(str.capitalize(input("Insira o sobrenome da pessoa: ")))
    lista_sup.append(int(input("Insira a idade da pessoa: ")))
    print("--------------------------------------------------------------------------")
    return lista_sup

print("--------------------------------------------------------------------------")
print("                          FREE CARBONO                                  ")
print("--------------------------------------------------------------------------")

escolha=str.lower(input("Voce gostaria de fazer o calculo do carbono neutro particular(P) ou empresarial(E)? P/E "))
if(escolha=="p"):
    cadastro()
    print(nome_idade)

elif(escolha=="e"):
    print("--------------------------------------------------------------------------")
    numPessoas=int(input("Quantas pessoas a empresa possui? "))
    for i in range (0,numPessoas):
        nome_idade.append(cadastro())
        print(nome_idade)
else:
    print("Escolha uma opção válida!!!")






