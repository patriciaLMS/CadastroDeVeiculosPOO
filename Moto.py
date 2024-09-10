from Veiculo import Veiculo
 # quando queremos herdar de uma superclasse, classe mãe/pai
class Moto(Veiculo):
    def __init__(self,marca, modelo, placa, ano, cilindradas): #super init significa chamar o construtor da super classe
        super().__init__(marca, modelo, placa, ano)  #cilindradas não é passado para a superclasse pois lá na superclasse só tem esses, as cilindradas é específico da subclasse Moto
        self.__cilindradas = cilindradas
        # Sobreescrita do método __str__
    def __str__(self):
            # Armazeno o retorno na variável "retorno"
            retorno = super().__str__() # self é o objeto q está invocando o método, invovo o método __str__  SUPERCLASSE (Veiculo)
            # Retorno a concatenação do valor da variável
            # "retorno" com as "__cilindradas"
            return f'''{retorno}
- Cilindradas: {self.__cilindradas}'''
                
        
