'''
Exercícios:
https://www.dropbox.com/scl/fi/4e7dz3v3f284jp9z1pm93/Lista-de-Exerc-cios-III-Python-para-Zumbis.pdf?rlkey=vw30r9kt82ulmtgcw69ab8fst&e=1&dl=0
'''

def l3_ex1():
    nota = float(input('Digite uma nota: '))
    while nota < 0 or nota > 10:
        nota = float(input('A nota deve ser um valor entre 0 e 10!\n Tente novamente: '))
    print("\num valor válido!")
    
def l3_ex2():
    nome = input('Digide seu nome: ')
    senha = input('Digite sua senha: ')
    erro = 'O nome não pode ser igual a senha'
    while senha == nome:
        senha = input('Erro! {erro},\nEscolha outra senha: ')
    print('Tudo certo!')
    
def l3_ex3():
    a = 80000
    b = 200000
    ano = 0
    while a < b:
        a = a + (a * 0.03)
        b = b + (b * 0.015)
        ano += 1
    print(f'Demoraria {ano} anos para a população da cidade A ultrapassar a da B')

def l3_ex4():
    ord = int(input('Escolha uma ordem: '))
    a, b = 1, 1
    for num in range(ord-2):
        a, b = b , a+b
    print(f'O {ord}º termo da sequência de Fibonacci é {b}')

def l3_ex5():
    a, b = map(int, input('Digite 2 números inteiros com espaço entre eles: ').split())
    while a % b != 0:
        a, b = b, a % b
    print(f'O MDC entre eles é {b}')
