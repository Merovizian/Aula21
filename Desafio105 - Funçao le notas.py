# Função para verificar notas
def notas (*num, sit = False):
    '''
    Função para adicionar notas a determinado aluno e saber sua situação
    :param num: lista com varios numeros
    :param sit: True printa a situação , False omite a situação
    :return: dicionario sobre a informação d eum aluno
    '''
    # iniciando algumas variáveis
    maior = 0
    soma = 0
    quantidade = 0
    situacao = ''
    # Loop que pecorre todos os numeros
    for a in num:
        # Definir o menor numero como sendo o primeiro
        if quantidade == 0:
            menor = a
        if a > maior:
            maior = a
        if a < menor:
            menor = a
        soma += a
        quantidade += 1
    media = (soma/quantidade)
    if media < 5:
        situacao = 'Reprovado'
    elif media < 7:
        situacao = "Recuperação"
    else:
        situacao = 'Aprovado'

    if sit:
        notageral = {'total': quantidade, 'maior': maior, 'menor': menor, 'média': media, 'situação': situacao }
        return notageral
    else:
        notageral = {'total': quantidade, 'maior': maior, 'menor': menor, 'média': media}
        return notageral

print(f"\033[;1m{'Desafio 105 - Função lê notas':*^70}\033[m")

print(notas(3.5,2,6.5,2,7,4,sit=True))