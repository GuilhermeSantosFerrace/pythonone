#constrói uma lista de sequência de números com 3 parâmetros
#o primeiro, é onde ele começa a criar a sequência de números
#o segundo, é onde passamos até onde vai a sequência
#o terceiro, é o intervalo de criação, é opcional, se não colocar nada, o default é 1
for i in range(0, 100, 2):
    print(i)
    if i >= 10:
        break