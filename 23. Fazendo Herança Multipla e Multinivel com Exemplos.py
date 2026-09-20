# Herança multipla e herança de multinivel.

# Classe avô.

class Animal:
    def __init__(self, nome):
        self.nome = nome


# classe Pai
class Predador(Animal):
    def cacando(self):
        print(f"O Animal {self.nome} esta caçando")

class Presa(Animal):
    def fungindo(self):
        print(f'O animal {self.nome} esta Fogindo')

# Classes filhos
class Coelho(Presa):
    pass

class Tigre(Predador):
    pass
class Golfinho(Predador, Presa):
    pass

coelho1 = Coelho('Coelho')
tigre1 = Tigre('Tigre')
golfinho1 = Golfinho('Golfinho')

coelho1.fungindo()
tigre1.cacando()
golfinho1.fungindo()
