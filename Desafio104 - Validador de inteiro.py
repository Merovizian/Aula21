# Programa semelhante a input porém só aceita inteiros.
def leiaint(msg='',i=-float('inf'),f=float('inf')):
    '''
    Programa que lê um valor pelo usuario e retorna inteiro, caso o usuário não digite nenhum inteiro será mostrado uma mensagem de erro.
    :param msg: Mensagem que o usuario final vai ler ex:"digite um número: "
    :param i: inicio do intervalo
    :param f: final do intervalo
    :return: o inteiro dentro desse intervalo
    '''
    # verifica se os intervalos são possiveis, se não forem, inverte-se
    if i>f:
        aux = i
        i = f
        f = aux
    # Loop para checagem se é inteiro
    while True:
        # Faz a chamada da função input com a mensagem colocada na função leiaint
        numero = input(msg)
        # Verifica se o usuario digitou algo
        if len(numero) != 0:
            # Verifica se o que foi digitado é numero negativo
            if numero[0] == '-':
                # se for negativo , este if ignora o sinal e verifica se o restante é numerico
                if numero[1:].isnumeric():
                    # se for numerico, transforma a string em numero
                    numero = int(numero)
                    # verifica se o numero está no intervalo dado
                    if numero < i or numero > f:
                        print(f"\033[1;33mError, Digite um valor entre {i} e {f}\033[m")
                    else:
                        return (numero)
                # se não for numérico.
                else:
                    print("\033[1;31mError, Digite um valor inteiro válido!\033[m")
            # Se o numero não for negativo ele parte para verificação de numérico automaticamente e repete os passos
            else:
                if numero.isnumeric():
                    numero = int(numero)
                    if numero < i or numero > f:
                        print(f"\033[1;33mError, Digite um valor entre {i} e {f}\033[m")
                    else:
                        return numero
                else:
                    print("\033[1;31mError, Digite um valor inteiro válido!\033[m")
        # Se o usuário não digitou nada mostra erro.
        else:
            print("\033[1;31mError, Digite um valor inteiro válido!\033[m")


print(f"\033[;1m{'Desafio 104 - Função input verificadora de inteiros':*^70}\033[m")

while True:
    i = leiaint("Informe o intervalo inicial: ")
    f = leiaint("Informe o intervalo final: ")
    x = leiaint('Informe o valor de x: ',i,f)
    print(x)
