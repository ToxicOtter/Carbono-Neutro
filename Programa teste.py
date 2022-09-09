nome_idade = [] #criação da lista que manterá os dados das pessoas cadastradas

def cadastro():
    #função que cria uma nova lista, a qual vai receber inicialmente os dados das pessoas cadastradas pelo usuário
    #retorna a lista preenchida com os dados

    lista_sup = []
    print("--------------------------------------------------------------------------")
    lista_sup.append(str.capitalize(input("Insira o primeiro nome da pessoa: ")))
    lista_sup.append(str.capitalize(input("Insira o sobrenome da pessoa: ")))
    lista_sup.append(int(input("Insira a idade da pessoa: ")))
    print("--------------------------------------------------------------------------")
    return lista_sup

#exibição visual para o usuário
print("--------------------------------------------------------------------------")
print("                          FREE CARBONO                                  ")
print("--------------------------------------------------------------------------")

#input que recebe a escolha do usuário, seja particular ou empresarial
escolha = str.lower(input("Voce gostaria de fazer o calculo do carbono neutro particular(P) ou empresarial(E)? P/E "))

#laço de repetição que verifica, por meio de um case, se o usário digitou um valor válido ou não
#caso seja um dos valores válidos, realiza o processo para adicionar os dados das pessoas na lista 
#caso não seja válido, o laço repete até que a variável escolha receba um valor permitido
while True:
    match escolha:
        case "p":
            nome_idade.append(cadastro())
            print(nome_idade)
            break
        case "e":
            print("--------------------------------------------------------------------------")
            numPessoas = int(input("Quantas pessoas a empresa possui? "))
            for i in range(0, numPessoas):
                nome_idade.append(cadastro())
                print(nome_idade)
            break
        case _:
            escolha = str.lower(input("Opção inválida, digite um valor válido (P/E): "))


"""
if(escolha == "p"):
    cadastro()
    print(nome_idade)

elif(escolha == "e"):
    print("--------------------------------------------------------------------------")
    numPessoas=int(input("Quantas pessoas a empresa possui? "))
    for i in range(0, numPessoas):
        nome_idade.append(cadastro())
        print(nome_idade)
"""