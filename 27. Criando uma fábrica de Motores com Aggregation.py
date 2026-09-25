class Motor:
    def __init__(self, marca, potencia):
        self.marca = marca
        self.potencia = potencia

class Carro:
    def __init__(self):
        self.motores = []

    def adicionar(self, motor):
        self.motores.append(motor)

    def listar_motores(self):
        for motore in self.motores:
            print(f'Marca: {motore.marca} - Potência: {motore.potencia}')

# criando os motores (objtos).

motor_v6 = Motor('Ford', 300)
motor_v8 = Motor('Ferrari', 650)
motor_v12 = Motor('Lamborghini', 950)

#Criar o carro e adicionar o motor a ele.
carro = Carro()
carro.adicionar(motor_v6)
carro.adicionar(motor_v8)
carro.adicionar(motor_v12)

# Listar motores
carro.listar_motores()