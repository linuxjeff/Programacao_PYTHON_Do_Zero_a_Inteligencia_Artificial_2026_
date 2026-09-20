class Casa:
    def __init__(self, cor, quartos, banheiros):
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros

    def mostrar_cor(self):
        print(f'A conda casa é {self.cor}')

    def mostrar_quartos(self):
        print(f'Esta casa tem {self.quartos} quarto(s)')

    def mostrar_banheiros(self):
        print(f'Esta casa tem {self.banheiros} banheiro(s)')

    def adicionar_quarto(self):
        self.quartos += 1
        print(f'Estacasa tem {self.quartos} quarto(s)')

    def pintar_casa(self, nova_cor):
        print(f'Pintando a casa de {self.cor} para {nova_cor}')

casa1 = Casa('Azul', 4, 3)
casa2 = Casa('Amarela', 6, 4)

print('\nCasa 1: ')
casa1.mostrar_cor()
casa1.mostrar_quartos()
casa1.mostrar_banheiros()
casa1.adicionar_quarto()
casa1.pintar_casa('Vermelho')
print('\nCasa 2: ')
casa2.mostrar_cor()
casa2.mostrar_quartos()
casa2.mostrar_banheiros()
casa2.adicionar_quarto()