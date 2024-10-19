'''
Exercícios:
https://www.dropbox.com/scl/fo/qbhx4eko9oq86qoxoojco/ALU8TV7Js7TN2Ef01vri6iA?dl=0&e=3&preview=Lista+11+Google+Python+Class.py&rlkey=v05xowjtnc0wxdfu5i5we694x
'''

#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
# Exercícios básicos com strings

# A. donuts
# Para um inteiro n retorna uma string na forma 'Número de donuts: <n>'
# onde n é o valor passado como argumento.
# Caso n >= 10 devo retornar 'muitos' em lugar do número.
# donuts(5) returns 'Número de donuts: 5'
# donuts(23) returns 'Número de donuts: muitos'
def donuts(n):
    if n >= 10: var = 'muitos'
    else: var = n
    return f'Número de donuts: {var}'

# B. pontas
# Dada uma string s, retorna uma string com as duas primeiras e as duas
# últimas letras da string original s
# Assim 'palmeiras' retorna 'paas'
# No entanto, se a string tiver menos que 2 letras, retorna uma string vazia
def pontas(s):
    if len(s) < 2: return ''
    else: return s[0]+s[1]+s[-2]+s[-1]

# C. fixa_primeiro
# Dada uma string s, retorna uma string onde todas as ocorrências
# do primeiro caracter são trocados por '*', exceto para o primeiro
# Assim 'abacate' retorna 'ab*c*te'
# Dica: use s.replace(stra, strb)
def fixa_primeiro(s):
    if len(s) == 0: return s
    primeiro_caractere = s[0]
    return primeiro_caractere + s[1:].replace(primeiro_caractere, '*')

# D. mistura2
# Sejam duas strings a e b
# Retorno uma string '<a> <b>' separada por um espaço
# com as duas primeiras letras trocadas de cada string
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
def mistura2(a, b):
    lista = [a.replace(a[0:2], b[0:2]), b.replace(b[0:2], a[0:2])]
    return ' '.join(lista)

# E. palindrome
# Verifique se uma string é palíndrome
#   palindrome('asa') True
#   palindrome('casa') False
def palindrome(s):
    lista = list(s)
    if lista == lista[::-1]: return True
    else: return False

# F. busca
# Verifique quantas ocorrências de uma palavra há numa frase
# frase = 'ana e mariana gostam de banana'
# palavra = 'ana'
# busca ('ana e mariana gostam de banana', 'ana') == 4
def busca(frase, palavra):
    contador = indice = 0
    while True:
        indice = frase.find(palavra, indice)
        if indice == -1:
            break
        contador += 1
        indice += 1
    return contador # Tentei com a função "count" porém ele não está considerando letras repetidas...

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'
    print ('%s obtido: %s esperado: %s'
            % (prefixo, repr(obtido), repr(esperado)))

def main():
    print ('donuts')
    test(donuts(4), 'Número de donuts: 4')
    test(donuts(9), 'Número de donuts: 9')
    test(donuts(10), 'Número de donuts: muitos')
    test(donuts(99), 'Número de donuts: muitos')

    print ()
    print ('pontas')
    test(pontas('palmeiras'), 'paas')
    test(pontas('algoritmos'), 'alos')
    test(pontas('a'), '')
    test(pontas('xyz'), 'xyyz')

    print ()
    print ('fixa_primeiro')
    test(fixa_primeiro('babble'), 'ba**le')
    test(fixa_primeiro('aardvark'), 'a*rdv*rk')
    test(fixa_primeiro('google'), 'goo*le')
    test(fixa_primeiro('donut'), 'donut')

    print ()
    print ('mistura2')
    test(mistura2('mix', 'pod'), 'pox mid')
    test(mistura2('dog', 'dinner'), 'dig donner')
    test(mistura2('gnash', 'sport'), 'spash gnort')
    test(mistura2('pezzy', 'firm'), 'fizzy perm')

    print ()
    print ('palindrome')
    test(palindrome('asa'), True)
    test(palindrome('casa'), False)

    print ()
    print ('busca')
    test(busca('ana e mariana gostam de banana', 'ana'), 4)
    test(busca('uma arara ou duas araras', 'ara'), 4)

if __name__ == '__main__':
    main()
