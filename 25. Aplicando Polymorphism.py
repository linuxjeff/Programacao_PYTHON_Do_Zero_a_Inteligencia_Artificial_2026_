# Polimorphism
class Guerreiro:
    def falar(self):
        print("Guerreiro")

class Mago:
    def falar(self):
        print("Mago")

class Arqueiro:
    def falar(self):
        print("Arqueiro")

# Objetos

persongem = [Guerreiro(), Mago(), Arqueiro()]

for persongem in persongem:
    persongem.falar()
# Ele mostrou um exemplo sem a eraça, mas já vimos que não é preciso somente
# tirando a classe Personagem do exemplo anterior.