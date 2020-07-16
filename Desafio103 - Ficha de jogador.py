# Escopo da função global
def ficha(jogador = "<Desconhecido>" , gols='0'):
    print(f"O jogador {jogador} fez {int(gols)} no campeonato")

# inicio função principal
print(f"\033[;1m{'Desafio 103 - Ficha jogador - gols':*^70}\033[m")
jogador = input("Informe o nome do jogador: ")
gols = input("Informe a quantidade de gols feitos: ")
# transforma o valor digitado em inteiro , caso não seja inteiro é transformado em inteiro 0
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
# verifica se digitado algum nome, caso não tenha sido, chama a função sem esse parametro
if len(jogador.strip()) == 0:
    ficha(gols=gols)
#     chama a função inteira se o nome tiver sido digitado.
else:
    ficha(jogador,gols)
