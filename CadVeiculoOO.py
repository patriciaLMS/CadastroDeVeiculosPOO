from Caminhao import Caminhao
from Carro import Carro
from Moto import Moto
from Veiculo import Veiculo
#BD em memória
listaVeiculos = [
    Carro("Hyundai", "HB20", "ABC", 2023, 4),
    Moto("Yamaha", "Lander", "DEF", 2008, 250)
]

def cadastrar():
    print("Qual o tipo de veículo: (1) Carro - (2) Moto - (3) Caminhão")
    tipo = input()
    print("Digite a marca:")
    marca = input()
    print("Digite o modelo:")
    modelo = input()
    print("Digite placa:")
    placa = input()
    print("Digite o Ano:")
    ano = input()

    if tipo == "1":
        nPortas = input("Digite o número de portas: ")
        veiculoAdd = Carro(marca, modelo ,placa, ano, nPortas)
    elif tipo == "2":
        cilindradas = input("Digite as cilindradas: ")
        veiculoAdd = Moto(marca, modelo, placa, ano, cilindradas)
    elif tipo == "3":
        nPortas = input("Digite o número de portas: ")
        capacidade = input("Digite a capacidade de carga do caminhão: ")
        veiculoAdd = Caminhao(marca, modelo ,placa, ano, nPortas,capacidade)


    listaVeiculos.append(veiculoAdd) #lista de objetos
    
    
    
    
     #[] para deixar as infos em uma linha, tbm criando uma lista, uma lista q coloco em outra lista, matriz unidimensional aqui temos uma lista dentro de outra lista[0][1] linha e coluna

def listar():
    if len(listaVeiculos) == 0:
        print("Não existem veículos cadastrados")
    else:
        i = 1
        for veiculo in listaVeiculos:
            print(f"Veículo: {i}")
            print(f"- {veiculo}")
            
        
            i+=1


def excluir():
    listar()
    print("Digite a placa que deseja excluir") #a única que não repete
    placa=input()
    encontrou = False
    for veiculo in listaVeiculos:
        if veiculo.get_placa() == placa:
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


