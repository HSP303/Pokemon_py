import random

class Pokemon:
    def __init__(self, especie, level=None, nome=None):
        self.especie = especie

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)
        if nome :
            self.nome = nome
        else:
            self.nome = especie

        self.ataque = self.level * 5
        self.vida = self.level * 10

    def __str__(self):
        return '{} ({})'.format(self.nome, self.level)
    
    def atacou(self, pokemon):
        ataque_efetivo = int((self.ataque * random.random() * 1.5))
        pokemon.vida -= ataque_efetivo
        print('{} perdeu {} pontos de vida'.format(pokemon ,ataque_efetivo))

        if pokemon.vida <= 0:
            print('{} foi derrotado'.format(pokemon))
            return True
        else:
            return False

class PokemonEletrico(Pokemon):
    tipo = 'elétrico'
    
    def atacou(self, pokemon):
        print('{} lançou um ataque do trovão em {}'. format(self.nome, pokemon.nome ))
        return super().atacou(pokemon)

class PokemonFogo(Pokemon):
    tipo = 'fogo'
    def atacou(self, pokemon):
        print('{} lançou uma bola de fogo na cabeça de {}'. format(self.nome, pokemon.nome ))
        return super().atacou(pokemon)

class PokemonAgua(Pokemon):
    tipo = 'água'
    def atacou(self, pokemon):
        print("{} lançou um jato d'água em {}". format(self.nome, pokemon.nome ))
        return super().atacou(pokemon)

