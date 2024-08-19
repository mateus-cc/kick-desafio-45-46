import random

opcoes = ['pedra', 'papel', 'tesoura']
vitoriaJogador = 0
vitoriaComputador = 0
empate = 0

def escolhaComputador(): 
  computador = random.choice(opcoes)
  print(computador)
  return computador

def escolhaJogador():
  opcao = input('Você escolhe pedra, papel ou tesoura? ').lower()
  while opcao != 'pedra' and opcao != 'papel' and opcao != 'tesoura':
    opcao = input('Digite uma opção válida: ')
  print(opcao)
  return opcao 
      
opcaoComputador = escolhaComputador()
opcaoJogador = escolhaJogador()

if opcaoJogador == 'pedra' and opcaoComputador == 'tesoura' or opcaoJogador == 'papel' and opcaoComputador == 'pedra' or opcaoJogador == 'tesoura' and opcaoComputador == 'papel':
  print(f'O jogador ganhou pois {opcaoJogador} ganha de {opcaoComputador}')
  vitoriaJogador += 1
elif opcaoComputador == 'pedra' and opcaoJogador == 'tesoura' or opcaoComputador == 'papel' and opcaoJogador == 'pedra' or opcaoComputador == 'tesoura' and opcaoJogador == 'papel':
  print(f'O computador ganhou pois {opcaoJogador} ganha de {opcaoComputador}')
  vitoriaComputador += 1
else: 
  print('O jogo acabou empatado')
  empate += 1

def continuarJogo():
  decisao = input('Deseja jogar novamente? s/n ')   
  while True:
    if decisao != 's': 
      print('Jogo encerrado')
      break
    else:
      escolhaComputador()
      escolhaJogador()
      continuarJogo()

def placarGeral(): 
  print(f'O jogador teve {vitoriaJogador} vitórias')
  print(f'O computador teve {vitoriaComputador} vitórias')
  print(f'Um total de {empate} empates')
  if vitoriaJogador > vitoriaComputador:
    print(f'Parabéns Jogador, você é campeão!')
  elif vitoriaJogador < vitoriaComputador:
    print(f'Que pena, não foi dessa vez. O computador foi campeão')
  else: 
    print('O jogo acabou empatado')

continuarJogo()
placarGeral()
