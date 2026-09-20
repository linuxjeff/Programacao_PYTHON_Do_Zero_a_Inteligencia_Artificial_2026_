class Pessoa():
    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
    def informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Cargo: {self.cargo}')

    def promover(self, novo_cargo):
        print(f'{self.nome} promovido a novo cargo de {novo_cargo}')
        self.cargo = novo_cargo

    def nova_idade(self, novo_idade):
        if novo_idade > self.idade:
            print(f'A nova idade é {novo_idade}')
            self.idade = novo_idade
        else:
            print(f'A idade é menor que a atual.')

colaborador1 = Pessoa('Ana', 36, 'Assistente Junior')

colaborador1.promover('Assistente Pleno')
colaborador1.nova_idade(37)
colaborador1.informacoes()
