class Carro:
    def __init__(self, modelo):
        self.modelo = modelo

class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

# Associação Simples
carro1 = Carro("Sedan")
motor1 = Motor("V8")
carro1.motor = motor1  # Carro está associado a um Motor

# Agregação
class Garagem:
    def __init__(self):
        self.carros = []

garagem1 = Garagem()
garagem1.carros.append(carro1)  # Garagem contém carros, mas eles podem existir independentemente

# Composição
class CarroComposto:
    def __init__(self, modelo, tipo_motor):
        self.carro = Carro(modelo)
        self.motor = Motor(tipo_motor)

carro_composto1 = CarroComposto("Hatchback", "Elétrico")
# Se carro_composto1 for destruído, também serão destruídos o Carro e o Motor associados a ele

# Herança (Exemplo básico)
class Veiculo:
    def __init__(self, marca):
        self.marca = marca

class CarroHeranca(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo

carro_heranca1 = CarroHeranca("Toyota", "Corolla")