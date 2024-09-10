from Veiculo import Veiculo
class Caminhao(Veiculo):
    def __init__(self,marca,modelo,placa,ano,n_portas,capacidade):
        super().__init__(marca,modelo,placa,ano)
        self.__capacidade = capacidade
    def __str__(self):
        retornar = super().__str__()
        return f''' {retornar}
- Capacidade de Carga: {self.__capacidade}'''