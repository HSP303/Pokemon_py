from pokemon import *
import random

NOMES = ['Roberto', 'Lorival', 'Robersom', 'Abdiel', 'Gustavo', 'Dizidério', 'James', 'Juninho', 'Vinicius',
         'Cabelo', 'Cebinho', 'Marcha Ré'
         ]

POKEMONS = [
        PokemonFogo('Charmander'),
        PokemonFogo('Flarion'),
        PokemonFogo('Charmilion'),
        PokemonEletrico('Pikachu'),
        PokemonEletrico('Raichu'),
        PokemonAgua('Squirtle'),
        PokemonAgua('Magicarp')
        
]

class Pessoa:
    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)
        
        self.pokemons = pokemons

        self.dinheiro = dinheiro

    def __str__(self):
        return self.nome
    
    def mostrar_pokemon(self):
        print('Pokemons de {}:'.format(self.nome))
        for i, pokemon in enumerate(self.pokemons):
            print('{} - {}'.format((i + 1), pokemon))

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print('{} escolheu {}'.format(self, pokemon_escolhido))
            return pokemon_escolhido

        else:
            print('Esse player não possui pokemons')

    def mostrar_dinheiro(self):
        print('Você possui ${}'.format(self.dinheiro))

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print('Você ganhou ${}'.format(quantidade))
        self.mostrar_dinheiro()
    
    def batalha(self, pessoa):
        print('{} iniciou uma batalha com {}'.format(self, pessoa))

        pessoa.mostrar_pokemon()
        pokemon_inimigo = pessoa.escolher_pokemon()

        pokemon = self.escolher_pokemon()

        if pokemon and pokemon_inimigo:
            while True:
                vitoria = pokemon.atacou(pokemon_inimigo)
                if vitoria:
                    print('{} ganhou a batalha'.format(self))
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break
                vitoria_inimiga = pokemon_inimigo.atacou(pokemon)
                if vitoria_inimiga:
                    print('{} ganhou a batalha'.format(pessoa))
                    break



        else:
            print('Não há pokemons suficientes na batalha')


class Player(Pessoa):
    tipo = 'player'
    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print('{} capturou {}'.format(self.nome, pokemon))

    def escolha_pokemon_inicial(player):
        print('Olá {}, agora você deve escolher o pokemon que lhe acompanhara nesta jornada!'.format(player))
    
        pikachu = PokemonEletrico('Pikachu', level=1)
        charmander = PokemonFogo('charmander', level=1)
        squirtle = PokemonAgua('Squirtle', level=1)

        print('Você possui as seguintes escolhas: ')
        print('1- ', pikachu)
        print('2- ', charmander)
        print('3- ', squirtle)

        while True:
            resposta = input('Digite o número do pokemon que você quer: ')
    
            if resposta == '1':
                player.capturar(pikachu)
                break 
            elif resposta == '2':
                player. capturar(charmander)
                break
            elif resposta == '3':
                player.capturar(squirtle)
                break
            else:
                print('Escolha inválida')
    
    def escolher_pokemon(self):
        self.mostrar_pokemon()

        while True:
            escolha = input('Digite o número do pokemon que irá batalhar: ')
            
            if self.pokemons:
                try:
                    escolha = int(escolha)
                    escolha -= 1
                    pokemon_escolhido = self.pokemons[escolha]
                    print('{} eu escolho você!!!'.format(pokemon_escolhido))
                    return pokemon_escolhido
                except:      
                    print('ERRO: escolha inválida')
            else:
                print('Esse player não possui pokemons')

    def explorar(self):
        if random.random() <= 0.6:
            pokemon = random.choice(POKEMONS)
            print('Um pokemon selvagem apareceu: {}'.format(pokemon))
            
            escolha = input('Deseja capturar pokemon? (s/n)\n')
            if escolha == 's' :
                if random.random() >= 0.5:
                    self.capturar(pokemon)
                else:
                    print('O pokemon fugiu')
            else:
                print('Ok, boa viagem')
        else:
            print('Essa exploração não deu em nada')

class Inimigo(Pessoa):
    tipo = 'inimigo'

    def __init__ (self, nome=None, pokemons = None):
        
        if not pokemons:
            pokemons_aleatorios = []
            for i in range(random.randint(1 , 6)):
                pokemons_aleatorios.append(random.choice(POKEMONS))

            super().__init__(nome=nome, pokemons = pokemons_aleatorios)
        else:
            super().__init__(nome=nome, pokemons = pokemons)

    

        


    