class Veiculo:
    #__init__ => é o método construtor, invocado quando instanciar um objt, sempre invocado quando inicia , pegar o modelo bluprint e constrói o objeto concreto
    def __init__(self, marca, modelo, placa, ano):
        self.__marca = marca    #esses
        self.__modelo = modelo  #são
        self.__placa = placa    #os
        self.__ano = ano        #atributos

    def get_marca(self):
        return self.__marca
    def set_marca(self, marca):
        if marca != "Pegeout":
            self.__marca = marca.upper()

    def get_modelo(self):
        return self.__modelo
    def set_modelo(self, modelo):
        self.__modelo = modelo
    
    def get_placa(self):
        return self.__placa
    def set_placa(self, placa):
        self.__placa = placa

    def get_ano(self):
        return self.__ano
    def set_ano(self, ano):
        if ano < 1900:   # posso criar regras
            self.__ano = ano

        #Método de instância, está relacionado a cada objeto
    def calcularTempoUso(self):#----> uma função, ou seja, método
        return 2024 - self.__ano
    
    def __str__(self): # self é o objeto q está invocando o método
        return f'''Marca: {self.__marca}
- Modelo: {self.__modelo}
- Placa: {self.__placa}
- Ano: {self.__ano} '''


    

