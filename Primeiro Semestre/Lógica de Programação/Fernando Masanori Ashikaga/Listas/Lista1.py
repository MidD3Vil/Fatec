'''
Perguntas:
https://www.dropbox.com/scl/fi/n970bl0ekk4y4e05d6wcv/Lista-de-Exerc-cios-I-Python-para-Zumbis.pdf?rlkey=9dlcbzln51t44frad3gdh9ooe&e=1&dl=0
'''

def l1_ex1():
  n1 = float(input('Digite o 1° número: '))
  n2 = float(input('Digite o 2° número: '))
  print('A soma é', n1 + n2)



def l1_ex2():
  m = float(input('Digite um valor em metros: '))
  print(f'Seu valor em milímetros é de {m*1000}')



def l1_ex3():
  valor = input('Digite separado com espaços, respectivamente os valores de DIAS / HORAS / MINUTOS / SEGUNDOS: ').split()
  segtot = int(valor[0])*86400 + int(valor[1])*3600 + int(valor[2])*60 + int(valor[1])
  
  print(f'Voce me informou {int(valor[0])} dias, {int(valor[1])} horas, {int(valor[2])} minutos e {int(valor[3])} segundos... Este tempo representado em segundos é de {segtot} seg')



def l1_ex4():
  sa = float(input('Qual seu salário atual? '))
  au = float(input('Qual o aumento em % do novo salàrio? '))
  
  nv = sa + au / 100 * sa
  print(f'Seu novo salário é {nv}')



def l1_ex5():
  pr = float(input('Quanto custa o produto atual? '))
  des = float(input('Qual o valor do desconto? '))
  nv = pr - des/100 * pr
  print(f'Seu novo produto custa {nv}R$')
  
  
  
def l1_ex6():
  dis = float(input('Qual a distância em KM? '))
  vm = float(input('Velocidade Média por KM/H: '))
  tempo_horas = dis / vm
  tempo_minutos = tempo_horas * 60
  
  horas = int(tempo_horas)
  minutos = int(tempo_minutos % 60)
  
  print(f'O tempo de viagem é de {horas} horas e {minutos} minutos.')
  
  
  
def l1_ex7():
  c = float(input("Digite os graus em Celsius: "))
  f = 9*c/5+32
  print (f'{f}ºFahrenheit')
  
  
  
def l1_ex8():
  f = float(input("Digite os graus em Fahrenheit: "))
  c = ( f - 32 ) * 5/9
  print (f'{c:.2f} Celsius')
  
  
  
def l1_ex9():
  km = float(input('Quantos km rodados? '))
  dias = int(input('Quantos dias alugados? '))
  preco = km * 0.15 + dias * 60
  print(f'Considerando os dias alugados e os km rodados sua conta final foi de R${preco}')
  
  
def l1_ex10():
  qnt = int(input('Digite a quantidade de cigarros que VOCÊ fuma por dia: '))
  ano = int(input('Digite há quantos ANOOOSS você fuma: '))
  
  sla = ano * 365 * qnt * 10
  
  print (f'Você perdeu {sla:.2f} minutos de vida')
  print (f'Você perdeu {sla/1440:.2f} dias de vida')
  
  
  
def l1_ex11():
  print(('O número de dígitos de 2^10.000 é'), len(f'{2**10000}'))