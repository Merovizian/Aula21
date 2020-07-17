# Função para verificar notas
def notas (*num, sit = False):
    '''
    Função para adicionar notas a determinado aluno e saber sua situação
    :param num: lista com varios numeros
    :param sit: True printa a situação , False omite a situação
    :return: dicionario sobre a informação d eum aluno
    '''
    # iniciando algumas variáveis já em formato de dicionario
    notageral = dict()
    notageral['quantidade'] = len(num)
    notageral['maior'] = max(num)
    notageral['menor'] = min(num)
    notageral['media'] = sum(num)/len(num)

    if notageral['media'] < 5:
        situacao = 'Reprovado'
    elif notageral['media'] < 7:
        situacao = "Recuperação"
    else:
        situacao = 'Aprovado'

    if sit:
        notageral['situação'] = situacao
        return notageral
    else:
        return notageral

print(f"\033[;1m{'Desafio 105 - Função lê notas':*^70}\033[m")

print(notas(3.5,9,6.5,9,7,7))