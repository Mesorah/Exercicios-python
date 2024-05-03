sandwich_orders = ['x-burguer', 'pastrami', 'x-tudo', 'pastrami', 'x-salada', 'pastrami']
finished_sandwiches = []
while 'pastrami' in sandwich_orders:
    print('desculpe não temos pastrami')
    sandwich_orders.remove('pastrami')
tot = len(sandwich_orders)
tott = 0
while tot > 0:
    finished_sandwiches.append(sandwich_orders[tott])
    print(f'seu {sandwich_orders[tott]} está pronto')
    tott += 1
    tot -= 1

toot = 1
for c in finished_sandwiches:
    print(f'{toot}- {c}')

    toot += 1