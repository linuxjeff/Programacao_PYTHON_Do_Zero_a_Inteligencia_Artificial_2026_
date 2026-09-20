class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Olá, o meu nome é {self.nome} e tenho {self.idade} idade.')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo

    def trabalhar(self):
        print(f'Olá, meu nome é {self.nome} e trabalho no cargo {self.cargo}.')



class Cliente(Pessoa):
    def __init__(self, nome, idade, saldo):
        super().__init__(nome, idade)
        self.saldo = saldo
    def comprar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Olá, {self.nome}. A sua compra de {valor} foi aprovada. Seu novo saldo é de: R${self.saldo}')
        else:
            print(f'Olá, {self.nome}.  A sua compra de {valor} foi reprovada. Saldo insuficiente')

f1 = Funcionario('Maria', 38, 'Gerente de contas')
f1.apresentar()
f1.trabalhar()

c1 = Cliente('Artur', 16, 200)
c1.apresentar()
c1.comprar(200.35)