"""Exercício de Orientação a Objetos com Herança, Polimorfismo e Encapsulamento
Neste exercício, você irá criar um sistema simples de gerenciamento de veículos, utilizando os conceitos de orientação a objetos, herança, polimorfismo e encapsulamento em Python. O sistema irá lidar com dois tipos de veículos: carros e motos.

Classe Base: Veiculo
Crie uma classe chamada Veiculo, que terá os seguintes atributos privados:

__marca: uma string que representa a marca do veículo.
__modelo: uma string que r

"""

# Classe Base: Veiculo
class Veiculo:
    def __init__(self, marca: str, modelo: str):
        self.__marca = marca
        self.__modelo = modelo

    # Métodos getters
    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo

    def descricao(self):
        return f"Marca: {self.__marca}, Modelo: {self.__modelo}"
    
# Classe Filha: Carro
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.__portas = portas

    def get_portas(self):
        return self.__portas

    def descricao(self):
        return f"Carro - {self.get_marca()}, Modelo: {self.get_modelo()}, Portas: {self.__portas}"
    
# Classe Filha: Moto
class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.__cilindradas = cilindradas

    def descricao(self):
        return f"Moto - {self.get_marca()}, Modelo: {self.get_modelo()}, Cilindradas: {self.__cilindradas}"

# Programa principal
if __name__ == "__main__":
    carro = Carro("Toyota", "Corolla", 4)
    moto = Moto("Honda", "CBR500R", 500)

    veiculos = [carro, moto]

for veiculo in veiculos:
     print(veiculo.descricao())


