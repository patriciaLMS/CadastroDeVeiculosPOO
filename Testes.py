from Moto import Moto
from Veiculo import Veiculo
# Instanciando a classe Moto
falcon = Moto("Honda", "Falcon NX4", "abc",2005,400)   #a classe Moto herda tudo da classe Veículo
# Exibir uma informação na tela => Vai imprimir o RETORNO do método "__str__()"
print(falcon.__str__())  # invoca str da Moto pq foi sobreescrito

# Instanciando a classe Veiculo=====================

cerato = Veiculo("Kia", "Cerato","IRL",2011)

print(cerato.__str__()) # o q define qual método vai ser invocado é classe




# Abaixo estou instanciando um objeto
#da Classe Veiculo #o q o construtor está pedindo #o self é o python que injeta
meuUno = Veiculo("Fiat", "Uno com Escada", "ABC-1234",2000)
print(meuUno.get_marca) 
print(meuUno.calcularTempoUso())
meuUno.__ano = 2010
print(meuUno.calcularTempoUso())
teuFusca = Veiculo("Volks", "Fusca do Itamar", "DEF-", 1995)


#print(meuUno.calcularTempoUso())
#print(teuFusca.calcularTempoUso())

#print("")