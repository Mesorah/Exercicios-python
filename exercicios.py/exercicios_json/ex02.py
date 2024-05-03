import json

nome = input('digite seu nome: ')
idade = int(input('digite sua idade: '))
cidade = input('digite sua cidade: ')

informacoes = {
    'nome': nome,
    'idade': idade,
    'cidade': cidade
}

with open('ex02.json', 'w', encoding='utf8') as arquivos:
    json.dump(informacoes, arquivos)