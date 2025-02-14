'''
Exercícios:
https://www.dropbox.com/scl/fi/vigm6n56wdr9qfua3hdn1/Lista-de-Exerc-cios-IV-Python-para-Zumbis.pdf?rlkey=1nce6pkdpsrik2qsrz3achhaq&e=1&dl=0
'''

def l4_ex1():
  from random import randint
  lista = [randint(1, 100) for _ in range(10)]
  maior = lista[0]
  menor = lista[0]
  for num in lista:
    if num > maior:
      maior = num
    if num < menor:
      menor = num
  print(", ".join(str(x) for x in lista))
  print(f'\nCriei uma lisa com 10 números aleatórios entre 0 e 100, sendo: \n Maior > {maior}\n Menor > {menor}')

def l4_ex2():
  from random import randint
  lista = [randint(1, 100) for _ in range(20)]
  par, impar = [], []
  for num in lista:
    if num % 2 == 0:
      par.append(num)
    else:
      impar.append(num)
  print(f'Lista: {", ".join(str(x) for x in lista)}\n\nPares: {", ".join(str(x) for x in par)}\n\nImpares: {", ".join(str(x) for x in impar)}')

def l4_ex3():
  from random import randint
  v1 = [randint(1, 100) for _ in range(10)]
  v2 = [randint(1, 100) for _ in range(10)]
  v3, x = [], 0
  for num in v1:
    x += x
    v3.append(v1[x])
    v3.append(v2[x])
  print(f'Lista 1: {", ".join(str(x) for x in v1)}\n\nLista 2: {", ".join(str(x) for x in v2)}\n\nLista 3: {", ".join(str(x) for x in v3)}')

def l4_ex4():
  from re import sub
  texto = """The Python Software Foundation and the global Python
  community welcome and encourage participation by everyone. Our community is based on
  mutual respect, tolerance, and encouragement, and we are working to help each other live up
  to these principles. We want our community to be more diverse: whoever you are, and
  whatever your background, we welcome you."""
  texto_limpo = sub(r'[^\w\s]', '', texto).lower()
  palavras = texto_limpo.split()
  lista = []
  py = ['p', 'y', 't', 'h', 'o', 'n']
  for palavra in palavras:
    if palavra[0] in py or palavra[-1] in py == True:
      lista.append(palavra)
  print(f'Lista de palavras que começam ou terminam com alguma letra de "Python":\n\n{", ".join(str(x) for x in lista)}')
  
def l4_ex5():
  from re import sub
  texto = """The Python Software Foundation and the global Python
  community welcome and encourage participation by everyone. Our community is based on
  mutual respect, tolerance, and encouragement, and we are working to help each other live up
  to these principles. We want our community to be more diverse: whoever you are, and
  whatever your background, we welcome you."""
  texto_limpo = sub(r'[^\w\s]', '', texto).lower()
  palavras = texto_limpo.split()
  lista = []
  py, n = ['p', 'y', 't', 'h', 'o', 'n'], 0
  for palavra in palavras:
    for letra in palavra:
      if letra in py and len(palavra) > 4:
        lista.append(palavra)
        n += 1
  print(f'Lista com palavras com mais de 4 letras que alguma delas exise na palavra "Python:\n {lista}')