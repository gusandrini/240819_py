# dicionario = {'chave' : 'valor'}
# type(dicionario)
# <class 'dict'>

dicionario = {'primeiro' :1, 'segundo': 2, 'terceiro' : 3}
dic_1 = dict(primeiro = 1, segundo = 2, terceiro = 3)


#função zip() - concatenas a chave e o valor
dic_2 = dict (zip(['primeiro', 'segundo', 'terceiro'], [1, 2, 3]))
#print(dic_2)

#dicionaria de uma lista de tuplas
tupla1 = ('primeiro' , 1) #tupla: é uma lista fixa estática"
tupla2 = ('segundo', 2)
tupla3 = ('terceiro', 3)

lista = [tupla1, tupla2, tupla3]
#print(lista)

dic_3 = dict(lista)
print(dic_3)

pessoa1 = {'nome': 'Pedro', 'idade': 25, 'altura': 1.75}
print(pessoa1['nome'])
pessoa1.get('nome')
pessoa1.get('peso', 'chave não encontrada')


computador = {'CPU': 'Intel', 'RAM': '16gb', 'SSD': '250gb'}
print(computador)
print(computador.keys()) #retorna as chaves do dicionario em lista
print(computador.values()) #retorna os valores do dicionario em lista

#percorrendo o dicionario
notas = {'PY': 8, 'Java': 5, 'BD': 9.5}
for chave in notas.keys():
    print(f'chave: {chave} e valor: {notas[chave]}')

for chave in computador.keys():
    print(f'chave: {chave} e valor: {computador[chave]}')

for nota in notas.values():
    print(f'Nota: {nota}')


#método items() --> pega um dicionario e devolve uma lista de tuplas
print(f'Elementos: {computador.items()}')


if 'PY' in notas:
    print(f'Está presente no dicionario {notas["PY"]}')

if 8 in notas.values():
    print('Nota existe!')