'''O for no Python, possui uma estrutura diferente das demais linguagens'''

listaExemplo = [15, 13, 19, 3, 88, 10, 1, 4]
listaExemplo.sort()

for num in listaExemplo:
    if num % 2 == 0:
        print(num, 'é par')
    elif num < 2 and num != 1:
        print('deu ruim')
    else:
        print(num, 'é impar')
print('\n')

#string são iteráveis, sempre
string = 'Isso é uma string'
for char in string:
    print(char)
print('\n')

#podemos usar o FOR nas tuplas também
l = [(1, 2), (3, 4), (5, 6)]
#Temos um método que se chama Tuple Unpacking, que expõe os dados da tupla de maneira a facilitar a interação com estes
(t1, t1) = l[0]
for (t1, t2) in l:
    print(t1 * t2)
print('\n')

#podemos usar o FOR nos dicionários também
d = {'k1': 1, 'k2': 2, 'k3': 3}
for item in d:
    print(item)
print('\nAssim fica diferente: \n')
#também pode ser feito de maneira a expor as keys e seus respectivos valores, como uma tupla
for item in d.items():
    print(item)
print('\n')
#também podemos escolher qual valor queremos entre key e valores, com o Tuple Unpacking
for (key, valor) in d:
    print(valor)
print('\n')
#ou também:
for (key, valor) in d.items():
    print(key, ':', valor)