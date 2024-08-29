'''
Perguntas:
https://www.dropbox.com/scl/fi/prnewjtl2578n36abvula/Lista-de-Exerc-cios-II-Python-para-Zumbis.pdf?rlkey=j5z4x5kjmsefhmwnln1hnjzv5&e=4&dl=0
'''

def ex1():
    L1 = float(input('Insira o valor do PRIMEIRO lado: '))
    L2 = float(input('Insira o valor do SEGUNDO lado: '))
    L3 = float(input('Insira o valor do TERCEIRO lado: '))
    
    if L1+L2 > L3 and L1+L3 > L2 and L2+L3 > L1:
      print('O triangilo existe!')
      if L1 == L2 == L3:
        print('Se trata de um triangulo EQUILÁTERO')
      elif L1 == L2 or L2 == L3 or L1 == L3:
         print('Se trata de um triangulo ISÓSCELES')
      else:
               print('Se trata de um triângulo ESCALENO')
    else:
      print('O triangulo NÃO existe!')
    
    
    
def ex2():
    ano = int(input('Digite um ano: '))
    
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
      print('O ano informado é Bissexto!')
    else:
      print('O ano informado NÃO é Bissexto!')
    
    
    
def ex3():
    kg = float(input('Quantos kg de peixe: '))
    
    if kg > 50:
        print(f'Você excedeu o peso limite. Deverá pagar uma multa de R${(kg-50)*4}, para um excesso de {kg-50}kg')
    else:
        print('O peso está de acordo! Tenha um bom dia.')
    
    
    
def ex4():
    n1 = float(input('Digíte o Primeiro número: '))
    n2 = float(input('Digíte o Segundo número: '))
    n3 = float(input('Digíte o Terceiro número: '))
    
    if n1 >= n2 and n1 >= n3:
        print(f'\nO Número {n1:.0f} é o maior!')
    elif n2 >= n1 and n2 >= n3:
        print(f'O Número {n2:.0f} é o maior!')
    else:
        print(f'O Número {n3:.0f} é o maior!')
    
    
    
def ex5():
    n1 = float(input('Digíte o Primeiro número: '))
    n2 = float(input('Digíte o Segundo número: '))
    n3 = float(input('Digíte o Terceiro número: '))
    
    if n1 >= n2 and n1 >= n3:
        print(f'\nO Número {n1:.0f} é o maior!')
    elif n2 >= n1 and n2 >= n3:
        print(f'O Número {n2:.0f} é o maior!')
    else:
        print(f'O Número {n3:.0f} é o maior!')
    
    if n1 <= n2 and n1 <= n3:
        print(f'\nO Número {n1:.0f} é o menor!')
    elif n2 <= n1 and n2 <= n3:
        print(f'O Número {n2:.0f} é o menor!')
    else:
        print(f'O Número {n3:.0f} é o menor!')
    
    
    
def ex5_2()
    n1 = float(input('Digíte o Primeiro número: '))
    n2 = float(input('Digíte o Segundo número: '))
    n3 = float(input('Digíte o Terceiro número: '))
    
    maior = n1
    menor = n1
    
    if n2 >= n1 and n2 >= n3:
        maior = n2
    elif n2 <= n1 and n2 <= n3:
        menor = n2
    
    if n3 >= n1 and n3 >= n2:
        maior = n3
    elif n3 <= n1 and n3 <= n2:
        menor = n3
    
    print(f'\nO maior número é o {maior:.0f} e o menor número é o {menor:.0f}')
    
    
    
def ex6():
    qnt = float(input('Quanto você ganha por hora? '))
    hr = int(input('Quantas horas você trabalha por mês? '))
    
    sal = (qnt * hr)
    desc = sal - (11/100)*sal - (8/100)*sal - (5/100)*sal
    
    print(f'\nSeu salário bruto é de: R${sal}\n Descontos:\n -IR(11%) > R${(11/100)*sal}\n -INSS(8%) > R${(8/100)*sal}\n -Sindicato(5%) > R${(5/100)*sal}\n')
    print(f'Seu salário líquido será de R${desc}')
    
    
    
def ex7():
    tam = float(input('Quantos m²: '))
    
    if tam % 54 == 0:
      qnt = int(tam/54)
    elif tam <= 54:
      qnt = 1
    else:
      qnt = int(tam/54 + 1)
    valor = int(qnt) * 80
    
    print(f'\nVoce deverá comprar {qnt} latas de tinta!\n Custará R${valor} e sobrará {54*qnt - tam}L')
    
