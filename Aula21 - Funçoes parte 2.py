# Função que tem um valor opicional
# O 'c' é opcional e pode receber qualquer valor.
def somar (a, b, c=0):
    s = a + b + c
    print(f"A Soma dos valores é {s}")
somar(4,6,55)

# Variavel global e local
def test(b):
    b = 2
    print(f"Variavel global: {a} e local {b}")
a = 5
test(a)

# Variavel global dentro de uma função
def test2(b):
    global x
    x = 8
    b += 2
    c = 3
    print(f"x = {x} b = {b} e c = {c}")

x = 10
test2(x)
print(f'x = {x}')

# Funçao Return
def somatoria (a=0,b=0,c=0):
    return (a+b+c)

soma = somatoria(9,2,5)
print(soma)
soma = somatoria(2,1)
print(soma)

# Fatorial
def fatorial (num=1):
    f = 1
    for c in range(num, 0 ,-1 ):
        f *= c
    return f

print(fatorial(int(input("Digite o numero que quer fatorial: "))))
print(fatorial())
