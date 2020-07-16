# função que mostra o help
def manual():
    import time
    while True:
        print('\033[1;46m=-'*30,end='\033[m')
        print("\n\033[1;46m                SISTEMA DE AJUDA DO PYTHON                  \033[m")
        print('\033[1;46m=-'*30,end='\033[m')
        print('\n')
        msg = input("Digite uma função ou uma biblioteca > ")
        if msg.upper() == 'FIM':
            print('\033[1;105m=-' * 30, end='\033[m')
            print("\n\033[1;105m                  ATE LOGO                      \033[m")
            print('\033[1;105m=-' * 30, end='\033[m')
            break
        print('\033[1;102m=-'*30,end='\033[m')
        print(f"\n\033[1;102m                Acessando o manual do {msg:<22}\033[m")
        print('\033[1;102m=-'*30,end='\033[m')
        print('\n')
        time.sleep(1.6)
        print('\033[;7m')
        help(msg)
        print('\033[m')




print(f"\033[;1m{'Desafio 106 - Programa que mostra os manuais disponiveis no help':*^70}\033[m")

manual()