# Função que retorna um fatorial, 'num' = valor desejado e 'show' = Mostra ou não os valores
def fatorial (num = 1 , show = False):
    # Pequenas informações sobre a função
    '''
    CALCULA O FATORIAL DE UM NUMERO
    :param num: É o valor para o qual se calcula o fatorial
    :param show: True para printar os calculos e false para retornar o valor somente
    :return: O resultado do fatorial
    '''
    # inicia-se com um para poder multiplicar com os demais numeros fatoriais
    numero = 1
    # condicional para saber se mostra ou não os calculos
    if show:
        # loop para printar na tela os valores e realizar os calculos
        for a in range (num, 1, -1):
            print(f'{a} x ',end='')
            # calculo do fatorial.
            numero *= a
        print(f"1 = ",end='')
        # retorna o valor calculado
        return numero
    # caso o usuario não queira mostrar os calculos
    else:
        for a in range (num , 1, -1):
            numero *= a
        return numero

# Programa principal
print(f"\033[;1m{'Desafio 102 - Fatorial com opção de mostrar calculos':*^70}\033[m")

print(fatorial(5))
help(fatorial)