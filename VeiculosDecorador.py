

# Classe Base: Veiculo
class Veiculo:
    def __init__(self, marca: str, modelo: str):
        self.__marca = marca
        self.__modelo = modelo

    def __str__(self):
        return self.descricao()
    
    # Métodos getters
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, nova_marca):
        self.__marca = nova_marca

    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, novo_modelo):
        self.__modelo = novo_modelo

    def descricao(self):
        return f"Marca: {self.__marca}, Modelo: {self.__modelo}"
    
# Classe Filha: Carro
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.__portas = portas

    def descricao(self):
        return f"Carro - {self.marca}, Modelo: {self.modelo}, Portas: {self.__portas}"
    
# Classe Filha: Moto
class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.__cilindradas = cilindradas

    def descricao(self):
        return f"Moto - {self.marca}, Modelo: {self.modelo}, Cilindradas: {self.__cilindradas}"

# Programa principal
if __name__ == "__main__":
    carro = Carro("Toyota", "Corolla", 4)
    moto = Moto("Honda", "CBR500R", 500)

    veiculos = [carro, moto]

for veiculo in veiculos:
     print(veiculo.descricao())


