import json

opcao = int(input('[1] para adicionar, [2]para atualizar, [3] ver: '))

if opcao == 1:

    nome = 'g'
    preco = 5
    quantidade = 5

    informacoes = {
            'nome': nome,
            'preço': preco,
            'quantidade': quantidade
        }


    with open('ex03.json', 'r', encoding='utf8') as arquivo:
        dados_existentes = json.load(arquivo)

    dados_existentes.append(informacoes)

    with open('ex03.json', 'w', encoding='utf8') as arquivo:
        json.dump(dados_existentes, arquivo, indent=2, ensure_ascii=False)

    with open('ex03.json', 'r', encoding='utf8') as arquivo:
        print(json.load(arquivo))

elif opcao == 2:
    with open('ex03.json', 'r', encoding='utf8') as arquivo:
        informacao = json.load(arquivo)
        
        for c in informacao:
            print(c)
    
        qual_quantidade = input("Digite o nome do produto para atualizar a quantidade: ")
        nova_quantidade = int(input("Digite a nova quantidade: "))

        for c in informacao:
            if c['nome'] == qual_quantidade:
                c['quantidade'] = nova_quantidade

        with open('ex03.json', 'w', encoding='utf8') as arquivo:
            json.dump(informacao, arquivo, indent=2, ensure_ascii=False)

elif opcao == 3:
    with open('ex03.json', 'r', encoding='utf8') as arquivo:
        informacao = json.load(arquivo)
        for c in informacao:
            print(c)