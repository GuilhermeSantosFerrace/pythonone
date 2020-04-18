my_dict = {'chave1': 1.2, 'chave2': 'string'}
'''Dicionários não tem tipos definidos'''
'''Dicionários são flexíveis em tipos de dados, podendo até adicionar outros dicionários dentro deste, porém são organizados apenas pelas chaves, nunca com posições como 0, 1 ou 2'''
print(my_dict)

'''pode-se adicionar valores aos dicionários da seguinte maneira:'''
d = {}
d['key1'] = 'cachorro'
d['key2'] = 'gato'
d['key3'] = 'papagaio'

'''pode-se acessar as chaves do dicionário com:'''
d.keys()
'''ou criar uma lista destas, com:'''
list(d.keys())
list(d.keys())[0]
'''dicionários podem ser considerados também como bancos de dados não-relacionais'''