'''Estas são formas de se trabalhar arquivos não-python dentro do código'''
fileOpener = open('Texto.txt')
print(fileOpener.readline())
print(fileOpener.seek(0))
print(fileOpener.readline())