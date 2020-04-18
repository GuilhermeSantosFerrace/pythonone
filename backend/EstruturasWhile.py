#funcionamento padrão de um while
x = 1
y = 1
while x < 10 and y < 20:
    print('O valor de x é:', x * y)
    x += 1
    y += 1
else:
    print('O valor de x é:', x * y)

#funcionamento de break
x = 1
lista = []
while True: #ESTRUTURA PERIGOSA: Caso coloque true no código, e não dê a este uma parada, vai rodar para sempre
    lista += [x]
    if x > 10:
        break

#funcionamento de continue
ate = 50
x = 1
while x < ate:
    x += 1
    if x % 2 == 1:
        continue
    if x % 2 == 0:
        print(x, ' é par!!')
    if x > 49:
        break