class Carro:
    def __init__(self, cor, ano):
        self.cor = cor
        self.ano = ano
        self.ligado = False
        self.seta = None

    def informacoes(self):
        print(f'A cor do carro é {self.cor}.')
        print(f'O ano do carro é {self.ano}.')

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f'O carro foi ligado')
        else:
            print(f'O carro já estava ligado.')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f'O carro foi desligado.')
        else:
            print(f'O carro estava desligado.')

    def ligar_seta(self, direcao):
        self.seta = direcao
        if self.ligado:
            print(f'Seta ligada para {self.seta}.')
        else:
            print(f'É nescessario o carro esta ligado para ligar a seta {self.seta}.')


carro1 = Carro('preto', 2021)
carro1.informacoes()
carro1.ligar()
carro1.ligar_seta('Esquerda')