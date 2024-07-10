from pokemon import *
from pessoas import *
import pickle

def salvar_jogo(player):
    try:
        with open('database.db', 'wb') as arquivo:
            pickle.dump(player, arquivo)
            print('O jogo foi salvo')
    except:
        print('Erro ao salvar o jogo')

def carregar_jogo():
    try:
        with open('database.db', 'rb') as arquivo:
            player = pickle.load(arquivo)
            print('Load feito com sucesso')
            return player 
    except Exception as Error:
        print('Save não encontrado')
    
if __name__ == "__main__":
    print('-------------------------------------------')
    print('Bem_vindo ao game Pokemon RPG de terminal')
    print('-------------------------------------------')

    player = carregar_jogo()

    if not player:
        nome = input('Olá, qual é o seu nome? ')
        player = Player(nome)
    
        print('\nOlá {}, esse é um mundo habitado por pokemons, a partir de agora sua missão é se tornar um mesmtre dos pokemon!'.format(player))
        print('Capture o máximo de pokemons que conseguir e lute com seus inimigos')
        player.mostrar_dinheiro()

        if player.pokemons:
            print('Já vi que você tem alguns pokemons')
            player.mostrar_pokemon()
        else:
            print('Você não tem nenhum pokemon, portanto precisa escolher um!')
            player.escolha_pokemon_inicial()

        print('Você devera derrotar Gary, seu inimigo!')
        gary = Inimigo(pokemons=[PokemonAgua('squirtle', level=1), ], nome='Gary') 
        player.batalha(gary)

        salvar_jogo(player)

    while True:
        print('-------------------------------------------')
        print('O que deseja fazer? ')
        print('1- Explorar o mundão a fora')
        print('2- Lutar com inimigo')
        print('3- Ver Pokeagenda')
        print('0- Sair do jogo')
        escolha = input('Sua escolha: ')

        if escolha == '0':
            print('Fechando o jogo...')
            break
        elif escolha == '1':
            player.explorar()
            salvar_jogo(player)
        elif escolha == '2':
            inimigo_aleatorio = Inimigo()
            player.batalha(inimigo_aleatorio)
            salvar_jogo(player)
        elif escolha == '3':
            player.mostrar_pokemon()
        else:
            print('Escolha inválida')