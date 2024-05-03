preco = int(input('preço das compras'))
print("""
FORMAS DE PAGAMENTO
[1] a vista dinheiro/cheque
[2] a vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")
op = int(input('qual sua opção?'))
if op == 1:
    print(f'com dinheiro/cheque o preço fica {preco * 10 / 100 + preco} reais')
elif op == 2:
    print(f'a vista no cartão o preço fica {preco * 5 / 100 + preco} reais')
elif op == 3:
    print(f'sua compra ficará com 2x de {preco / 2} reais')
else:
    v = int(input('quantas vezes quer parcelar?'))
    print(f'sua compra será parcelada em {v}x de {((preco * 20 / 100) + preco) / v} reais')
    print(f'sua compra de {preco} vai custar {preco * 20 / 100 + preco} reais')