'''
Exercícios:
https://www.dropbox.com/scl/fo/qbhx4eko9oq86qoxoojco/ALU8TV7Js7TN2Ef01vri6iA?dl=0&e=7&preview=Lista+14+Google+Python+Class.py&rlkey=v05xowjtnc0wxdfu5i5we694x
'''

#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Exercícios extras para listas

# D. Dada uma lista de números retorna uma lista sem os elementos repetidos
# PS: se você usar o comando set deve ficar ordenado
# como aparece no resultado dos testes
def remove_iguais(nums):
    return list(set(nums))

# E. Cripto desafio!!
# Dada uma frase, você deve retirar todas as letras repetidas das palavras
# e ordenar as letras que sobraram
# Exemplo: 'ana e mariana gostam de banana' vira 'an e aimnr agmost de abn'
# Dicas: tente transformar cada palavra em um conjunto,
# depois tente ordenar as letras e montar uma string com o resultado.
# Utilize listas auxiliares se facilitar
def cripto(frase):
    resultado = []
    for i in frase.split():

        letras_unicas = sorted(set(i)) 
        palavra_resultado = ''.join(letras_unicas)
        resultado.append(palavra_resultado)
    return ' '.join(resultado)


# F. Derivada de um polinômio
# Os coeficientes de um polinômio estão numa lista na ordem do seu grau.
# Você deverá devolver uma lista com os coeficientes da derivada.
# Exemplo: [3, 2, 5, 2] retorna [2, 10, 6]
# A derivada de 3 + 2x + 5x^2 + 2x^3 é 2 + 10x + 6x^2
def derivada(coef):
    resp = []
    for i in range(1, len(coef)):
        novo_coef = coef[i] * i
        resp.append(novo_coef)
    return resp   

# G. Soma em listas invertidas
# Colocamos os dígitos de dois números em listas ao contrário
# 513 vira [3, 1, 5] e 295 vira [5, 9, 2]
# [3, 1, 5] + [5, 9, 2] = [8, 0, 8]
# pode supor que n1 e n2 tem o mesmo número de dígitos
# Não vale converter a lista em número para somar diretamente
def soma(n1, n2):
    resultado = []
    carry = 0
    
    for i in range(len(n1)):  
        soma = n1[i] + n2[i] + carry              
        resultado.append(soma % 10) 
        carry = soma // 10  # Transbordo é a parte inteira da soma dividida por 10
    if carry > 0:
        resultado.append(carry)
    return resultado

# H. Anagrama
# Verifique se duas palavras são anagramas,
# isto é, uma palavra é permutação das letras da outra
# anagrama('aberto', 'rebato') = True
# anagrama('amor', 'ramo') = True
# anagrama('aba', 'baba') = False
def anagrama(s1, s2):
    for x in s1:
        if x not in s2:
            return False
    i1 = 0
    i2 = 0
    for x in s1:
        i1 = s1.count(x)
        i2 = s2.count(x)
        if i1 != i2:
            return False
    return True  # --> Já estava resolido na lista proposta, eu não alterei

def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'
    print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

def main():
    print ('remove_iguais')
    test(remove_iguais([2, 2, 1, 3]), [1, 2, 3])
    test(remove_iguais([2, 2, 3, 2, 3]), [2, 3])
    test(remove_iguais([]), [])
    
    print ()
    print ('cripto')
    test(cripto('ana e mariana gostam de banana'),
       'an e aimnr agmost de abn')
    test(cripto('Batatinha quando nasce esparrama pelo chão'),
       'Bahint adnoqu acens aemprs elop choã')
    
    print ()
    print ('derivada de polinômio')
    test(derivada([3, 0, 4, 3, 5]), [0, 8, 9, 20])
    test(derivada([4, 16, 1]), [16, 2])
    
    print ()
    print ('soma em listas invertidas')
    test(soma([5, 2, 3, 4], [9, 8, 7, 8]), [4, 1, 1, 3, 1])
    test(soma([3, 1, 5], [5, 9, 2]), [8, 0, 8])
    
    print ()
    print ('anagrama')
    test(anagrama('abacate', 'abacatx'), False)
    test(anagrama('sim', 'xxs'), False)
    test(anagrama('sim', 'siiimmmmm'), False)
    test(anagrama('iracema', 'america'), True)
    test(anagrama('ator', 'rota'), True)
    test(anagrama('aberto', 'rebato'), True)
    test(anagrama('amor', 'roma'), True)
    test(anagrama('ramo', 'amor'), True)
    test(anagrama('baba', 'aba'), False)
    test(anagrama('casa', 'cassa'), False)
    test(anagrama('palmeiras', 'abacate'), False)
    test(anagrama('arco', 'roca'), True)
    test(anagrama('alegria', 'alergia'), True)
    test(anagrama('cantiga', 'catinga'), True)

if __name__ == '__main__':
    main()