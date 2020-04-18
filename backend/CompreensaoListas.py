'''
AS VARIÁVEIS UTILIZADAS NO FOR, NESTE ESPECÍFICO MOMENTO DE CRIAÇÃO, DEVERÃO TER O MESMO NOME
POR EXEMPLO: i for i in teste
TEREMOS SEMPRE O MESMO NOME ANTES E DEPOIS DO FOR
'''
#A compreensão em listas traz a possibilidade de criar as mesmas listas, se formas menos trabalhosas
x = []
for i in range(0, 30):
    x += [i]
   #ou
   #x.append(i)
   #ambos funcionam da mesma maneira

x2 = [i for i in range(0, 31)]
for i in x2:
    print(i)

x3 = [i * 2 + 10 for i in range(0, 31)]
for i in x3:
    print(i)

#Criando uma lista somenta com números pares
x4 = []
for i in range(0, 100):
    if i % 2 == 0:
        x4 += [i]
print(x4)

#pode ser sintetizado em:
x5 = [i for i in range(0, 100) if i % 2 == 0]
for i in x5:
    print(i)

#podemos usar também essas estruturas para string?
lista = [letter for letter in 'palavra']
print(lista)

#Conversão de temperaturas Celsius para Fahrenheit
celsius = [0, 10, 15, 20, 30, 40, 50, 100]
fahrenheit = [temp * 9/5 + 32 for temp in celsius]
print(celsius)
print(fahrenheit)