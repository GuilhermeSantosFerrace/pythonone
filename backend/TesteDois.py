#Imprimir cada palavra iniciada em 'm'
st = 'oi meu nome é guilherme'
st2 = st.split()
for letra in st2:
    if letra[0] == 'm':
        print(letra)
print('\n')

#Imprimir cada palavra com tamanho par
st = 'Print every word in this sentence that has an even number os letters'
split_st = st.split()
for i in split_st:
    if len( i ) % 2 == 0:
        print(len(i), i)

#Inteiros de 1 a 100, múltiplos de 3, imprimir 'Fizz', múltilpos de 5, 'Buzz', múltiplos de
#3 e 5, 'FizzBuzz', e os demais números, normalmente
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)