from Veiculo import Veiculo
#BD em memória
listaVeiculos = []

def cadastrar():
    print("Digite a marca:")
    marca = input()
    print("Digite o modelo:")
    modelo = input()
    print("Digite placa:")
    placa = input()
    veiculo = Veiculo()
    listaVeiculos.append([marca, modelo, placa]) #[] para deixar as infos em uma linha, tbm criando uma lista, uma lista q coloco em outra lista, matriz unidimensional aqui temos uma lista dentro de outra lista[0][1] linha e coluna

def listar():
    if len(listaVeiculos) == 0:
        print("Não existem veículos cadastrados")
    else:
        i = 1
        for veiculo in listaVeiculos:
            print(f"Veículo: {i}")
            print(f"- Marca: {veiculo[0]}")
            print(f" - Modelo: {veiculo[1]}")
            print(f" - Placa: {veiculo[2]}")
            i+=1


def excluir():
    listar()
    print("Digite a placa que deseja excluir") #a única que não repete
    placa=input()
    encontrou = False
    for veiculo in listaVeiculos:
        if veiculo[2] == placa:
            listaVeiculos.remove(veiculo)
            encontrou = True
            break
    if  encontrou:
        print("Veículo excluido")
    else:
        print("Veículo não encontrado")


while True:
    print("Escolha uma das opções:")
    print("1 - Cadastrar Veículo")
    print("2 - Listar Veículos")
    print("3 - Excluir Veículos")
    print("0 - SAIR")
    opcao = input()
    try:
        opcao = int(opcao)
    except:
        print("Opção Inválida")

    if opcao == 1:
       cadastrar()
        #cadastro
    elif opcao == 2:
       listar()
        #Listar
        
    elif opcao == 3:
        excluir()

    elif opcao == 0:
        break
    else:
        print("Opção Inválida")


