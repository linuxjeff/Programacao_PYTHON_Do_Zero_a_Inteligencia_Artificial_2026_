class Animal:
    def __init__(self, nome, cor, especie):
        self.nome = nome
        self.cor = cor
        self.especie = especie

    def apresentar(self):
        print(f'Eu sou da especie {self.especie} e meu nome é {self.nome}.')

class Gato(Animal):
    def emitir_som(self):
        print(f'Miau!')
    def arrarar(self):
        print(f'O gato esta arranhando!')

class Cachorro(Animal):
    def emitir_som(self):
        print(f'Au Au!')

class Jabuti(Animal):
    def emitir_som(self):
        print(f'Track!')

gato1 = Gato('Pedro', 'Azul', 'Azul Russo')
gato1.apresentar()
gato1.emitir_som()
gato1.arrarar()

cachorro = Cachorro('Vitória Rebecca', 'Preto e Branco', 'SRD')
cachorro.apresentar()
cachorro.emitir_som()
cachorro2 = Cachorro('Benedito', 'Preto e Amarelo', 'SRD')
cachorro2.apresentar()

jabuti1 = Jabuti('Anselmo', 'Verde', 'Jabuti')
jabuti1.apresentar()
jabuti1.emitir_som()