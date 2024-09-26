'''
Prova para participar do Hackaton Facebook

- Seja dois inteiros positivos n e k. Gere a representação binária de todos os números o intervalo 0 até 2**n-1, inclusive. Esses binários devem ser ordenados em ordem decrescente de acordo com o número de 1's. Retorne o k-ésimo elemento da lista gerada.

Ex: n = 3 e k = 5
A lista ordenada é ['Ob111', '0b11', '0b101', '0b110', '0b1', '0b10', '0b100', '0b0']
O 5 elemento é 'ob1'
'''

# Método 1
def contar_uns(x): return x.count('1')
n, k, lis = 3, 5, []
for element in range(0, 2**n): lis.append(bin(element))
print(sorted(lis, key=contar_uns, reverse=True)[k-1])

# Método 2
n, k = 3, 5
print(sorted((bin(i) for i in range(2**n)), key=lambda x: x.count('1'), reverse=True)[k-1])