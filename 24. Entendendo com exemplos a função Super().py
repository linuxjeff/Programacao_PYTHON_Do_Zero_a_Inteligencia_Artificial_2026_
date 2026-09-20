#Sistema de Escola

class Escola:
    def __init__(self, nome, idade, estado):
        self.nome = nome
        self.idade = idade
        self.estado = estado

    def Apresentar(self):
        print(f'Meu nome é {self.nome}.')

    def Estado(self):
        print(f'Esta {self.estado}.')


class Aluno(Escola):
    def __init__(self, nome, idade, ano, estado):
        super().__init__(nome, idade, estado)
        self.ano = ano

    def Apresentar(self):
        super().Apresentar()
        print(f'Eu sou um aluno da escola.')

    def Estado(self):
        print(f'O Aluno {self.nome}')
        super().Estado()


class Professor(Escola):
    def __init__(self, nome, idade,  materia, estado):
        super().__init__(nome, idade, estado)
        self.materia = materia

    def Apresentar(self):
        super().Apresentar()
        print(f'Eu sou um proffesor da escola.')

    def Estado(self):
        print(f'O Proffesor {self.nome}')
        super().Estado()

class Assistente(Escola):
    def __init__(self, nome, idade,  bloco, estado):
        super().__init__(nome, idade, estado)
        self.bloco = bloco

    def Apresentar(self):
        super().Apresentar()
        print(f'Eu sou um(a) assistente da escola.')

    def Estado(self):
        print(f'O(A) Assistente {self.nome}')
        super().Estado()

a1 = Aluno('Marcos', 12, 8, 'Ativo')
p1 = Professor('Roberto', 34, 'Geometria', 'Ativo')
aas1 = Assistente('Ana Maria', 29, 'Bloco C', 'Inativo')

p1.Estado()
aas1.Estado()
aas1.Estado()
