# Importo uma função que retorna quandos anos uma pessoa tem a partir da dt do seu nascimento
from idade import ano


# função que pega o valor do ano da pessoa e verifica em qual faixa ele está
def voto(nascimento):
    if ano(nascimento) < 16:
        print(f"Com {ano(nascimento)} anos de idade o voto é proibido")
    elif ano(nascimento) < 18 or ano(nascimento) >= 65:
        print(f"Com {ano(nascimento)} anos de idade o voto é facultativo")
    else:
        print(f"Com {ano(nascimento)} anos de idade o voto é obrigatorio")


# MAIN - função principal
print(f"\033[;1m{'Desafio 101 - Direito a voto':*^70}\033[m")
# utilizando a função criada acima.
voto(input("Informe a data do seu nascimento[dd/mm/aaaa]: "))